"""
Coding Exercise 1
Your task is to create a program that generates a random whole number. Here is how the program should behave:
Enter Your Lower Bound: 5
Enter Your Upper Bound: 15
Random Number: 7
"""

import random
lower_bound = int(input("Enter Your Lower Bound: "))     #by default, input() takes str agrument.
upper_bound = int(input("Enter Your Lower Bound: "))
random_number = random.randint(lower_bound, upper_bound)
print(f'Random Number: {random_number}')
