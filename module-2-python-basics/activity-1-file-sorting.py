"""
Module 2 — Activity: File Sorting with os and shutil
Student: Julianne Cyril S. Mariano
Date: 09/27/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I built an automated file organizer using Python. It asks for the path of the target folder 
and then scans all the files inside it. The program creates subfolders based on the file types
 and automatically moves each file into its corresponding folder.

============================================
KEY VOCABULARY
============================================
- os module: A python module used to interact with the operating system, such as accessing 
files and creating folders.
- shutil module: A python module used to move, copy, and manage files.
- file path: The location of a file on a computer.
- directory: A folder used to store and organize files.
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

user_folder = input ("Enter the folder path to organize:")

if os.path.exists(user_folder):
    print(f"Proceed to next step.")

    folder = os.listdir(user_folder)
    images = 0
    documents = 0
    videos = 0
    other = 0 

    image = os.path.join(user_folder)
    documents = os.path.join(user_folder)
    videos = os.path.join(user_folder)
    others = os.path.join(user_folder)

    for file in [image, documents, videos, others]:
        if not os.path.exists(file):
            os.mkdir(file)

    for item in folder:
        user_folder = os.path.isdir(user_folder)



else:
    print(f"Error: Can't Continue")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
