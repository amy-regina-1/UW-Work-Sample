# The purpose of this program is to provide possible solutions for Wordle.
# Users can enter known letters and positions, known letters with unknown positions,
# and known wrong letters to generate a list of possible solutions. 


import json
import typing


def read_words():
    with open('words_dictionary.json') as fp:
        return list(json.load(fp).keys())

def filter_words_with_length(all_words, length):
    valid_words = []
    for word in all_words:
        if length == len(word):
            valid_words.append(word)        
    return valid_words

def filter_words_with_letter(all_words, letter):
    valid_words = []
    for word in all_words:
        if letter in word:
            valid_words.append(word)
    return valid_words

def get_position_of_letter_in_word(word, letter):
    positions = []
    for position, character in enumerate(word):
        if character == letter:
            positions.append(position)
    return positions  
 

def filter_words_with_known_wrong_position(words, position: dict):
    valid_words = []
    for word in words:
        is_valid = True
        for l, ps in position.items():
            for p in ps:
                if p == word.find(l):
                    is_valid = False
                    break
        if is_valid:
            valid_words.append(word)
    return valid_words
  

def get_wrong_letters(letters):
    wrong_letters = list(letters)
    return set(wrong_letters)

def filter_words_without_known_wrong_letters(words, letters):
    valid_words = []
    for word in words:
        is_valid = True
        for letter in letters:
            if letter in word:
                is_valid = False
                break
        if is_valid:
            valid_words.append(word)
    return valid_words

def get_letter_count(letters):
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def filter_words_by_letter_count(words, position: dict):
    valid_words = []
    for word in words:
        word_letter_count = get_letter_count(word)
        is_valid = True
        for l, ps in position.items():
            if l not in word_letter_count:
                is_valid = False
                break
            letter_frequency = word_letter_count[l]
            if len(ps) > letter_frequency:
                is_valid = False
                break
        if is_valid:
            valid_words.append(word)
    return valid_words

def get_letter_position(letters: str):
    letter_position: typing.Dict[str, typing.List[int]] = {}
    for position, letter in enumerate(letters):
        if letter == "?":
            continue
        if letter in letter_position:
            letter_position[letter].append(position)
        else:
            letter_position[letter] = [position]
    return letter_position

def filter_words_by_letter_position(words, position: dict):
    valid_words = []
    for word in words:
        is_valid = True
        for l, ps in position.items():
            if l not in word:
                is_valid = False
                break
            for p in ps:
                if p != word.find(l):
                    is_valid = False
                    break
        if is_valid:
            valid_words.append(word)
    return valid_words


words = read_words()
words_length_five = filter_words_with_length(words, 5)
result = words_length_five


known_letters = input("Enter letters using the following format: \n????? (known letters and position), ????? (known letters but unknown position), abc (wrong letters). \nFor example: f??e?, ?s???, pln\nEnter letters: ")


separated_input = [x.strip() for x in known_letters.split(",")]
if len(separated_input) != 3:
    exit("Enter letters using this format: ?????, ?????, xyz")
if len(separated_input[0]) != 5:
    exit("Enter 5 letters. For unknown letters, enter ?")
if len(separated_input[1]) >5:
    exit("Enter 5 letters or less.")


#letter_count = get_letter_count(separated_input[1])
letter_position = get_letter_position(separated_input[0])
wrong_letters = get_wrong_letters(separated_input[2])
known_letters_wrong_position = get_letter_position(separated_input[1])
result = filter_words_by_letter_count(words_length_five, known_letters_wrong_position)
result = filter_words_without_known_wrong_letters(result, wrong_letters)
result = filter_words_by_letter_position(result, letter_position)
result = filter_words_with_known_wrong_position(result, known_letters_wrong_position)

if len(result) == 0:
    exit("No results found.")


print(result)