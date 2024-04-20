password = input("Enter a password: ")

#password criteria- at least contains 8 character, contains at least one upper case, lower case and a number it will be strong password.
result = {}   #storing result in a dictionary this time.

#first checking if password is of at least 8 character long
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

#checking if there is any digit.
digit = False
for char in password:
    if char.isdigit():
        digit = True
result["number"] = digit

#checking if there is any lowercase
lower_case = False
for char in password:
    if char.islower():
        lower_case = True
result["lowercase"] = lower_case

#checkinh if there is any uppercase
upper_case = False
for char in password:
    if char.isupper():
        upper_case = True
result["uppercase"] = upper_case

print(result)


if all(result.values()) is True:
    print("Strong Password")
else:
    print("Weak Password")

