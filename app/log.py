import logging
from functools import wraps


def log_decorator(log_file):
    # Configure logging inside the decorator factory
    logging.basicConfig(
        filename=log_file,  # Use the provided log file name
        level=logging.INFO,  # Log level
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
        datefmt='%Y-%m-%d %H:%M:%S'  # Date format
    )

    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            logging.info(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
            result = func(*args, **kwargs)
            logging.info(f"Function '{func.__name__}' returned {result}")
            return result

        return inner_wrapper

    return wrapper
