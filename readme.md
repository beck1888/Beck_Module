# Beck Module

## About
The Beck Module is a collection of commonly used functions by Beck in his coding. This module was created so he didn't have to rewrite these functions in every single project file. Therefore, the functions in this module are an assortment of various ones with no common theme or goal. They all have annotations and a docstring for ease of use. I might write documentation for them at some point in the future.

## Use

### Step 1 - Install

#### Install from GitHub
1. From [GitHub](https://github.com/beck1888/Beck_Module)  download `beck_module.py` 
2. Put it into your project's root directory.

#### Install from the command line
1. Navigate to your project's root directory by running: 
    
    `cd /path/to/your/project`


2. Run one of the following commands based on which one your system uses:

    `curl -O https://raw.githubusercontent.com/beck1888/Beck_Module/main/beck_module.py`

    *or*

    `wget https://raw.githubusercontent.com/beck1888/Beck_Module/main/beck_module.py`

3. Check `beck_module.py` and make sure you have all of its dependencies installed. You can install any of them using 

    `pip install package_name`

    or

    `pip3 install package_name`

### Step 2 - Import and use

1. In your project's main file, at the top, type:

    `import beck_module as b` (import method 1 - for if you are only using a few functions)

    `from beck_module import *` (import method 2 - for if you are using many of the functions within)

2. Setup

    1. Replace the filepath for the chromedriver with your own path

3. Use any functions in your project like this

    `b.get_time()` (based on import method 1)

    `b.package_exists('turtle')` (based on import method 1)

    `Cursor.hide()` (based on import method 2)

    `get_date()` (based on import method 2)