'''
real-world example : multiprocessing for cpu bound tasks
scenario : factorial calculation
factorial calculation, especially for large number, involve significant computation work .multiple processing 
can be used to distribute the workload across multiple 
CPU cores, improving proformance
'''

import multiprocessing
import math
import sys
import time

#increase maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

##function to compute factorial of agiven number
def Compute_my_factorial(number):
    print(f'computing factorial of {number}')
    result = math.factorial(number)
    print(f'factoral of no {result}')
    return result

if __name__ == "__main__":
    number= [5000, 6000, 7000]
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results= pool.map(Compute_my_factorial, number)

    end_time = time.time()

    print(f'result {results}')
    print(f'time take :{end_time - start_time} second')
    