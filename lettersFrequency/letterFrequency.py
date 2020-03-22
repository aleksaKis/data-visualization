import json

english_alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
with open('WebstersEnglishDictionary/dictionary_compact.json') as f:
    data = json.load(f)

# Get list of all words in English dictionary.
words_list = list(data.keys())
# Convert list to a string of words.
words = ' '.join(words_list)


# Function for letter count in each word.
def letter_counter(letter):
    counter = 0
    for i in words:
        if i == letter:
            counter += 1
    return counter


# Create an empty dictionary
dictionary = {}

# Loop for counting all letters
for l in english_alphabet:
    dictionary[l] = letter_counter(l)


# Export Dictionary
def get_dictionary():
    return dictionary
