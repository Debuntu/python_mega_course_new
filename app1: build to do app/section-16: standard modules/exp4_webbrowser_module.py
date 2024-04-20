import webbrowser

user_search = input("Enter your search: ")

# if you search anything on google, you should find this- "https://www.google.com/search?q=" part common, the searched word goes afterwards in
# the browsers url when we search. try it yourself by searching anything in google
webbrowser.open(f"https://www.google.com/search?q={user_search}")
