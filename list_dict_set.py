# Practice 06.12.2021

import collections


def merge_two_dicts(x, y):
    z = x.copy()   # start with x keys and values
    z.update(y)    # modifies z with y keys and values & returns None
    return z


def merge_two_sets(x, y):
    z = x.copy()   # start with x keys and values
    z.union(y)    # modifies z with y keys and values & returns None
    return z

# Task 1
# to convert string to normalized full name
my_incorrect_name = " пчелякова Rюдмила DdD"
my_correct_name = my_incorrect_name.lstrip().replace('R', 'л').replace('DdD', 'николаевна').title()
print(my_correct_name)

# to create a list of letters that make up the name
list_of_my_correct_name_letters = list(my_correct_name)
print(list_of_my_correct_name_letters)

# to sort in ascending order
list_of_my_correct_name_letters.sort()
print(list_of_my_correct_name_letters)

# to replace all "a" with "A"
# the elements of a list can be changed using a for loop
# For this we need the Python enumerate () function.
# This function returns two lists: a list with index numbers and a list with the values
# of the corresponding elements. We can iterate through these two sequences as needed with a single for-loop.

for index, item in enumerate(list_of_my_correct_name_letters):
    if item == 'а':
        list_of_my_correct_name_letters[index] = 'А'

print(list_of_my_correct_name_letters)

# to make unique-letters list
# 1-st way
# converting to set -> converting to list again
set_of_my_correct_name_letters = set(list_of_my_correct_name_letters)
print(set_of_my_correct_name_letters)

list_with_uniq_letters_1 = list(set_of_my_correct_name_letters)
print(list_with_uniq_letters_1)

list_with_uniq_letters_1.sort()
print(list_with_uniq_letters_1)

# 2-nd way
# Unpacking a list into a set
list_with_uniq_letters_2 = [*{*list_of_my_correct_name_letters}]
print(list_with_uniq_letters_2)

list_with_uniq_letters_2.sort()
print(list_with_uniq_letters_2)

# to print the length of the resulting list
len_of_the_list_with_uniq_letters_2 = len(list_with_uniq_letters_2)
print(len_of_the_list_with_uniq_letters_2)


# Task 2
# Create a dictionary, where the keys are letters from the list (task 1),
# and values are the numeric representation of that letter (ord ())
keys = list_with_uniq_letters_2
values = []
for item in list_with_uniq_letters_2:
    values.append(ord(item))

dictionary = dict(zip(keys, values))
print(dictionary)


# Task 3
# get the value by key "a" and by key "A" from the dictionary from task 2.
value_from_key_A = dictionary['А']
print(value_from_key_A)

# ERROR
# the key does not exist
# value_from_key_a = dictionary['a']


# Task 4
# by analogy, execute item 1,2,3 with the last name below yours from Names.
alina_incorrect_name = " гайсюк Rлина DdD"
alina_correct_name = alina_incorrect_name.lstrip().replace('R', 'л').replace('DdD', 'сергеевна').title()
print(alina_correct_name)

list_of_alina_correct_name_letters = list(alina_correct_name)
print(list_of_alina_correct_name_letters)

list_of_alina_correct_name_letters.sort()
print(list_of_alina_correct_name_letters)

for index, item in enumerate(list_of_alina_correct_name_letters):
    if item == 'а':
        list_of_alina_correct_name_letters[index] = 'А'

print(list_of_alina_correct_name_letters)

list_with_uniq_letters_alina = [*{*list_of_alina_correct_name_letters}]
print(list_with_uniq_letters_alina)

list_with_uniq_letters_alina.sort()
print(list_with_uniq_letters_alina)

len_of_the_list_with_uniq_letters_alina = len(list_with_uniq_letters_alina)
print(len_of_the_list_with_uniq_letters_alina)

keys_alina = list_with_uniq_letters_alina
values_alina = []
for item in list_with_uniq_letters_alina:
    values_alina.append(ord(item))

dictionary_alina = dict(zip(keys_alina, values_alina))
print(dictionary)

value_from_key_A_alina = dictionary_alina['А']
print(value_from_key_A_alina)


# Task 5
# to unite dictionaries from task 2 and 4 into one
# 1-st way
# new one dictionary is created
merged_dict = merge_two_dicts(dictionary, dictionary_alina)
print(merged_dict)

# 2-nd way
# modify dictionary by adding some pairs from dictionary_alina
dictionary.update(dictionary_alina)
print(dictionary)


# Task 6
# to create 2 sets (from the keys of dictionaries task 2 and task 4) and unite them
set_from_task_2 = set(dictionary.keys())
print(set_from_task_2)

set_from_task_4 = set(dictionary_alina.keys())
print(set_from_task_4)

# 1-st way
# new one set is created
merged_set = merge_two_sets(set_from_task_2, set_from_task_4)
print(merged_set)

# 2-nd way
# modify dictionary by adding some pairs from dictionary_alina
set_from_task_2.union(set_from_task_4)
print(set_from_task_2)

# Task 7
# to compare the list created from the keys of the dictionary (task 5)
# and the list created from the set (task 6)
list_merged_dict_keys = list(merged_dict.keys())
list_merged_dict_keys.sort()
print(list_merged_dict_keys)

list_merged_set = list(merged_set)
list_merged_set.sort()
print(list_merged_set)

# comparison of 2 lists
if collections.Counter(list_merged_dict_keys) == collections.Counter(list_merged_set):
    print("Equals")
else:
    print("Not equals")
