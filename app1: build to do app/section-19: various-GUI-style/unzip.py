import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive("/Volumes/Drive C/PycharmProjects/python_mega_course_new/app1: build to do app/Section-18: to-do desktop gui/files/compressed.zip", "/Volumes/Drive C/PycharmProjects/python_mega_course_new/app1: build to do app/Section-18: to-do desktop gui/files/")