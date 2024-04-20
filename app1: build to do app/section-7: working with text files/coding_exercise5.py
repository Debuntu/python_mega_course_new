"""create a program that:
1. prompts the user to enter a new member.
2. adds that member to ./files/members.txt at the end of the existing members. For example, the user here has entered the member Solomon Right.

In the above example, Solomon Right will be added to members.txt updating the content of the file to:
John Smith
Sen Lakmi
Sono Octonot
Solomon Right
"""

new_member = input("Enter a new member: ")

#first reading the file and storing its existing members in a list
file = open(f"./files/members.txt", 'r')
existing_members = file.readlines()
file.close()

#adding a new member to the list
existing_members.append(new_member + '\n')    #adding a new line

#reopening the file with write mode to save the changes
file = open(f"./files/members.txt", 'w')
file.writelines(existing_members)
file.close()


