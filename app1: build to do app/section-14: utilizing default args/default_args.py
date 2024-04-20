"""explicitly providing filepath value here in the function definition, so for every occurence of the filepath arg in the program,
if we don't specify the filepath, it will take the default filepath value of "../todos.txt".
"""

while True:
    user_actions = input("Type add, show, edit, complete or exit: ")
    user_actions = user_actions.strip()

    def get_todos(filepath="../todos.txt"):
        """reads a text file and returns the list of todo items"""
        with open(filepath, "r") as file_local:
            local_todos = file_local.readlines()
            return local_todos
    print(help(get_todos()))

    #in the below function we have 2 args, look at their order carefully- the default arg should always be followed by the non-default arg.
    def write_todos(todos_arg, filepath="../todos.txt"):
        """write/overwrite a file with given todos arg and filepath"""
        with open(filepath, "w") as file_local:
            return file_local.writelines(todos_arg)


    if user_actions.startswith("add"):
        todo = user_actions[4:] + "\n"
        todos = get_todos()  # we didnt specify any args here, so it will take the default value of "../todos.txt"
        todos.append(todo)

        write_todos(todos)    #write todos function has two arguments/parameters, here we passing only one because the other arg is default.

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
