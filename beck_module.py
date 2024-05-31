import time
import importlib
from datetime import datetime
from typing import Union
import os
import sys

def smooth_print(text: str, delay: Union[float, int]) -> None:
    """Prints out a string one character at a time.
    
    Args:
        text (str): The string to print.
        delay (float or int): The amount of time to wait between printing each character.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Create a new line

def package_exists(package_name: str) -> bool:
    """Checks if a package is installed and accessible by the interpreter.
    
    Args:
        package_name (str): The name of the package to check for.

    Returns:
        bool: True if the package is installed and accessible, False otherwise.
    """
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False
    
def get_time() -> str:
    """Gets the current time formatted as HH:MM AM/PM.
    
    Returns:
        str: The system's current time in the specified format.
    """
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    print(time_str)
    return time_str

def clear() -> None:
    """Clears the current terminal."""
    os.system("clear")

def get_date() -> str:
    """Gets the current date formatted as MM/DD/YYYY.
    
    Returns:
        str: The system's current date in the specified format.
    """
    now = datetime.now()
    date_str = now.strftime("%m/%d/%Y")
    print(date_str)
    return date_str

class cursor:
    def hide():
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    def show():
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()