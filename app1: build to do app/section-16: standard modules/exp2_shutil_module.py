import shutil


# make_archive(basename, format, dir) function will create an archived file (zipr or tar), in this case, a zip file named "output.zip" in the current working dir by combining files under the /files directory under the current directory.
#in case the files are located in other directory, we will have to provide the absolute path of that directory.
shutil.make_archive("output", "zip", "file")
