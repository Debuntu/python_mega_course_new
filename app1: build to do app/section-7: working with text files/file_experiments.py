contents = ["I am learning", " Text file processing", "Using Python"]

files = ["file1.txt", "file2.txt", "file3.txt"]

#write a program that will save each of the contents elements in a each of the file in files list.
# for example "file1.txt" should contain "I am learning" and file2.txt should contain "Text file processing"......

#instead of iterating through both the lists, it would be easy to iterate through zip(contents, files).
#zip function produces paired objects combining both the lists like ("I am learning", "file1.txt").....
for content, filename in zip(contents, files):
    file = open(f"./files/{filename}", 'w')      #we are now creating this new files in files directory under current directory
    file.writelines(content)
    file.close()