import time

i = 100000000
start_time = time.time()

while i > 0:
    try:
        1
    except:
        1
    finally:
        1
    i -= 1

while_and_exception_handling_time = time.time() - start_time
print(f"{while_and_exception_handling_time} seconds for while and exception handling.")

i = 100000000
start_time = time.time()
while i > 0:
    i -= 1

while_time = time.time() - start_time
print(f"{while_time} seconds for while.")

exception_handling_time = while_and_exception_handling_time - while_time
print(f"{exception_handling_time} seconds for exception handling.")

# output:
# 5.630743980407715 seconds for while and exception handling.
# 4.794489145278931 seconds for while.
# 0.8362548351287842 seconds for exception handling.
# Process finished with exit code 0
