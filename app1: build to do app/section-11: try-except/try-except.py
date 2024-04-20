"""
in the previous section of code at if-else.py, we have 2 bugs-
1. if we enter something like this to edit or complete-    "edit add a new do", program will be confused
 and consider this an add todo task as it contains "add" in the user's input.
 2. if we enter any string in case of edit or complete it will throw error.

in this part of code, we will modify code to handle bug 1 using startswith() method and will use try-except to handle bug 2.
"""

while True:
    user_actions = input("Type add, show, edit, complete or exit: ")
    user_actions = user_actions.strip()

    if user_actions.startswith("add"):
        todo = user_actions[4:] + "\n"   # here I am slicing the string user_actions to get rest of the string from "add string....."
        # we are storing the user input in a file named todos.txt instead of a predefined empty list [].
        # if the todos.txt file is not located in the current dir, we will have to provide the full path to that file
        with open("todos.txt", "r") as file:
            todos = file.readlines()  # readlines() creates a list you can check it by printing type(todos) here
        todos.append(todo)
        # now we need to save the changes and we are saving in the same file in write mode so we can overwrite the file.
        # with write mode, it can also create a new file if it was not already created.
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_actions.startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()
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

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos[todo_number - 1] = new_todo + '\n'
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        except ValueError:
            print("Command is not valid")
            continue


    elif user_actions.startswith("complete"):
        try:
            todo_number = int(user_actions[9:])

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos_to_remove = todos[todo_number - 1].strip('\n')
            todos.pop(todo_number - 1)

            with open("todos.txt", "w") as file:
                file.writelines(todos)
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
