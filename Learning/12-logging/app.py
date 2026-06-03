import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[
                        logging.FileHandler('app1.log', mode='w'),
                        logging.StreamHandler()
                    ]
                    )    

logger = logging.getLogger("arithmeticApp")


def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} and {b}, result: {result}")
    return result


def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {b} from {a}, result: {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} by {b}, result: {result}")
        return result
    except ZeroDivisionError as e:
        logger.error(f"Error dividing {a} by {b}: {e}")
        return None
    
add(10, 5)
subtract(10, 5)
divide(10, 0)