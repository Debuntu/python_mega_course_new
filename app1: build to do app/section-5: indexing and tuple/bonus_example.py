
filenames = ['textfile.1', 'textfile.2', 'textfile.3']


for file in filenames:
    file = file.replace('.','-', 8)
    print(file)

print(filenames)