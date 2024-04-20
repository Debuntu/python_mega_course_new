filenames = ["1.doc", "1.report", "1.presentation"]

#our goal is to change this list as such filenames = ["1-doc".txt, "1-report.txt", "1-presentation.txt"]

filenames = [filename.replace('.', '-')+'.txt' for filename in filenames]

print(filenames)