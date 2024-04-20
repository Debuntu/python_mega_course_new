"""
in this part we import a python standard module named "time". to see the details of this module right click on "time"
and then chose "Go To" > Declarations and Usages", it will direct you to time.py module file.

You can find all the standard modules here- https://docs.python.org/3/py-modindex.html    along with all the functions under each of the module.
"""

# time is a built-in python module. We can find the list of all builtin module names by running-
               #import sys
               #sys.builtin_module_names
#to find the library path we can do the following in the python terminal
#import sys
#sys.prefix

#to open the lib folder in mac/linux: type the path (Library/Frameworks/Python.framework/Versions/3.10) you get from the sys.prefix command with 'open' in the beginning of the command (in windows type start instead of open)
#open /Library/Frameworks/Python.framework/Versions/3.10

#built in modules are written in C language and built in inside the python softwere
#while the standard modules come with the python installation as .py scripts.
#Standard library is a jargon that includes both builtin modules written in C and also modules written in Python.
#Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix


import functions
import time


current_time =time.strftime("%B %d, %Y %H:%M:%S")
print(f"It is {current_time}")


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
