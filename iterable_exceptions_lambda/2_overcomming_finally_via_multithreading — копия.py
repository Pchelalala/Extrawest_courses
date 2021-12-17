import threading
import time


def overcome_finally_block(a, b):
    try:
        # Checking if try works
        print("Try")
        c = a/b
    except ZeroDivisionError:
        # Checking if except works
        print("Except")

        # Delay. The main thread exits after a second of execution,
        # and the thread with this function only after two
        time.sleep(2)
        return

        # Checking if nothing works after return
        time.sleep(2)
        print("after return")

    finally:
        # Checking if finally works
        print("Finally")


# Thread creation
thread = threading.Thread(target=lambda: overcome_finally_block(1, 0))

# Setting the daemon flag to true.
# If the threads with true-flags remain incompleted,
# then the program terminates without waiting for their execution.
thread.daemon = True

# thread start
thread.start()

# main thread continues working
print("main_1")

# works for 1 second. after that, the thread exits.
# Since the last running thread has the daemon flag set to True,
# then the program exits without waiting for it to complete
time.sleep(1)
print("main_2")

# output:
# Try
# main_1
# Except
# main_2
# Process finished with exit code 0
