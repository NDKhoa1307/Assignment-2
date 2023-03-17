import os
import random as rd

def print_user_UI(user_guesses, incorrect_guesses) -> str:
    print(f"You currently have {incorrect_guesses} incorrect guesses")
    print("Here is your puzzle:")
    for x in user_guesses:
        print(x, end=" ", )
    user_guess = input("\n""Please enter your guess: ").strip().upper()

    # Split the user's guess into individual letters
    guesses = []
    for letter in user_guess:
        if letter not in guesses:
            guesses.append(letter)
    user_guess = ''.join(guesses)

    return user_guess


def play_the_game():
    enter_file = input("What file stores the puzzle words?:\n").strip()
    while True:
        try:
            words = open(enter_file, 'r')
            break
        except FileNotFoundError:
            enter_file = input("I'm sorry, but your input file does not exist or its format is not sufficient, please re-enter: ").strip()
    words = words.read().strip().split()
    wordsnew=[]
    for i in words:
        i=i.upper()
        wordsnew.append(i)
    word = wordsnew[rd.randint(0, len(words) - 1)]


    user_guesses = ['_'] * len(word)
    print("Your puzzle has",len(word),"words")
    incorrect_guesses = 0
    guessed_letters = []

    while True:
     user_guess = print_user_UI(user_guesses, incorrect_guesses)

     # Loop over each letter in the user's guess
     for guess in user_guess:
        # Check if the user has already guessed the letter
        if guess in guessed_letters:
            print(f"Sorry, you have guessed '{guess}' already.")
            incorrect_guesses += 1
        else:
            guessed_letters.append(guess)
            # Check if the user's guess is in the word
            if guess in word:
                print(f"Congratulations, '{guess}' is in the puzzle!")
                for i in range(len(word)):
                    if word[i] == guess:
                        user_guesses[i] = guess
            else:
                print(f"Sorry, '{guess}' is NOT in the puzzle.")
                incorrect_guesses += 1

    # Check if the user has won or lost
     if '_' not in user_guesses:
        print(f"Congratulations! You got the correct word, '{word}'.")
        break
     elif incorrect_guesses == 5:
        print(f"Sorry, you have made 5 incorrect guesses, you lose. The correct word was '{word}'.")
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
