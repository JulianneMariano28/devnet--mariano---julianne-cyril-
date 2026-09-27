"""
Module 2 — Lesson 3: Loops & Lists
Student: Julianne Cyril S. Mariano
Date: 09/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Lists are used to store multiple values in one variable, while loops allow 
us to repeat a block of code. There are different types of loops. A for loop is 
useful when going through items in a list, while a while loop repeats as long 
as a condition is true. 

============================================
KEY VOCABULARY
============================================
- list: A collection of items stored in a single variable.
- for loop: Repeats a block of code for each item in sequence.
- while loop: Repeats a block of code as long as a condition is true.
- index: The position of an item in a list, starting from 0.
- iteration: One complete repetition of a loop.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

#for loop
songs = ["Cardigan", "August", "Willow", "Delicate"] 
for song in songs: 
       print("Song:", song)

print ()

#while loop
glasses = 0 
while glasses < 8: 
       glasses += 1 
       print("Glasses of water:", glasses) 

print("Daily goal reached!")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Just like in control flows, loops in Python are sensitive in term of indentation. 
Therefore, I should know how to properly implement correct indentation so Python knows 
which statements are part of a loop

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Since we often deal with multiple things at one, loops and lists can be connected to our 
daily routine. For example, we can have a list of tasks, things to buy, or activities we 
need to finish. A loop is similar to going through each item one by one until everything 
is completed.

"""
