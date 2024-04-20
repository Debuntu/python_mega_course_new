#in this part we would like to give user a chance to edit their todos list.

todos = []

while True:
    user_actions = input("Type add, show, output or exit: ")
    #as for example "add" and "add " will not be treated as same in python, we are using strip method to strip off the extra spcae from user input
    user_actions = user_actions.strip()

    match user_actions:
        case "add":
            todo = input("Enter a To Do: ")
            todos.append(todo)
        case "show" | "output":
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case "edit":
            todo_number = int(input("Enter number of todos to edit: "))   #asking user to choose the number from list [1,2,3...]
            new_todo = input("Enter a New To Do: ")
            todos[todo_number - 1] = new_todo     #using indexing to re-assign the todo value to edit
        case "exit":
            break
        # to handle the case when user type something other than "add" "show", "output" or "exit" we are using underscore(_).
        case _:
            print("Please Type Again")
print("Bye")
