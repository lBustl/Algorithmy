user_input = input("Please enter a character string: ")

with open("output.txt", "w") as file:

    file.write(user_input)
print(f"String '{user_input}' has been written to 'output.txt'.")
#REGEX TEST
#REGEX TEST
#REGEX TEST
import re

user_input = input("Enter a character string: ")

pattern = r".*"

if re.match(pattern, user_input):
    with open("output.txt", "w") as file:
        file.write(user_input)
    print("String written to 'output.txt'")
else:
    print("Invalid input. Please enter a valid character string.")
