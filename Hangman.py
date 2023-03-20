import os
import random as rd
#GROUP 07
#NGUYEN DANG KHOA 
#NGUYEN VAN NHAT NAM 
#NGUYEN HO NHAT HUY 





def print_user_UI(user_guesses, incorrect_guesses) -> str:
    print(f"You currently have {incorrect_guesses} incorrect guesses")
    print("Here is your puzzle:")
    for x in user_guesses:
        print(x, end=" ")
    print()
    user_guess = input("\nPlease enter your guess (type '1' to guess a single letter, '2' to guess the whole word): ").strip().upper()
    while user_guess not in ['1', '2']:
        user_guess = input("Please enter a valid guess (type '1' to guess a single letter, '2' to guess the whole word): ").strip().upper()
    return user_guess


def is_word_correct(word, user_guess):  
    if word == user_guess:
        return True
    elif len(word) != len(user_guess):
        return False
    else:
        for i in range(len(word)):
            if word[i] != user_guess[i]:
                return False
        return True


def play_the_game():
    enter_file = input("What file stores the puzzle words?:\n").strip()
    while True:
        try:
            words = open(enter_file, 'r')
            break
        except FileNotFoundError:
            enter_file = input("I'm sorry, but your input file does not exist or its format is not sufficient, please re-enter: ").strip()
    words = words.read().strip().split()
    wordsnew = []
    for i in words:
        i = i.upper()
        if i.isalpha():
            wordsnew.append(i)
    if not wordsnew:
        print("I'm sorry, but there are no valid puzzle words in the file. Please add some words and try again.")
        return
    word = wordsnew[rd.randint(0, len(wordsnew) - 1)]

    user_guesses = ['_'] * len(word)
    print("Your puzzle has", len(word), "words")
    incorrect_guesses = 0
    guessed_letters = []
    guessed_word = False

    while True:
        user_guess = print_user_UI(user_guesses, incorrect_guesses)

        if user_guess == '1':
            letter = input("Please enter a single letter: ").strip().upper()

            if letter in guessed_letters:
                print("Sorry, you have guessed that letter already.")
                incorrect_guesses += 1
            else:
                guessed_letters.append(letter)

                if letter in word:
                    print("Congratulations, you guessed a letter in the puzzle!")
                    for i in range(len(word)):
                        if word[i] == letter:
                            user_guesses[i] = letter
                else:
                    print("Sorry, that letter is NOT in the puzzle.")
                    incorrect_guesses += 1

        elif user_guess == '2':
            word_guess = input("Please enter the word you think is correct: ").strip().upper()
            
            if is_word_correct(word, word_guess):
                print(f"Congratulations! You got the correct word, {word}.")
                guessed_word = True
                break
            else:
                print("Sorry, that is not the correct word.")
                incorrect_guesses += 1
                if len(word)!=len(word_guess) :
                    print("word length does not match")
                else :
                  for i in range(len(word)):
                      if word[i] == word_guess[i]:
                         user_guesses[i] = word_guess[i]

        if '_' not in user_guesses and not guessed_word:
            print(f"Congratulations! You got the correct word, {word}.")
            break
        elif incorrect_guesses == 5:
            print(f"Sorry, you have made 5 incorrect guesses, you lose. The correct word was {word}.")
            break


def main():
    os.system('cls')
    play_game = input("Welcome to Hangman, do you wish to play the game? (yes/no): ").strip().lower()
    if play_game == 'yes':
        play_the_game()
    elif play_game == 'no':
        print("Thank you for stopping by, have a good day!")
    else:
        print("I'm sorry, but your input is not valid. Please enter either 'yes' for yes and 'no' for no.")

if __name__ == '__main__':
    main()
