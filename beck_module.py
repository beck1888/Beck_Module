# curl -O https://raw.githubusercontent.com/beck1888/Beck_Module/main/beck_module.py

# Setting environment variables
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  # Hide pygame support / welcome message

# Try to import all of the modules
try:
    from gtts import gTTS
    import hashlib
    import io
    import importlib
    from mutagen.mp3 import MP3
    import numpy as np
    # import os
    from playsound import playsound
    import pygame
    import requests
    import socket
    import sounddevice as sd
    import sys
    import threading
    import time
    from datetime import datetime
    from PIL import Image
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import subprocess
    from typing import Union, Literal
    from warnings import warn
except:
    exit("1 or more modules is missing that's needed by `beck_module.py`. Please resolve and try again.")

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
    """Uses text to speech to say a message out loud (works offline).
    
    Parameters:
    message_to_speak (str): The message to speak.
    
    Returns:
    None
    """
    os.system("say " + message_to_speak)

def capture_screenshot(url: str, wait_time: int = 2) -> bytes:
    """
    Captures a screenshot of the given URL at 2560x1600 resolution and returns the screenshot as bytes.

    Args:
        url (str): The URL of the webpage to capture.
        wait_time (int, optional): The amount of time to wait for the page to load. Defaults to 2.

    Returns:
        bytes: The screenshot of the webpage as a byte array.
    """
    # Check for websites thar are not supported or disallowed
    blocked_sites = ["reddit"]
    for site in blocked_sites:
        if site.lower() in url.lower():
            raise ValueError(f"Prohibited option. You are not allowed to capture a screenshot of: {site}")

    # Set up the options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=2100,1100")

    # Set up the WebDriver service
    service = Service(executable_path='/Users/beckorion/Documents/Sources/Drivers/chromedriver')

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the URL
        driver.get(url)

        # Wait for the page to load
        wait = WebDriverWait(driver, wait_time)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

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

def google_say(message_to_speak: str, allow_offline_fallback: bool = False, show_warning: bool = True) -> None:
    """Uses google text to speech to say a message out loud."""

    # Ensures the user is online (an internet connection is needed to use google text to speech API)
    if not is_online():
        if allow_offline_fallback:
            if show_warning:
                warn("\033[1;33mFalling back on offline speech. Hide this message by setting show_warning to False.\033[0m")
            say(message_to_speak)
            return
        else:
            raise ConnectionError("An internet connection is needed to use google text to speech API. \nUse say() instead for offline usage: this can also be achieved by setting the allow_offline_fallback parameter to True in the google_say() function call.")

    # Uses the Google Text-to-Speech API to convert text to speech and save it as an audio file
    tts = gTTS(text=message_to_speak, lang='en')
    tts.save('gtts_output.mp3')

    # To play the audio file
    playsound("gtts_output.mp3")

    # To delete the audio file
    os.remove("gtts_output.mp3")

# Using pygame as a better audio player
class Play:
    def __init__(self, filename):
        """
        Initializes a Play object with the given filename.

        Args:
            filename (str): The path to the audio file to be played.
        """
        # Initialize the pygame mixer
        pygame.mixer.init()

        # Store the filename
        self.filename = filename

        # Load the sound from the file
        self.sound = pygame.mixer.Sound(filename)

        # Set the playing flag to False
        self.playing = False

    def length(self):
        """
        Returns the length of the audio file in seconds.

        Returns:
            float: The length of the audio file in seconds.
        """
        audio = MP3(self.filename)
        return audio.info.length

    def _wait_and_clear_playing_flag(self):
        wait(self.length())
        self.playing = False

    def play(self, hold_execution: bool = True, *, die_with_main_thread: bool = False, pause_main_thread: bool = False):
        """
        Plays the audio file.

        Args:
            hold_execution (bool, optional): If True, the function will wait for the audio file to finish playing before continuing. Defaults to True.
            die_with_main_thread (bool, optional): If True, the sound will stop with the main thread (when the __main__ thread exits the sound will be stopped). If False, the sound will play to the end, holding open the __main__ thread even if it reaches the end. Defaults to False.
            pause_main_thread (bool, optional): If True, the __main__ thread will be paused while the sound is playing. Defaults to False.
        """
        if not self.playing:
            self.sound.play()
            self.playing = True

            if hold_execution:
                hold_audio_player_thread = threading.Thread(target=self._wait_and_clear_playing_flag)
                hold_audio_player_thread.daemon = die_with_main_thread
                hold_audio_player_thread.start()

                if die_with_main_thread or pause_main_thread:
                    hold_audio_player_thread.join()
            elif pause_main_thread:
                raise ValueError("Cannot pause the main thread if the execution is not held.")

    def stop(self):
        """
        Stops the audio file if it is currently playing.

        This function stops the audio file if it is currently playing. It sets the playing flag to False and stops the audio file using the pygame mixer.

        Returns:
            None
        """
        # If the audio file is currently playing
        if self.playing:
            # Stop the audio file
            self.sound.stop()
            # Set the playing flag to False
            self.playing = False

## Apple Script UI Functions
def check_if_file_exists(file_path: str) -> bool:
    """
    Checks if a file exists

    Args:
        file_path: The path to the file

    Returns:
        True if the file exists, False otherwise
    """
    return subprocess.call(["test", "-f", file_path]) == 0

def collect_input_ui(message: str, icon_path: str = None) -> str:
    """
    Shows a UI element using Apple Script with an input box

    Args:
        message: The message to show in the input box
        icon_path: The path to the icon to display in the dialog (shows no icon if none is provided)

    Returns:
        The value entered by the user
    """

    if icon_path is not None:
        if not check_if_file_exists(icon_path):
            raise FileNotFoundError(f"File not found: {icon_path}")
        script = (
            'display dialog "{}" default answer "" with icon POSIX file "{}" buttons {{"Submit"}} default button "Submit"'
        ).format(message, icon_path)
    else:
        script = (
            'display dialog "{}" default answer "" buttons {{"Submit"}} default button "Submit"'
        ).format(message)
    
    return subprocess.check_output(["osascript", "-e", script]).decode("utf-8").strip().removeprefix("button returned:Submit, text returned:")

def collect_input_ui_password(message: str, icon_path: str = None) -> str:
    """
    Shows a UI element using Apple Script with an input box

    Args:
        message: The message to show in the input box
        icon_path: The path to the icon to display in the dialog (shows no icon if none is provided)

    Returns:
        The value entered by the user
    """

    if icon_path is not None:
        if not check_if_file_exists(icon_path):
            raise FileNotFoundError(f"File not found: {icon_path}")
        script = (
            'display dialog "{}" default answer "" with hidden answer with icon POSIX file "{}" buttons {{"Submit"}} default button "Submit"'
        ).format(message, icon_path)
    else:
        script = (
            'display dialog "{}" default answer "" with hidden answer buttons {{"Submit"}} default button "Submit"'
        ).format(message)

    return subprocess.check_output(["osascript", "-e", script]).decode("utf-8").strip().removeprefix("button returned:Submit, text returned:")

def popup_ui(message: str, icon_path: str = None) -> None:
    """
    Shows a UI element using Apple Script with an input box

    Args:
        message: The message to show in the input box
        icon_path: The path to the icon to display in the dialog (shows no icon if none is provided)

    Returns:
        None
    """

    if icon_path is not None:
        if not check_if_file_exists(icon_path):
            raise FileNotFoundError(f"File not found: {icon_path}")
        script = (
            'display dialog "{}" with icon POSIX file "{}" buttons {{"Ok"}} default button "Ok"'
        ).format(message, icon_path)
    else:
        script = (
            'display dialog "{}" buttons {{"Ok"}} default button "Ok"'
        ).format(message)
    
    subprocess.check_output(["osascript", "-e", script])

def ask_for_confirmation(message: str, icon_path: str = None) -> bool:
    """
    Shows a UI element using Apple Script with an input box

    Args:
        message: The message to show in the input box
        icon_path: The path to the icon to display in the dialog (shows no icon if none is provided)

    Returns:
        True if the user confirmed, False otherwise
    """

    if icon_path is not None:
        if not check_if_file_exists(icon_path):
            raise FileNotFoundError(f"File not found: {icon_path}")
        script = (
            'display dialog "{}" with icon POSIX file "{}" buttons {{"No", "Yes"}} default button "Yes"'
        ).format(message, icon_path)
    else:
        script = (
            'display dialog "{}" buttons {{"No", "Yes"}} default button "Yes"'
        ).format(message)

    return subprocess.check_output(["osascript", "-e", script]).decode("utf-8").strip().removeprefix("button returned:") == "Yes"

### MAIN ###
# Updater code
def update():
            """Updates the module to the latest version."""
            try:
                r = requests.get("https://raw.githubusercontent.com/beck1888/Beck_Module/main/beck_module.py")
                with open("beck_module.py", "w") as f:
                    f.write(r.content.decode())
                print_formatted("Beck Module updated!", 'green')
            except Exception as e:
                print_formatted("Module update failed. Version is still out of date.", 'light_red')
                print("Details: ", e)

# This code will run on import
if os.environ.get("BECK_MODULE_VERSION_OUTDATE_ALERT") != "hide":
    # Check for updates
    # Get the cloud version hash
    r = requests.get("https://raw.githubusercontent.com/beck1888/Beck_Module/main/beck_module.py")
    cloud_version_hash = hashlib.md5(r.content).hexdigest()

    # Get the local version hash
    with open("beck_module.py", "r") as f:
        local_version_hash = hashlib.md5(f.read().encode()).hexdigest()

    # Compare the hashes
    if cloud_version_hash != local_version_hash:
        print_formatted("Beck Module is out of date. To update, run: python3 beck_module.py update", 'yellow')
        print_formatted("To hide this message, set the BECK_MODULE_VERSION_OUTDATE_ALERT environment variable to 'hide'", 'dark_gray')
