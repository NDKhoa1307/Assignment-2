import os
import random as rd

def print_user_UI(user_guesses, incorrect_guesses) -> str:
    print(f"You currently have {incorrect_guesses} incorrect guesses")
    print("Here is your puzzle:")
    for x in user_guesses:
        print(x, end = "")
    user_guess = input("Please enter your guess").strip()
    return user_guess


def play_the_game():
    enter_file = input("What file stores the puzzle words?:\n").strip()
    while True:
        try:
            words = open(enter_file, 'r')
            break
        except FileNotFoundError:
            enter_file = input("I'm sorry, but your input file does not exsist or it's format is not sufficient, please re-enter:").strip()
            continue

    words = words.read().strip().split()
    word = words[rd.randint(0, len(words) - 1)]

    user_guesses = ['_'] * len(word)
    pass

#Main function
def main():
    os.system('cls')
    play_game = input("Welcome to Hangman, do you wish to play the game ?(yes/no):").strip().lower()
    if not (play_game == 'no' or play_game == 'yes'):
        while True:
            play_game = input("I'm sorry, but your input is not valid, please re-enter(Only enter either 'yes' for yes and 'no' for no):").strip()
            if play_game == 'no' or play_game == 'yes':
                break
                
    if play_game == 'yes':
        play_the_game()
        
    os.system('cls')
    print("Thank you for stopping by, have a good day!")
    pass

def hello():
    print("Hello World")
    
#Main program
if __name__ == '__main__':
    main()
    pass
