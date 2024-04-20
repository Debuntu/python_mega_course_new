user_prompt = "Enter a To Do: "
todos = []


#this loop will continue till the length of todos list is less than 3.
while len(todos) < 3:
    todo = input(user_prompt)
    print(todo.capitalize())       #capitalize method will capitalize only the first letter of the sentence.
    print(todo.title())            #title method will capitalize first letter of each word.
    print(todo.upper())
    print(todo.lower())
    todos.append(todo)
    print(todos)