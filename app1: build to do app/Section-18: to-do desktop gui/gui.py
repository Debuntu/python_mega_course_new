import PySimpleGUI as sg
import functions

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

# the layout must be a list of lists of datatype created by PySimpleGUI
window = sg.Window("My To-Do App", layout= [[label], [input_box, add_button], [list_box, edit_button]], font=("Times new Roman", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            new_todo = values["todo"] + "\n"
            todos = functions.get_todos()
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todo":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:        #(with this we are enabling the window to be closed when we click on cross button on the window)
            break

window.close()

