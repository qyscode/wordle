import random
import string
import csv

all_words = []
all_words_full = []
all_letters = list(string.ascii_letters)

available_letters = all_letters[:26]

with open('5_letters.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    for row in csv_reader:
        # Append each row to the list
        all_words.append(row)

for word in all_words:
    current_word = ''
    for letter in word:
        current_word += letter
    all_words_full.append(current_word)

mystery_word = random.choice(all_words_full)
possible_characters = []
correct_letters = []

for letter in mystery_word:
    possible_characters.append(letter)

try_counter = 1

solved = False

def check_if_valid(word):
    
    if attempt.lower() not in all_words_full:
        print('Not a valid word! Try again...')
        return False

    else:
        return True 

while not solved and try_counter < 7:

    output = ''
    while True:
        attempt = input('Your Word: ')
        if check_if_valid(attempt):
            break

    for i in range(5):
        if attempt[i] == mystery_word[i]:
            output += attempt[i].upper()

        else:
            output += attempt[i].lower()
            if attempt[i].lower() in available_letters:
                available_letters.remove(attempt[i].lower())

        if attempt[i] in possible_characters:
            if attempt[i] in correct_letters:
                pass
            
            else:
                correct_letters.append(attempt[i])
        
    print('Attempt N0.' + str(try_counter))
    print('---------')
    print(output)
    print('---------')
    print('Correct Letters: ')
    print(correct_letters)
    print('---------')
    print('Available Letters: ') 
    print(available_letters)
    print('---------')
    print('*********')

    if attempt.lower() == mystery_word.lower():
        solved = True 
        print('You Win!!!!!')

    try_counter += 1 

if not solved:
    print('You Lose :(')
    print('Myster Word is ' + mystery_word)
        
    print("██████                        ██████    ")
    print("██████████  ████████████████  ██████████")
    print("█████████████              ██████████████")
    print("████████                          ███████")
    print("██████                              █████")
    print("  ██                                  ██  ")
    print("  ██                                  ██  ")
    print("██        ██████            ██████        ██")
    print("██      ██████████        ██████████      ██")
    print("██    ████████  ██        ██  ████████    ██")
    print("██    ████████  ██        ██  ████████    ██")
    print("██    ██████████            ██████████    ██")
    print("██      ██████      ████      ██████      ██")
    print("  ██                ████                ██  ")
    print("  ████████  ▒▒▒▒▒▒        ▒▒▒▒▒▒  ████████  ")
    print("███████████▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒████████████")
    print("██████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████")
    print("██████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████")
    print("██████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████")
    print("  ████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████  ")
    print("    ████████  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ████████  ")
    print("                ▒▒▒▒▒▒▒▒▒▒▒▒                ")
    print("                  ▒▒▒▒▒▒▒▒                  ")
    print("                    ▒▒▒▒                    ")
        