password = input("Enter a password: ")

#password criteria- at least contains 8 character, contains at least one upper case, lower case and a number it will be strong password.
result = []

#first checking if password is of at least 8 character long
if len(password) >= 8:
    print(len(password))
    result.append(True)
else:
    result.append(False)

#checking if there is any digit.
digit = False
for char in password:
    if char.isdigit():
        digit = True
result.append(digit)

#checking if there is any lowercase
lower_case = False
for char in password:
    if char.islower():
        lower_case = True
result.append(lower_case)

#checkinh if there is any uppercase
upper_case = False
for char in password:
    if char.isupper():
        upper_case = True
result.append(upper_case)

print(result)

#in stead of the following way, we can simply use a builtin function all here-
# all(iterable, /) returns True if bool(x) is True for all values x in the iterable.
"""
if False not in result:
    print("Strong Password")
else:
    print("Weak Password")
"""
if all(result) is True:
    print("Strong Password")
else:
    print("Weak Password")
