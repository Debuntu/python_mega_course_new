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
