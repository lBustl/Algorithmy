def count_words(text):
    compteur = 0
    import string

    special = " -&_~#`^@]}¤%§!¨^>><*+="
    for b in text:

        if b== " " :
            compteur+=1
        elif b in special:
            compteur-=1
    return compteur

with open("data.txt", "r", encoding="utf-8") as file:
        file_content = file.read()


word_count = count_words(file_content)
print("Number of words (excluding special characters) in 'data.txt':", word_count)



#regex

import re

try:
    with open("data.txt", "r") as file:
        contents = file.read()

        words = re.findall(r'\b\w+\b', contents)
        word_count = len(words)
        print(f"Number of words without special characters in 'data.txt': {word_count}")
except FileNotFoundError:
    print("The 'data.txt' file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

