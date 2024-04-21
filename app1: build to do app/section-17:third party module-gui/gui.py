import functions
import PySimpleGUI as sg                  # sg is working a variable name for long word PySimpleGUI.

label = sg.Text("Type in a To-Do")
box = sg.InputText(tooltip="Enter To-Do")
button = sg.Button("Add")


display = sg.Window("My To-Do App", layout= [[label], [box, button]] )
display.read()
display.close()
