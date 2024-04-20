# in this part we will open file using with open context manager instead of open. if you open a file using open, you have to close it too
# if you use with open, you don't have to close it as with context manager close the file itself under the hood.
# also we are saving the changes made in edit or complete case in this program.

while True:
    user_actions = input("Type add, show, edit, complete or exit: ")
    user_actions = user_actions.strip()

    match user_actions:
        case "add":
            todo = input("Enter a To Do: ") + "\n"
            #we are storing the user input in a file named todos.txt instead of a predefined empty list [].
            #if the todos.txt file is not located in the current dir, we will have to provide the full path to that file
            with open("todos.txt", "r") as file:
                todos = file.readlines()  # readlines() creates a list you can check it by printing type(todos) here
            todos.append(todo)
            #now we need to save the changes and we are saving in the same file in write mode so we can overwrite the file.
            # with write mode, it can also create a new file if it was not already created.
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            #stripping off the backslash from each elemnt of the todos list using list comprehension.
            new_todos = [todo.strip('\n') for todo in todos]

            for index, item in enumerate(new_todos):
                #we could also strip the backslash here as well
                #item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)
        case "edit":
            todo_number = int(input("Enter number of todos to edit: "))
            new_todo = input("Enter a New To Do: ")

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos[todo_number - 1] = new_todo + '\n'
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        # adding this case to pop an element from the todos list
        case "complete":
            todo_number = int(input("Enter number of todos row  to remove: "))

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos_to_remove = todos[todo_number-1].strip('\n')
            todos.pop(todo_number - 1)

            with open("todos.txt", "w") as file:
                file.writelines(todos)
            message = f"todo {todos_to_remove} was removed from the todos list"
            print(message)
        case "exit":
            break
        case _:
            print("Please Type Again")
print("Bye")
