"""
three files- a.txt, b.txt, and c.txt are located at  under files directory
Then, create a program that:
1. reads each text file and
2. prints out the content of each file in the command line.
The expected output would be like the following:
"""

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f'./files/{filename}', 'r')
    content = file.read()
    # difference between read() and readlines() is that read() method reads the entire content of the file as
    #a single string while readlines also reads entire content but considers each line as an individual string.
    print(content)