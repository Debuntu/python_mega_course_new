"""
write a program that will output like the following-
Enter today's date: 12-21-23
How you rate your mood today from 1 to 8? 7
Let your thoughts flow:
I am exhausted now and almost done for the day.

and finally it will save the "7" and "I am exhausted now and almost done for the day." in a file named 12-23-2023.txt under the directory journal

so the file should contain like following- s
7
I am exhausted now and almost done for the day.
"""

#notice that by default input function will consider entered input as a string unless we specify using int(input()), float(input()) etc.
date = input("Enter today's date: ")
mood = input("How you rate your mood today from 1 to 8? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"./journal/{date}.txt", "w") as file:
    file.writelines(mood + 2*'\n')   #doubling line gap multiplying by 2file
    print(type(mood))
    file.writelines(thoughts)


