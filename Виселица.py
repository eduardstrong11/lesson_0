import random

def hangman():
    words = ['настена', 'эдуард', 'морти', 'покемоны']
    word = random.choice(words)
    guesses = ''
    attempts = 55

    while attempts > 0:
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
        print()

        guess = input("Введите букву: ")
        guesses += guess

        if guess not in word:
            attempts -= 1

        if set(word) <= set(guesses):
            print("ВЫ ПОБЕДИЛИ!")
            break
        elif attempts == 0:
            print("ПРОИГРЫШ!", word)

hangman()