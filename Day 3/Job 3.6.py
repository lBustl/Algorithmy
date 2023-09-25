import matplotlib.pyplot as plt
import re

# Function to count initial letter occurrences
def count_initial_letters(text):
    initial_letters = {}
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        if word:
            initial_letter = word[0].lower()
            initial_letters[initial_letter] = initial_letters.get(initial_letter, 0) + 1
    return initial_letters

try:
    with open("data.txt", "r") as file:
        contents = file.read()
        initial_letters = count_initial_letters(contents)
        
        total_initial_letters = sum(initial_letters.values())
        
        # Calculate percentage of presence for each initial letter
        initial_letter_percentages = {letter: (count / total_initial_letters) * 100 for letter, count in initial_letters.items()}
        
        # Sort initial letters
        sorted_initial_letter_percentages = {k: v for k, v in sorted(initial_letter_percentages.items())}
        
        # Create a histogram
        plt.bar(sorted_initial_letter_percentages.keys(), sorted_initial_letter_percentages.values())
        plt.xlabel('Initial Letters')
        plt.ylabel('Percentage of Presence (%)')
        plt.title('Percentage of Presence of Initial Letters in data.txt')
        plt.xticks(rotation=45)
        plt.show()
except FileNotFoundError:
    print("The 'data.txt' file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
