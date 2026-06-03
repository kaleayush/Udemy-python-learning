from concurrent.futures import ProcessPoolExecutor
import time

def print_number(number):
    time.sleep(2)
    return f"number :{number* number}"

number=[1,2,3,4,5,1,2,3,4,4,4,112,32323,323]

if __name__== "__main__":
    with ProcessPoolExecutor(max_workers= 3) as executors:
        result = executors.map(print_number, number)

    for re in result:
        print(re)

