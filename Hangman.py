import os

def play_the_game():
    print("Hello World")
    pass

def main():
    print("Hello World")
    pass

#Main function
def main():
    os.system('cls')
    play_game = input("Welcome to Hangman, do you wish to play the game ?(y/n):").strip()
    if not (play_game == 'n' or play_game == 'y'):
        while True:
            play_game = input("I'm sorry, but your input is not valid, please re-enter(Only enter either 'y' for yes and 'n' for no):").strip()
            if play_game == 'n' or play_game == 'y':
                break
                
    if play_game == 'y':
        play_the_game()
    os.system('cls')
    print("Thank you for stopping by, have a good day!")
    pass


#Main program
if __name__ == '__main__':
    main()
