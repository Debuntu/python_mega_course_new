veg = ["kale", "avocado", "asparagus"]

#we are modifying the veg list with a backslash at the end of each item, so when we write on the file, each ietm will be on anew line.
veg_modified = [(item+"\n") for item in veg]

# while writelines function take both string and list as argument, write function takes only string as argument
with open("write_vs_writelines.txt", "w") as file:
    file.writelines(veg_modified)
    file.write("spinach") #if we pass veg_modified list here in the write() function, it will throw error.