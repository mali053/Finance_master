import logging
from functools import wraps


def log_decorator(log_file):
    """
    Decorator factory that creates a decorator to log function calls and their results to a specified log file.

    Args:
        log_file (str): The name of the file where logs will be written.

    Returns:
        function: A decorator that logs the function's name, arguments, and return value.

    Usage:
        @log_decorator('app.log')
        def my_function(arg1, arg2):
            pass

    The log entries will include:
    - Timestamp of the log entry
    - Name of the logger
    - Log level (INFO)
    - Name of the function being called
    - Arguments passed to the function
    - Function's return value
    """

    # Configure logging with the specified log file
    logging.basicConfig(
        filename=log_file,  # Log file name
        level=logging.INFO,  # Log level set to INFO
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
        datefmt='%Y-%m-%d %H:%M:%S'  # Date format for log entries
    )

    def wrapper(func):
        """
        The actual decorator that logs function calls and results.
        Args:
            func (function): The function to be decorated.
        Returns:
            function: The wrapped function that includes logging.
        """

        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            """
            Wrapper function that logs the function call details and the result.
            Args:
                *args: Positional arguments passed to the decorated function.
                **kwargs: Keyword arguments passed to the decorated function.
            Returns:
                The result of the function call.
            """
            logging.info(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
            result = func(*args, **kwargs)
            logging.info(f"Function '{func.__name__}' returned {result}")
            return result

        return inner_wrapper

    return wrapper
