
# multithreading allows us to run multiple threads (tasks, function calls) at the same time.
#  concurrent execution of threads is possible, which can lead to faster execution of tasks,
#  especially when they involve I/O operations or waiting for resources.
# In Python, the `threading` module provides a way to create and manage threads.
# Each thread runs a separate function, and they can run concurrently, 
# allowing for tasks to be performed simultaneously.



import threading
import time


def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)
## In this example, we have two functions: `print_numbers` and `print_letters`.
# Each function prints a series of numbers or letters with a delay of 1 second between prints
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# We create two threads, `thread1` and `thread2`, and assign the target functions to them.
t= time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()
finished_time = time.time()

print(f"Finished in {finished_time - t} seconds")