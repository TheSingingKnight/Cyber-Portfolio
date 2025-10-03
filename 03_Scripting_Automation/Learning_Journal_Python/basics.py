"""
Python Learning Journal: Chapter 1 - Python Basics.

Focus: Demonstrating foundational concepts including print statements, user input,
variable assignment, simple data type conversion, and f-string formatting.
"""

# 1. Print Function: Simple string output to the console.
print('Hello, world!')

# 2. Input and Variable Assignment: Capture user's input and store it as a string variable.
my_name = input('What is your name?\n')

# 3. f-string and String Variable Usage: Use a formatted string literal (f-string) 
#    to combine output with the stored 'my_name' variable.
print(f'It is good to meet you, {my_name}. My name is TheSingingKnight.')

# 4. Built-in Function (len): Calculates and prints the length of the string variable.
print(f'Fun fact, your name is {len(my_name)} letters long!')

# 5. Input and Type Conversion: Capture input, then use int() to convert the string 
#    input into an integer for mathematical calculation.
my_age = input('What is your age?\n')
print(f'You will be {int(my_age) + 1} in a year.')

# End of Chapter 1 - Python Basics
