import PySimpleGUI as sg
from unzip import extract_archive

sg.theme("DarkTeal7")
label1 = sg.InputText("Choose archive file to extract")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key = "zip_file")


label2 = sg.InputText("Choose destination directory")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key = "folder")
compress_button = sg.Button("Extract")

output_label = sg.Text(key="output", text_color="Black")

layout = [[label1, input1, choose_button1],
          [label2, input2, choose_button2],
          [compress_button, output_label]]

window = sg.Window("Extract the compressed file", layout= layout, font=("Helvetica", 15))

while True:
    event, values = window.read()
    print(event, values)
    filepath = values["zip_file"]
    dest_folder = values["folder"]
    extract_archive(filepath, dest_folder)
    window["output"].update(value="Extraction Completed", font=("Times new Roman", 20))

window.close()