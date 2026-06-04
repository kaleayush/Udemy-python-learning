from logger import logging

def add(x,y):
    logging.info(f'Adding {x} and {y}')
    return x+y

logging.info('Starting the program')
add(5,10)