import os

a = 4
b = 0

try:
    c = a / b
except ZeroDivisionError:
    print("Division by 0!")
    os._exit(1)
finally:
    print("Is this code always run?")

# output:
# Division by 0!
# Process finished with exit code 1
