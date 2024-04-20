#If you want to get all the text as one single string, use read(). If you want to get separate strings for each line, use readlines().

#if we don't mention file mode, it will be in default read mode.
with open("todos.txt") as file:
    print(file.read())
#however, if we try printing the content outside the 'with open' block  like the one shown below
#as commented out, it will throw errors it cant read a closed file
#print(file.read())

#however, if we store the read contents in a variable, than we can print the content even outside the "with open" block.
with open("todos.txt") as file:
    content = file.read()

print(content)

#the following block of code will print nothing
with open("todos.txt") as file:
    file.read()        #because cursor is already at the end of the file and there is nothing more to read
    content = file.read()
print(content)    #so in this case it will print nothing even though we stored the content in a variable




