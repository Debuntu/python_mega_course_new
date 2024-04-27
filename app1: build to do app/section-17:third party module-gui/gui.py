import PySimpleGUI as sg                  # sg is working a variable name for long word PySimpleGUI.

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do")
add_button = sg.Button("Add")

# the layout must be a list of lists of datatype created by PySimpleGUI
window = sg.Window("My To-Do App", layout= [[label], [input_box, add_button]] )
window.read()
window.close()
