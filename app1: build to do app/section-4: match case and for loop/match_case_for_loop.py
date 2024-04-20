#this program will keep asking the user until he/she types "exit'.

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
            #to print out each to do in a seperate line, we are using for loop here
            for item in todos:
                print(item)
        case "exit":
            break
        # to handle the case when user type something other than "add" "show", "output" or "exit" we are using underscore(_).
        case _:
            print("Please Type Again")
print("Bye")
