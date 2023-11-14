# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: k77
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate



#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    # subclass initiator
    def __init__(self, string_phrase):
        self.string_phrase = string_phrase

    # getter
    def get_string_phrase(self):
        return self.string_phrase

    # check if phrase in text
    def is_phrase_in(self, text):
        # remove punctuation
        t_list = list(text)

        for letter in t_list:
            if letter in string.punctuation:
                i = t_list.index(letter)
                t_list[i] = ' '

        text = ''.join(t_list)

        # get text and phrase and the lists of them
        text = text.lower()
        text_list = text.split()
        phrase = self.get_string_phrase().lower()
        phrase_list = phrase.split()

        # iterate through the text list and check if first word of phrase is equal to any word
        index = 0

        if phrase_list[0] in text_list:
            index = text_list.index(phrase_list[0])

        # now with the correct index, iterate through the phrase list and check if match the text list word by word
        for word in phrase_list:
            # if something goes wrong with the indexing, returns False
            try:
                if word != text_list[index]:
                    return False
            except:
                return False

            index += 1

        return True

# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, string_phrase):
        super().__init__(string_phrase)

    def evaluate(self, story):
        title = story.get_title()
        return super().is_phrase_in(title)

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, string_phrase):
        super().__init__(string_phrase)

    def evaluate(self, story):
        description = story.get_description()
        return super().is_phrase_in(description)

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, datetime_str):
        datetime_obj = datetime.strptime(datetime_str, '%d %b %Y %H:%M:%S')
        self.datetime_obj = datetime_obj

# Problem 6
class BeforeTrigger(TimeTrigger):
    def __init__(self, datetime_str):
        datetime_obj = datetime.strptime(datetime_str, '%d %b %Y %H:%M:%S').replace(tzinfo=pytz.timezone("EST"))
        self.datetime_obj = datetime_obj

    def evaluate(self, story):
        pubdate = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
        if self.datetime_obj > pubdate:
            return True


class AfterTrigger(TimeTrigger):
    def __init__(self, datetime_str):
        datetime_obj = datetime.strptime(datetime_str, '%d %b %Y %H:%M:%S').replace(tzinfo=pytz.timezone("EST"))
        self.datetime_obj = datetime_obj

    def evaluate(self, story):
        pubdate = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
        if self.datetime_obj < pubdate:
            return True


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

# Problem 8
# TODO: AndTrigger

# Problem 9
# TODO: OrTrigger


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    return stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line
        # triggerlist = read_trigger_config('triggers.txt')

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
