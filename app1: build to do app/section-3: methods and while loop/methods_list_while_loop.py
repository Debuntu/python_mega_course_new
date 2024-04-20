user_prompt = "Enter a To Do: "
todos = []

while True:
    todo = input(user_prompt)
    print(todo.capitalize())       #capitalize method will capitalize only the first letter of the sentence.
    print(todo.title())            #title method will capitalize first letter of each word.
    print(todo.upper())
    print(todo.lower())
    todos.append(todo)
    print(todos)



