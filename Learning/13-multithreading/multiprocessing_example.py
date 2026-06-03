##processes that run in parallel
### CPU-bound tasks can benefit from multiprocessing, as they can utilize multiple CPU cores to perform computations in parallel. This can lead to significant performance improvements for tasks that require intensive computation.
#Prallel execution -multiple core of the CPU can be utilized to run multiple processes simultaneously, which can lead to faster execution of tasks that can be parallelized.
###Improved performance -By using multiple processes, you can take advantage of the full processing power


import multiprocessing
import time


def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"square : {i*i}")

def Cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"square : {i*i*i}")


if __name__ == "__main__":
    #create 2 processes
    p1 = multiprocessing.Process(target = square_numbers)
    p2 = multiprocessing.Process(target= Cube_numbers)

    #start the process
    t= time.time()
    p1.start()
    p2.start()

    ## wait for the process to complete
    p1.join()
    p2.join()
    final_time = time.time()-t
    print(final_time)
