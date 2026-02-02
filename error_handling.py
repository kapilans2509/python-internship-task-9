# Task 9: Exception Handling & Logging

import logging

# Configure logging
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide_numbers(a, b):
    """
    Divides two numbers and handles possible errors.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error("Attempted division by zero")
        print("Error: Cannot divide by zero")
    except TypeError:
        logging.error("Invalid data type used for division")
        print("Error: Please enter numeric values only")
    else:
        print("Division result:", result)
    finally:
        print("Execution completed.\n")

# -------- Simulating runtime errors --------

divide_numbers(10, 2)     # valid
divide_numbers(10, 0)     # ZeroDivisionError
divide_numbers(10, "a")   # TypeError
