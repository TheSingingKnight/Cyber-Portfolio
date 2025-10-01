# My first script. A version on the famous 'Hello World'!
# Showcasing basic scripting ability and concepts.
# The script says hello, asks for your name, age and then gives a whimsically useless fact on both.


print('Hello, world!')
my_name = input('What is your name?\n')
print(f'It is good to meet you, {my_name}. My name is TheSingingKnight.')
print(f'Fun fact, your name is {len(my_name)} letters long!')
my_age = input('What is your age?\n')
print(f'You will be {int(my_age) + 1} in a year.')
