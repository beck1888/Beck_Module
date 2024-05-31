import time
import importlib
from datetime import datetime
from typing import Union, Literal
import os
import sys
import socket
import numpy as np
import sounddevice as sd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image
import io

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

class Cursor:
    """
    A class to manage the visibility of the cursor in the terminal.
    """

    @staticmethod
    def hide() -> None:
        """
        Hide the cursor in the terminal.
        """
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    @staticmethod
    def show() -> None:
        """
        Show the cursor in the terminal.
        """
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

def wait(seconds: Union[float, int]) -> None:
    """Stops execution for a specified amount of time, the proceeds."""
    time.sleep(seconds)

def print_formatted(text: str, style: Literal['black', 'red', 'green', 'brown', 'blue', 'purple', 'cyan', 'light_gray', 
                                              'dark_gray', 'light_red', 'light_green', 'yellow', 'light_blue', 
                                              'light_purple', 'light_cyan', 'light_white', 'bold', 'faint', 
                                              'italic', 'underline', 'blink', 'negative', 'crossed']) -> None:
    """
    Prints the given text with the specified style.

    Args:
        text (str): The text to be printed.
        style (Literal['black', 'red', 'green', 'brown', 'blue', 'purple', 'cyan', 'light_gray', 
                       'dark_gray', 'light_red', 'light_green', 'yellow', 'light_blue', 
                       'light_purple', 'light_cyan', 'light_white', 'bold', 'faint', 
                       'italic', 'underline', 'blink', 'negative', 'crossed']): The style to print the text with.
                       This includes both colors and text formats.

    Raises:
        ValueError: If the style is not one of the supported styles.
    """
    # ANSI escape codes for colors and text formats
    styles = {
        'black': "\033[0;30m",
        'red': "\033[0;31m",
        'green': "\033[0;32m",
        'brown': "\033[0;33m",
        'blue': "\033[0;34m",
        'purple': "\033[0;35m",
        'cyan': "\033[0;36m",
        'light_gray': "\033[0;37m",
        'dark_gray': "\033[1;30m",
        'light_red': "\033[1;31m",
        'light_green': "\033[1;32m",
        'yellow': "\033[1;33m",
        'light_blue': "\033[1;34m",
        'light_purple': "\033[1;35m",
        'light_cyan': "\033[1;36m",
        'light_white': "\033[1;37m",
        'bold': "\033[1m",
        'faint': "\033[2m",
        'italic': "\033[3m",
        'underline': "\033[4m",
        'blink': "\033[5m",
        'negative': "\033[7m",
        'crossed': "\033[9m",
        'end': "\033[0m"
    }

    # Check if the style is valid
    if style not in styles:
        raise ValueError(f"Unsupported style: {style}. Choose from {', '.join(styles.keys())}.")

    # Print the text with the specified style
    print(f"{styles[style]}{text}{styles['end']}")

def is_online(host: str = "8.8.8.8", port: int = 53, timeout: int = 3) -> bool:
    """
    Check if the computer is online by attempting to connect to a specified host.

    Args:
        host (str): The host to connect to, default is Google's DNS server (8.8.8.8).
        port (int): The port to connect to, default is 53.
        timeout (int): The timeout duration in seconds, default is 3 seconds.

    Returns:
        bool: True if the computer is online, False otherwise.
    """
    try:
        # Create a socket object
        socket_obj = socket.create_connection((host, port), timeout)
        # Close the socket connection
        socket_obj.close()
        return True
    except (OSError, socket.timeout):
        return False
    
def play_beep(frequency: int, duration: float) -> None:
    """
    Play a beep sound at a specified frequency and duration.

    Parameters:
    frequency (int): The frequency of the beep in Hertz.
    duration (float): The duration of the beep in seconds.

    Returns:
    None
    """
    if duration < 0:
        raise ValueError("Duration must be a non-negative float.")
    if frequency <= 0:
        raise ValueError("Frequency must be a positive integer.")
    
    sample_rate = 44100  # samples per second
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    sd.play(wave, sample_rate)
    sd.wait()  # Wait until sound has finished playing

def say(message_to_speak: str) -> None:
    """Uses text to speech to say a message out loud.
    
    Parameters:
    message_to_speak (str): The message to speak.
    
    Returns:
    None
    """
    os.system("say " + message_to_speak)

def capture_screenshot(url: str) -> bytes:
    """
    Captures a screenshot of the given URL at 2560x1600 resolution and returns the screenshot as bytes.

    Args:
        url (str): The URL of the webpage to capture.

    Returns:
        bytes: The screenshot of the webpage as a byte array.
    """
    # Set up the options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=2560,1600")

    # Set up the WebDriver service
    service = Service(executable_path='/Users/beckorion/Documents/Sources/Drivers/chromedriver')

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the URL
        driver.get(url)

        # Capture the screenshot
        screenshot = driver.get_screenshot_as_png()

        # Convert the screenshot to bytes
        screenshot_bytes = io.BytesIO(screenshot)

        # Open the screenshot using PIL
        image = Image.open(screenshot_bytes)

        # Save the screenshot to a byte array
        byte_array = io.BytesIO()
        image.save(byte_array, format='PNG')
        return byte_array.getvalue()
    finally:
        # Quit the WebDriver
        driver.quit()