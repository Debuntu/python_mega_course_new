"""
Create a program that:
1. generates multiple text files by iterating over the filenames list,
2. and writes the text Hello  inside each generated text file.
"""
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for i in filenames:
    file = open(f'./files/{i}', 'w')   #creating the files under ./files directory
    file.writelines('Hello')
    file.close()

