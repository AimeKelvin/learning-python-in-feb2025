name = input("Enter your name, but don't go more than 12 characters: ")
name = name.replace(' ', '-')
name = f'Your name is {name}' if len(name)<12 else "name exceeds max characters(12) please enter a short name 😅"
print(name)
