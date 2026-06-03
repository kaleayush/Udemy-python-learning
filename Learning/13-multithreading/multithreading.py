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

#create 2 thread 
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

t= time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()
finished_time = time.time()
print(f"Finished in {finished_time - t} seconds")