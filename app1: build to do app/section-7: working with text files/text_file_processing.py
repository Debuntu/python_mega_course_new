while True:
    user_actions = input("Type add, show or exit: ")
    user_actions = user_actions.strip()

    match user_actions:
        case "add":
            todo = input("Enter a To Do: ") + "\n"
            #we are storing the user input in a file named todos.txt instead of a predefined empty list [].
            #if the todos.txt file is not located in the current dir, we will have to provide the full path to that file
            file = open("todos.txt", "r")      #opens the file in read mode
            todos = file.readlines()  #readlines() creates a list you can check it by printing type(todos) here
            #print(type(todos))
            file.close()

            todos.append(todo)
            #now we need to save the changes and we are saving in the same file in write mode so we can overwrite the file.
            # with write mode, it can also create a new file if it was not already created.
            file = open("todos.txt", "w")
            todos = file.writelines(todos)
            file.close()
        case "show":                         #printed output in this case will have double backslash: one from input("Enter a To Do: ") + "\n"
            file = open("todos.txt", "r")     # and the 2nd one from  print(row)
            todos = file.readlines()
            file.close()
            print(todos)    #see the todos list element has already a backslash in it
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case "edit":
            todo_number = int(input("Enter number of todos to edit: "))
            new_todo = input("Enter a New To Do: ")

            file = open("todos.txt", "r")
            todos = file.readlines()
            print(type(todos))
            todos[todo_number - 1] = new_todo
        case "exit":
            break
        case _:
            print("Please Type Again")
print("Bye")
