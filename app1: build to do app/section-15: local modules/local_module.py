"""
in this part, we are writing our functions in a separate .py file named functions.py and we will import that functions
or the entire file here. the functions.py file should be in the same directory as the original .py file that will be calling or importing
or should be in a directory named modules.
"""

"""
we can import the functions two ways-
1.directly importing the functions from the file (without .py extension) where it is written for eaxmple- 
    
from functions import get_todos, write_todos 
    
or 

2.importing the entire file (without .py extension) where the functions are defined for example- 

import functions 

in this case we will have to call the function like we call a method -for example: 

functions.get_todos()
functions.write_todos()
"""

import functions


while True:
    user_actions = input("Type add, show, edit, complete or exit: ")
    user_actions = user_actions.strip()


    if user_actions.startswith("add"):
        todo = user_actions[4:] + "\n"
        todos = functions.get_todos()  # we didnt specify any args here, so it will take the default value of "../todos.txt"
        todos.append(todo)

        functions.write_todos(todos)    #write todos function has two arguments/parameters, here we passing only one because the other arg is default.

    elif user_actions.startswith("show"):
        todos = functions.get_todos()
        # stripping off the backslash from each elemnt of the todos list using list comprehension.
        new_todos = [todo.strip('\n') for todo in todos]

        for index, item in enumerate(new_todos):
            # we could also strip the backslash here as well
            # item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_actions.startswith("edit"):
        try:
            todo_number = int(user_actions[5:])
            new_todo = input("Enter a New To Do: ")
            todos = functions.get_todos()
            todos[todo_number - 1] = new_todo + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Command is not valid")
            continue
    elif user_actions.startswith("complete"):
        try:
            todo_number = int(user_actions[9:])
            todos = functions.get_todos()
            todos_to_remove = todos[todo_number - 1].strip('\n')
            todos.pop(todo_number - 1)

            functions.write_todos(todos)
            message = f"todo {todos_to_remove} was removed from the todos list"
            print(message)
        except IndexError:
            print("There is no number with that item")
            continue
    elif user_actions.startswith("exit"):
        break
    else:
        print("Command is not valid")
print("Bye")
