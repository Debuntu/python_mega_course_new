import PySimpleGUI as sg
from zip_maker import archive_maker

label1 = sg.InputText("Choose files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key = "files")


label2 = sg.InputText("Choose destination directory")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key = "folder")
compress_button = sg.Button("Compress")

output_label = sg.Text(key="output", text_color="red")

layout = [[label1, input1, choose_button1],
          [label2, input2, choose_button2],
          [compress_button, output_label]]

window = sg.Window("Compress the selected Files", layout= layout)

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    archive_maker(filepaths, folder)
    window["output"].update(value="Compression Completed")





window.close()