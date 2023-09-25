def count_words(text,n):
    compteur = 0
    length=0
    for b in text:

        if b == " " :

            if length == n:
                compteur+=1
                length=0
            else: length=0
        else: length+=1

    return compteur

with open("data.txt", "r", encoding="utf-8") as file:
        file_content = file.read()

n=int(input("enter the length of the word u want:"))
word_count = count_words(file_content,n)

print("Number of words (excluding special characters) in 'data.txt':", word_count)

#regex

import re
try:

    word_length = int(input("Enter a whole number to count words of that size: "))
    
    if word_length <= 0:
        print("Please enter a positive whole number.")
    else:
        with open("data.txt", "r") as file:
            contents = file.read()

            words = re.findall(r'\b\w+\b', contents)

            matching_words = [word for word in words if len(word) == word_length]
            count = len(matching_words)
            print(f"Number of words of length {word_length} in 'data.txt': {count}")
except ValueError:
    print("Invalid input. Please enter a valid whole number.")
except FileNotFoundError:
    print("The 'data.txt' file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
