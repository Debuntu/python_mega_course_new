import zipfile
import pathlib               # to dynamically get the absolute path of files

def archive_maker(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname = filepath.name)


    if __name__ == "__main__":
        archive_maker(filepaths=["a.txt", "b.txt"])
