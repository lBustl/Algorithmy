with open("output.txt", "r") as file:

        file_contents = file.read()

print("Contents of 'output.txt':")
print(file_contents)

#REGEX TEST

try:
    with open("output.txt", "r") as file:
        contents = file.read()
        print("Contents of 'output.txt':")
        print(contents)
except FileNotFoundError:
    print("The 'output.txt' file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


