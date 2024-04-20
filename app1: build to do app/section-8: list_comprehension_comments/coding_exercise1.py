"""
Coding Exercise 1
Extend the given code (in the exercise area) so the code capitalizes all the names and surnames of the list and then prints the new list. The output of your code should be as below:
['John Smith', 'Jay Santi', 'Eva Kuki']
"""

names = ["john smith", "jay santi", "eva kuki"]

name = [name.title() for name in names]       #capitalize method would capitalize only first letter of each name

print(name)
