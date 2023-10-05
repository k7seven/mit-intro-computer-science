# Problem Set 2, hangman.py
# Name: k77
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_words = []
    for letter in secret_word:
      if letter in letters_guessed:
        guessed_words.append(letter)
      else:
        guessed_words.append("_ ")
    return guessed_words



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = string.ascii_lowercase
    for letter in letters_guessed:
      if letter in available_letters:
        available_letters = available_letters.replace(letter, "")
    return available_letters



def welcome_message(word_length, guesses_left, available_letters):
  print("Welcome to the game Hangman!")
  print("I am thinking of a word that is", word_length, "letters long.")
  print("-------------")
  print("Available letters:", available_letters)



def ask_user_input(available_letters):
  letter_guessed = input("Please guess a letter: ")
  if(letter_guessed.isalpha() and len(letter_guessed) == 1 and letter_guessed in available_letters):
    return letter_guessed
  elif(letter_guessed not in available_letters):
    print("That letter was guessed before.")
    return False
  return False



def is_letter_guessed_correct(letter_guessed, secret_word):
  if(letter_guessed in secret_word):
    return True
  else:
    return False




def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_length = len(secret_word)
    guesses_left = 6
    available_letters = get_available_letters([])
    number_of_warnings = 3
    letters_guessed = []
    word_guessed = False

    # greets the users
    welcome_message(word_length, guesses_left, available_letters)

    # if the user doesnt input correct single alphabet letter
    # reduce the number of warnings
    # if warnings = 0 he loses a guess
    while(is_word_guessed(secret_word, letters_guessed) is False):
      print("You have", guesses_left, "guesses left.")
      letter_guessed = ask_user_input(available_letters)

      # this while loop asks the users for a new input every time he insert an invalid letter
      while(letter_guessed is False):
        number_of_warnings -= 1
        if(number_of_warnings > 0):
          print("Oops! That is not a valid letter. You have", number_of_warnings, "warnings left.")
          print("------------")
        elif(guesses_left == 1 and number_of_warnings == 0):
          print("You ran out of guesses. You lost!")
          print("The word was", secret_word)
          return
        else:
          guesses_left -= 1
          number_of_warnings = 3
          print("Oops! You have no more warnings. You have lost a guess. Your warnings have been reset to 3.")
          print("------------")

        letter_guessed = ask_user_input(available_letters)

      # this append the letter guessed by the user to the letters_guessed list
      letters_guessed.append(letter_guessed)

      available_letters = get_available_letters(letters_guessed)

      if(is_letter_guessed_correct(letter_guessed, secret_word)):
        print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        print("------------")
        print("Available letters:", available_letters)
      elif(letter_guessed in "aeiou"):
        guesses_left -= 2
        print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        print("You lose 2 guessed because it was a vowel.")
        print("------------")
        if (guesses_left <= 0):
          print("You ran out of guesses. You lost!")
          print("The word was", secret_word)
          return
      else:
        guesses_left -= 1
        print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        print("------------")
        if (guesses_left <= 0):
          print("You ran out of guesses. You lost!")
          print("The word was", secret_word)
          return
        print("Available letters:", available_letters)

    print("Congratulations, you won!")





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
