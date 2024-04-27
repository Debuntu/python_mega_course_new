import PySimpleGUI as sg                  # sg is working a variable name for long word PySimpleGUI.

label1 = sg.Text("Choose files from source dir")
input1 = sg.Input()
add_button1 = sg.FileBrowse("Select Source Files")

label2 = sg.Text("Choose destination dir")
input2 = sg.Input()
add_button2 = sg.FolderBrowse("Select Destination Directory")

compress_button = sg.Text("Compress")



# the layout must be a list of lists of datatype created by PySimpleGUI
display = sg.Window("File Zipper",
                    layout= [[label1, input1, add_button1], [label2, input2, add_button2],
                             [compress_button]])


display.read()
display.close()