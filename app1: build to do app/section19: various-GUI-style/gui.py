## in the final version, we will adjust for some error while clicking "Edit" or "Complete" button before selecting todos from list.

import PySimpleGUI as sg
import functions
import time

sg.theme("BrightColors")   #see available themes online for pysimpleGUI

live_clock = sg.Text('', key="clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# the layout must be a list of lists of datatype created by PySimpleGUI
window = sg.Window("My To-Do App", layout= [[live_clock],
                                            [label],
                                            [input_box, add_button],
                                            [list_box, edit_button, complete_button],
                                            [exit_button]], font=("Times new Roman", 20))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d %Y %H %M %S"))
    print(event)
    print(values)

    match event:
        case "Add":
            new_todo = values["todo"] + "\n"
            todos = functions.get_todos()
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value=" ")   ##to clean the input box after each button selection
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value=" ")
            except:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_remove = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value=" ")
            except:
                sg.popup("Please select an item first")
        case "todo":
            window["todo"].update(value=values["todos"][0])
        case "Exit":
            break

window.close()

