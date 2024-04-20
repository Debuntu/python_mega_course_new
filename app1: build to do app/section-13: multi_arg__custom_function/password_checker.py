"""
The function should:
1. get a password argument
2. return the string "Strong Password" if all of the following conditions are true:
- Eight or more characters
- At least one uppercase letter.
- At least one digit.
3. returns "Weak Password" if at least one of the three conditions is not met.
"""

password = input("Enter your password: ")
def strength(password):
    results = []

    if len(password) >= 8:
        results.append(True)

    digit = False
    for char in password:
        if char.isdigit():
            digit = True
    results.append(digit)

    uppercase = False
    for char in password:
        if char.isupper():
            uppercase = True
    results.append(uppercase)

    print(results)

    for result in results:
        if all(results) is True:
            return "Strong password"
        else:
            return "Weak password"


print(strength(password))

