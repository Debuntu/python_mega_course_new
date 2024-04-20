options_1 = """
What are dolphins?
1-Amphibians
2-Fish
3-Mammals
4-Birds
"""

options_2 = """
What occupies most of the earth's surface?
1-Land
2-Water
"""
correct_ans1 = "3"
correct_ans2 = "2"

result = []
user_inputs = []

print(options_1)
user_ans1 = input("Enter your answer: ")
print(user_ans1)
user_inputs.append(user_ans1)

if user_ans1 == correct_ans1:
    result.append(True)
    with open("bonus_example_output.txt", 'w') as file:
        content = f'1 Correct Answer:User Answer: {user_ans1}, Correct Answer: {correct_ans1}'
        file.writelines(content + '\n')
else:
    result.append(False)
    with open("bonus_example_output.txt", 'w') as file:
        content = f'1 Incorrect Answer:User Answer: {user_ans1}, Correct Answer: {correct_ans1}'
        file.writelines(content + '\n')

print(options_2)
user_ans2 = input("Enter your answer: ")
print(user_ans2)
user_inputs.append(user_ans2)

if user_ans2 == correct_ans2:
    result.append(True)
    with open("bonus_example_output.txt", 'r') as file:
        data = file.readlines()
    with open("bonus_example_output.txt", 'w') as file:
        content = f'2 Correct Answer:User Answer: {user_ans2}, Correct Answer: {correct_ans2}'
        data.append(content)
        file.writelines(data)

else:
    result.append(False)
    with open("bonus_example_output.txt", 'r') as file:
        data = file.readlines()
    with open("bonus_example_output.txt", 'w') as file:
        content = f'2 Incorrect Answer:User Answer: {user_ans2}, Correct Answer: {correct_ans2}'
        data.append(content)
        file.writelines(data)

print(result)
