# this program will keep asking the user until he/she types "exit'.

todos = []

while True:
    user_actions = input("Type add, show or exit: ")
    match user_actions:
        case "add":
            todo = input("Enter a To Do: ")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            break
print("Bye")

