import matplotlib.pyplot as plt
import re

def count_next_letter_occurrences(text):
    letter_occurrences = {}
    words = re.findall(r'\b\w+\b', text)
    
    for word in words:
        for i in range(len(word) - 1):
            current_letter = word[i].lower()
            next_letter = word[i + 1].lower()
            
            if current_letter not in letter_occurrences:
                letter_occurrences[current_letter] = {}
            
            if next_letter not in letter_occurrences[current_letter]:
                letter_occurrences[current_letter][next_letter] = 1
            else:
                letter_occurrences[current_letter][next_letter] += 1
                
    return letter_occurrences

try:
    with open("data.txt", "r") as file:
        contents = file.read()
        letter_occurrences = count_next_letter_occurrences(contents)
        
        plt.figure(figsize=(12, 8))
        
        for current_letter, next_letters in letter_occurrences.items():
            total_next_letters = sum(next_letters.values())
            
            # Calculate percentage of appearance for each next letter
            percentages = {letter: (count / total_next_letters) * 100 for letter, count in next_letters.items()}
            

            sorted_percentages = {k: v for k, v in sorted(percentages.items())}
            
            plt.plot(list(sorted_percentages.keys()), list(sorted_percentages.values()), label=current_letter)
        
        plt.xlabel('Next Letters')
        plt.ylabel('Percentage of Appearance (%)')
        plt.title('Percentage of Appearance of Next Letters Following Each Letter')
        plt.legend(title='Current Letter')
        plt.xticks(rotation=45)
        plt.show()
        
except FileNotFoundError:
    print("The 'data.txt' file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

import random

def generate_word(length, initial_letter, letter_sequence, statistics):
    word = initial_letter
    current_letter = initial_letter
    for _ in range(length - 1):
        if current_letter in statistics and letter_sequence in statistics[current_letter]:
            next_letters = list(statistics[current_letter][letter_sequence].keys())
            probabilities = list(statistics[current_letter][letter_sequence].values())
            next_letter = random.choices(next_letters, probabilities)[0]
            word += next_letter
            current_letter = next_letter
        else:
            break
    return word

# test
word_length = 5
initial_letter = 'a'
letter_sequence = 'b'

generated_word = generate_word(word_length, initial_letter, letter_sequence, letter_occurrences)
print("Generated Word:", generated_word)

import matplotlib.pyplot as plt
import re

def count_words_per_sentence(text):
    sentences = re.split(r'[.!?]', text)
    sentence_lengths = [len(re.findall(r'\b\w+\b', sentence)) for sentence in sentences]
    return sentence_lengths

try:
    with open("data.txt", "r") as file:
        contents = file.read()
        sentence_lengths = count_words_per_sentence(contents)
        
        plt.hist(sentence_lengths, bins=range(max(sentence_lengths) + 2), align='left', edgecolor='black')
        plt.xlabel('Number of Words in Sentence')
        plt.ylabel('Frequency')
        plt.title('Distribution of Words per Sentence in data.txt')
        plt.show()
        
        # Generate "Lorem Ipsum" sounding phrase
        generated_phrase = ""
        for _ in range(5):  # Generate 5
            sentence_length = random.choice(sentence_lengths)
            sentence = " ".join([generate_word(5, 't', 'h', letter_occurrences) for _ in range(sentence_length)])
            generated_phrase += sentence.capitalize() + ". "
        
        print("\nGenerated Lorem Ipsum-like Phrase:\n")
        print(generated_phrase)
        
except FileNotFoundError:
    print("The 'data.txt' file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

