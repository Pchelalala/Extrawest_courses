# Lecture 1
# 26.11.2021

import sys

# Task 1
# to find out the maximum possible value of an integer variable
print("Task 1")

# some explanation
# in Python value of an integer is not restricted by the number of bits
# and can expand to the limit of the available memory

# solution #1.1
# sys.maxsize is an integer which contains the maximum value
# that a variable of type Py_ssize_t can take.
# 2 ^ (31 - 1) on a 32-bit platform
# 2 ^ (63 - 1) on a 64-bit platform

print(sys.maxsize)
# 9223372036854775807

print(type(sys.maxsize))
# <class 'int'>

print(sys.maxsize == 2**63 - 1)
# True

# solution #1.2
# the maximum possible value of an integer variable on current device
# the exact number will be found, but it will take too much time
current_max_int = sys.maxsize
while 1:
    current_max_int += 1

# solution #1.3
# the maximum possible value of an integer variable on current device
# my stupid algorithm consists of 2 parts:
# 1) to find approximate value of max integer by exponentiation
# in order to save time
# 2) to find exact value of max integer by incrementing the approximate value,
# which was found before the error interrupt the first cycle
# this should be done because the max integer is in
# range [<last_successfully_received_value_from_first_cycle> and <error_value - 1>]

current_max_int_not_exact = sys.maxsize
while 1:
    current_max_int_not_exact += current_max_int_not_exact ** 100

current_max_int_from_not_exact_to_exact = current_max_int_not_exact

while 1:
    current_max_int_from_not_exact_to_exact += 1


# Task 2
# to demonstrate inaccuracies in calculating monetary amounts using the floating point data type
print("\nTask 2")

# some explanation about the essence of the problem
# in the float data type, the number is represented as sums of powers with base 2,
# while monetary amounts in all prices and documents are represented in decimal notation.
# Most decimal numbers are not exactly represented as a finite sum of powers of two.

# how we can solve the problem
# to represent the monetary amount as sums of powers with base 10

# here the problem is:
# program output: 100.0100000000000051159076974727213382720947265625
price = 100.01
print(Decimal(price))

# logically, subsequent calculations will lead to inaccuracies,
# which is often unacceptable while working with monetary amounts


# Task 3
# to fix the problem from Task 2
# (some inaccuracies in calculating monetary amounts using the floating point data type)
print("\nTask 3")

# solution #3.1 (bad solution)
# floating point representation in str using the type casting
price_converted_to_str = str(price)
print(Decimal(price_converted_to_str))

# solution #3.2 (a little bit better than previous one, but the logic is the same)
# floating point representation in str using the built-in repr()
price_converted_to_str_by_repr = repr(price)
print(price_converted_to_str_by_repr)

# however, there are some errors
# price2 = price_converted_to_str + 100
# price2 = price_converted_to_str_by_repr + 100

# one more type casting is needed to overcome the errors
price_converted_back_to_digit_1 = Decimal(price_converted_to_str)
print(price_converted_back_to_digit_1)

price_converted_back_to_digit_2 = Decimal(price_converted_to_str_by_repr)
print(price_converted_back_to_digit_2)

# solution #3.3 (still not so good solution)
# the problem of this solution is that the precision is limited
price_formatted = format(price, ".2f")
print(price_formatted)


# Task 4
# to find out the maximum possible length of a string variable
print("\nTask 4")

# some explanation
# Python itself has no specific limit on the length of a string.
# In the process of usage, it is necessary to take into account the performance of the computer
# and the effectiveness of the program.

# solution #4.1
# the maximum possible value of str variable on current device
# the exact number will be found, but it will take too much time
current_max_str = ""
current_max_str_size = 0
while 1:
    current_max_str += 'a'
    current_max_str_size = len(current_max_str)

# Also I could write the same shit as in solution #1.3 (max value of integer)
# with two cycles, but there should be a more rational solution, than mine


# Task 5
# to find out the size of boolean variable
print("\nTask 5")

is_smth = True
print("Amount of memory in bytes, which was allocated for is_smth = " + str(sys.getsizeof(is_smth)))

# a number of set bits
number_of_set_bits = bin(64).count("1")
print("Number of set bits = " + str(number_of_set_bits))

# a number of unset bits
number_of_unset_bits = bin(64).count("0")
print("Number of unset bits = " + str(number_of_unset_bits))

# another way to count a number of set bits using bitwise operations
number_of_set_bits2 = 0
while is_smth:
    number_of_set_bits2 += 1
    is_smth &= is_smth-1

print("Number of unset bits counted by another way = " + str(number_of_set_bits2))