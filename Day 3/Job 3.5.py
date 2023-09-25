import matplotlib.pyplot as plt
import re

# Function to count letter occurrences
def count_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

try:
    with open("data.txt", "r") as file:
        contents = file.read()
        letter_count = count_letters(contents)
        
        total_letters = sum(letter_count.values())
        
        # Calculate percentage of appearance for each letter
        letter_percentages = {letter: (count / total_letters) * 100 for letter, count in letter_count.items()}
        
        # Sort the letters alphabetically
        sorted_letter_percentages = {k: v for k, v in sorted(letter_percentages.items())}
        
        # Create a histogram
        plt.bar(sorted_letter_percentages.keys(), sorted_letter_percentages.values())
        plt.xlabel('Letters')
        plt.ylabel('Percentage of Appearance (%)')
        plt.title('Percentage of Appearance of Letters in data.txt')
        plt.xticks(rotation=45)
        plt.show()
except FileNotFoundError:
    print("The 'data.txt' file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


import matplotlib.pyplot as plt
import re

# Function to count word sizes
def count_word_sizes(text):
    word_sizes = {}
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        size = len(word)
        word_sizes[size] = word_sizes.get(size, 0) + 1
    return word_sizes

try:
    with open("data.txt", "r") as file:
        contents = file.read()
        word_sizes = count_word_sizes(contents)
        
        total_words = sum(word_sizes.values())
        
        # Calculate percentage of appearance for each word size
        word_size_percentages = {size: (count / total_words) * 100 for size, count in word_sizes.items()}
        
        # Sort word sizes
        sorted_word_size_percentages = {k: v for k, v in sorted(word_size_percentages.items())}
        
        # Create a histogram
        plt.bar(sorted_word_size_percentages.keys(), sorted_word_size_percentages.values())
        plt.xlabel('Word Sizes')
        plt.ylabel('Percentage of Appearance (%)')
        plt.title('Percentage of Appearance of Word Sizes in data.txt')
        plt.xticks(rotation=45)
        plt.show()
except FileNotFoundError:
    print("The 'data.txt' file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
