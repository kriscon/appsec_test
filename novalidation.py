user_input = input("Enter filename: ")

with open(user_input, 'r') as file:

    content = file.read()