'''
Lists -> Sequence of something
       -> Collection of any data type
       -> Mutable
       -> Created with []
'''
# declaring a list
list_example = [1, 5, "k77"]
print("Before mutation:", list_example)

# lists are mutable
list_example[0] = 15
print("After mutation:", list_example)

# lists can be concatenated
# this method doesnt mutate the list
list_2 = [True, False, "programming"]
list_3 = list_example + list_2
print("Concatenated list:", list_3)
print("List 2:", list_2)

# this method mutates the list
list_example.extend(list_2)
print("List with extend:", list_example)

# list elements can be deleted
# del() can be used to delete an element at a specific index
# It mutates the list
del(list_2[1])
print("List 2 index 1 removed from the list", list_2)

# remove() deletes the element from the list
# if there is duplication of the element, removes the first one
new_list = [1, 2, 3, 2, 4]
print("New list before using remove:", new_list)
result = new_list.remove(2)
print("New list after using remove:", new_list)

# pop removes the last element of the list
list_3.pop()
print("After pop:", list_3)

# lists can be sliced
sliced_list = list_3[1:4]
print("Sliced list", sliced_list)

# we can append new items to the list
sliced_list.append(99)
print("Appended list:", sliced_list)

# we can apply len() to know how many elements it has
print("Sliced list has:", len(sliced_list), "elements")
print("List 3 has:", len(list_3), "elements")

# can be converted to string and vice-versa, it doesnt mutated the string
string_example = "Hello"
string_example_list = list(string_example)
print("String to list with list():", string_example_list)

# split can also convert on an specific character, it doesnt mutated the string
# split on spaces if called without a parameter
string_split = string_example.split('e')
print("String using split('e'):", string_split)

# join can be used to convert from list to string
# the char between '' will be put between elements of list
string_from_list = ''.join(string_example_list)
print("String from list using join:", string_from_list)

# aliasing is when multiple variables point to the same thing, therefore if when mutated all of the variables will change
aliasing_example = ["New", "List", "Aliasing", "Is", "Cool"]
print("Aliasing example before another variable call pop:", aliasing_example)
another_aliasing_list = aliasing_example
another_aliasing_list.pop()
print("Aliasing Example after another variable call pop:", aliasing_example)

# how to clone a list
# cloning is good when no need to mutate the list
cloning_example = aliasing_example[:]
print("This is a clone of the aliasing example list before:", cloning_example)
cloning_example.pop()
print("This is cloning example after pop call:", cloning_example)
print("This is aliasing example after pop is called in the cloning example:", aliasing_example)

# sort and sorted
# sort mutates, storted doesnt
# sort doesnt return anything and mutates the list
sort_example = [1, 4, 8, 2, 6, 9, 3]
print("Unsorted list before sort():", sort_example)
sort_example.sort()
print("Sorted list after sort():", sort_example)

# sorted returns the sorted list and doesnt mutate
sort_example_2 = [1, 4, 8, 2, 6, 9, 3]
print("Unsorted list before sorted(list):", sort_example_2)
sorted_list = sorted(sort_example_2)
print("New sorted list after sorted(list):", sorted_list)
print("Unsorted list still intact:", sort_example_2)

# example of nested lists and how mutation must be watched out for
american_tennis_players = ["Shelton", "Murray"]
european_tennis_players = ["Federer", "Nadal", "Djokovic"]
world_tennis_players = [american_tennis_players]
world_tennis_players.append(european_tennis_players)
print("World tennis players after we assign american and append europeans:", world_tennis_players)
european_tennis_players.pop()
print("World tennis players after pop on europeans:", world_tennis_players)

# mutation and iteration
# the code below doesnt work because python in the background on the for loop doesnt update the index along with the list
# the index counter will go over number 2 because we removed the first element and the index doesnt get -1 also, thats why we go over
list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 5, 6]

def remove_dups(list_1, list_2):
    for e in list_1:
        if e in list_2:
            list_1.remove(e)

    return list_1

removed_dups = remove_dups(list_1, list_2)
print("Removed dups without a copy:", removed_dups)

# to make it work we need a clone of the list and then iterate over the clone but remove on the main one
def correct_remove_dups(list_1, list_2):
    copy_list_1 = list_1[:]
    for e in copy_list_1:
        if e in list_2:
            list_1.remove(e)

    return list_1

correct_removed_dups = correct_remove_dups(list_1, list_2)
print("Correct removed dups:", removed_dups)
