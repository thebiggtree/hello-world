import random

words_file = 'hangman_words.txt'

try:
    f = open(words_file)
    words = f.read().splitlines()
    f.close
except IOError:
    print("Cannot find file: " + words_file)
    exit()
    
#words = ['chicken', 'dog', 'cat', 'mouse', 'frog','moose', 'Nick', 'Rasberry Pi']
lives_remaining = 14
guessed_letters = ''

def pick_a_word():
    return random.choice(words)

def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print('Yay!! You guessed -- ' + guess)
            print('You win! Possum Toss!!!')
            break
        if lives_remaining == 0:
            print('They said you was Hung!')
            print('They was right!')
            print('The word was ' + word)
            break


def get_guess(word):
    print_word_with_blanks(word)
    print('Lives Remaining: ' + str(lives_remaining))
    guess = input(' Guess a letter or whole word?')
    return guess

def process_guess(guess, word):
    if len(guess) > 1:
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)
    
    
def single_letter_guess(guess, word):
    global lives_remaining
    global guessed_letters
    if word.find(guess) == -1:
        lives_remaining = lives_remaining - 1
        
    guessed_letters = guessed_letters + guess
    if all_letters_guessed(word):
        return True

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter) == -1:
            return False
    return True

def whole_word_guess(guess, word):
    global lives_remaining
    if guess.lower() == word.lower():
        return True
    else:
        lives_remaining = lives_remaining - 1
        return False

def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            #letter found
            display_word = display_word + letter
        else:
            #letter not found
            display_word = display_word + '-'
    print (display_word)
    
play()
