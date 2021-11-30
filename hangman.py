import os
import time

word = "hello"
no_letters_guessed = 0
guess_count = 0
guessed_before = False


def create_secret_word(word):
    target_score = 0
    place = 0
    word_guessed ={}
    secret_word = {}
    for character in word:
        target_score = target_score + 1
        word_guessed[str(place)]='-'
        secret_word[str(place)]=character
        place = place + 1
    return word_guessed, secret_word, target_score


def check_not_guessed_before(word_guessed, guessed_letter, target_score):
    guessed_before_count = 0
    guessed_before = False
    place = 0
    while place < target_score:
        if word_guessed[str(place)]== guessed_letter :
            #print('You have already guessed that!')
            guessed_before_count = guessed_before_count + 1
        place = place +1
    if guessed_before_count > 0:
        guessed_before = True
    return guessed_before


def check_correct(word_guessed, secret_word, guessed_letter, target_score, no_letters_guessed):
    place = 0
    while place < target_score:
        if secret_word[str(place)]== guessed_letter :
            word_guessed[str(place)]=guessed_letter
            no_letters_guessed = no_letters_guessed + 1
        place = place +1
    return no_letters_guessed


def print_word_guessed(word_guessed, no_letters_guessed, guess_count,target_score):
    place = 0
    guess_so_far = ""
    clear = lambda:os.system('cls')
    clear()
    print("GUESS THE WORD!")
    while place < target_score:
        guess_so_far = guess_so_far + word_guessed.get(str(place))  + " "
        place = place + 1
    print()
    print(guess_so_far)
    print()

    print("Letters Guessed: "+ str(no_letters_guessed))
    print("Guesses Available: " + str((2*target_score)-guess_count))
    print()
    guessed_letter = input("Please guess a letter: ")
    print()
    guess_count = guess_count + 1
    return guessed_letter, guess_count



#set up dictionary of word guessed and secret word to compare 
(word_guessed, secret_word, target_score) = create_secret_word(word)


while no_letters_guessed != target_score:
    #Display progress and get a guessed letter
    guessed_letter,guess_count = print_word_guessed(word_guessed, no_letters_guessed, guess_count, target_score)
    #check not guessed before
    guessed_before = check_not_guessed_before(word_guessed, guessed_letter, target_score)

    #update the word_guessed
    if guessed_before == False:
        no_letters_guessed = check_correct(word_guessed, secret_word, guessed_letter, target_score, no_letters_guessed)
        guessed_before = True
    else:
        print()
        print('You have already guessed that!')
        time.sleep(1)
     
    if ((2*target_score)-guess_count) == 0:
        clear = lambda:os.system('cls')
        clear()
        print("Bad Luck Sunshine!")
        print("Try again another time.")
        break

if no_letters_guessed == target_score:
    clear = lambda:os.system('cls')
    clear()
    print('Well done! You guessed the password!: ' + word)
    




