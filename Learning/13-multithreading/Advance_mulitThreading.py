#multi processing  with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time

from numpy import number

def print_number(number):
    time.sleep(1)
    return f"number :{number}"

number=[1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(print_number, number)

for re in result:
    print(re)   