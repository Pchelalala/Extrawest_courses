# Practice 29.11.2021
print("\n\n29.11.2021")

# Part 1 - expression operations
a = 104
b = 78
print("a = " + str(a) + "\nb = " + str(b))

# addition for int
add = a + b
print("\nIf a and b are int:\na + b = " + str(add))

# addition for str
add_str = str(a) + str(b)
print("\nIf a and b are str:\na + b = " + add_str)

# subtraction
a_minus_b = a - b
b_minus_a = b - a
print("\na - b = " + str(a_minus_b) + "\nb - a = " + str(b_minus_a))

# multiplication
product = a * b
print("\na * b = " + str(product))

# exponentiation
exponentiation = a ** b
print("\na ** b = " + str(exponentiation))

# division
division = a / b
print("\na / b = " + str(division))

# integer division
integer_division = a // b
print("\na // b = " + str(integer_division))

# modulo division
modulo_division = a % b
print("\na % b = " + str(modulo_division))

# right shift
right_shift_a_to_b = a >> b
right_shift_b_to_a = b >> a
print("\na >> b = " + str(right_shift_a_to_b) + "\nb >> a = " + str(right_shift_b_to_a) )

# left shift
left_shift_a_to_b = a << b
left_shift_b_to_a = b << a
print("\na << b = " + str(left_shift_a_to_b) + "\nb << a = " + str(left_shift_b_to_a) )

# bitwise and
bitwise_and = a & b
print("\na & b = " + str(bitwise_and))

# bitwise or
bitwise_or = a | b
print("\na | b = " + str(bitwise_or))

# bitwise exclusively or
bitwise_exclusively_or = a ^ b
print("\na ^ b = " + str(bitwise_exclusively_or))

# bitwise not
bitwise_not_a = ~a
print("\n~a = " + str(bitwise_not_a))

bitwise_not_b = ~b
print("\n~b = " + str(bitwise_not_b))

# comparison
# >
is_a_bigger_than_b = a > b
is_b_bigger_than_a = b > a
print("\nis_a_bigger_than_b: " + str(is_a_bigger_than_b) + "\nis_b_bigger_than_a: " + str(is_b_bigger_than_a))

# <
is_a_less_than_b = a < b
is_b_less_than_a = b < a
print("\nis_a_less_than_b: " + str(is_a_less_than_b) + "\nis_b_less_than_a: " + str(is_b_less_than_a))

# >=
is_a_bigger_or_equals_b = a >= b
is_b_bigger_or_equals_a = b >= a
print("\nis_a_bigger_or_equals_b: " + str(is_a_bigger_or_equals_b)
      + "\nis_b_bigger_or_equals_a: " + str(is_b_bigger_or_equals_a))

# <=
is_a_less_or_equals_b = a <= b
is_b_less_or_equals_a = b <= a
print("\nis_a_less_or_equals_b: " + str(is_a_less_or_equals_b)
      + "\nis_b_less_or_equals_a: " + str(is_b_less_or_equals_a))

# ==
is_a_equals_b = a == b
print("\nis_a_equals_b: " + str(is_a_equals_b))

# !=
is_a_not_equals_b = a != b
print("is_a_not_equals_b: " + str(is_a_not_equals_b))

# logical operations
# not (logical not) - returns True if expression is False
not_is_a_equals_b = not is_a_equals_b
print("\nlogical operations\nnot: not_is_a_equals_b: " + str(not_is_a_equals_b))

# and (logical multiplication)
is_a_and_b_less_than_100 = a < 100 and b < 100
print("\nand: is_a_and_b_less_than_100: " + str(is_a_and_b_less_than_100))

# or (logical addition) - returns True if at least one of the expressions is True
is_a_or_b_less_than_100 = a < 100 or b < 100
print("\nor: is_a_or_b_less_than_100: " + str(is_a_or_b_less_than_100))


# Part 2 - String
print("\nString")

first_name_letter = "л"
patronymic = "николаевна"
start_string = "пчелякова Rюдмила DdD"
print("start: " + start_string)

# str. partition() splits the string based on the separator into a tuple of three lines.
# The first line is the part before the delimiter,
# the second line is the part after the delimiter,
# the third line is the part after the delimiter.
cortege_before_template_after = start_string.partition("DdD")
print(cortege_before_template_after)

# storing the surname and name (the zero element of the tuple) into a variable
surname_and_name = cortege_before_template_after[0]
print(surname_and_name)

surname_and_name_fixed = surname_and_name.replace('R', first_name_letter)
print(surname_and_name_fixed)

full_name = surname_and_name_fixed + patronymic
print(full_name)

full_name_with_capital_letters = full_name.title()
print(full_name_with_capital_letters)