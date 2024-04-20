"""
glob() function Returns a list of paths matching a pathname pattern.
The pattern may contain simple shell-style wildcards a like fnmatch. However, unlike fnmatch, filenames starting with a
dot are special cases that are not matched by '*' and '?' patterns
If recursive is true, the pattern '**' will match any files and  zero or more directories and subdirectories.
"""
import glob     # importing glob module
filepaths = glob.glob("*.txt")   #glob() function Returns a list of paths matching a pathname pattern.
print(filepaths)

#reading each file for that filepath list and printing its content
for filepath in filepaths:
    with open(filepath, 'r') as file:
        print(file.read())

