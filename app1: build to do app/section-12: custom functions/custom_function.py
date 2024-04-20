 #in this part of rthe code, we defined two functions- one with no argument and other with an argument todos_arg to reduce
# the repetitive lines of codes.

while True:
    user_actions = input("Type add, show, edit, complete or exit: ")
    user_actions = user_actions.strip()

    def get_todos():
        with open("todos.txt", "r") as file_local:
            local_todos = file_local.readlines()
            return local_todos
    def write_todos(todos_arg):
        with open("todos.txt", "w") as file_local:
            return file_local.writelines(todos_arg)


    if user_actions.startswith("add"):
        todo = user_actions[4:] + "\n"
        todos = get_todos()  # calling the get_todos function here to read the todos.txt file
        todos.append(todo)
        write_todos(todos)  # calling the write_todos function and passing todos as argument.

    elif user_actions.startswith("show"):
        todos = get_todos()
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
            todos = get_todos()
            todos[todo_number - 1] = new_todo + '\n'
            write_todos(todos)

        except ValueError:
            print("Command is not valid")
            continue


    elif user_actions.startswith("complete"):
        try:
            todo_number = int(user_actions[9:])
            todos = get_todos()
            todos_to_remove = todos[todo_number - 1].strip('\n')
            todos.pop(todo_number - 1)

            write_todos(todos)
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
