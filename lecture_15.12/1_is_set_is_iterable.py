"""
In Python, Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements
Some of the ways to iterate through set in python are:
  1. Using for loop statement
  2. Enumerating over a set
  3. Using iter with for loop
  4. Converting the set to a list
  5. Using comprehension
  6. Iterating over two sets simultaneously using zip()
"""

set_to_check = {'Hello', ',', 'world', '!', '!', ')'}
print(type(set_to_check))

# 1-st way
# Using for loop statement
for item in set_to_check:
    print(item)

# 2-nd way
# Enumerating over a set
# When we use enumerate() method, we receive a counter along with the iterable item.
for counter, item in enumerate(set_to_check):
    print(counter, ':', item)

# 3-rd way
# Using iter with for loop
# The iter() method returns an iterator. Using that iterator, we can iterate over a given object.
for item in iter(set_to_check):
    print(item)

# 4-th way
# Converting the set to a list
convert_set_to_list = list(set_to_check)

# iterating over convert_set_to_list using indexing.
for i in range(0, len(convert_set_to_list)):
    print(convert_set_to_list[i])

# using a while loop
i = 0
while i < len(convert_set_to_list):
    print(convert_set_to_list[i])
    i += 1

# 5-th way
# using comprehension
# Comprehension in python is a compact piece of code used to generate new sequences from already existing sequences.
# Comprehension consists of three main parts:
#  1. the expression to be printed
#  2. the iterable item
#  3. the list, which is the sequence
val = [print(item) for item in set_to_check]

# 6-th way
# iterating over two sets simultaneously using zip()
# The zip function returns a zip object.
# With that, we can iterate over two or more iterables simultaneously.
# This saves a lot of computation time because multiple sequences are iterated simultaneously.
set1 = {1, 2, 3, 4}
set2 = {'A', 'B', 'C', 'D'}
for (i1, i2) in zip(set1, set2):
    print(i1, i2)