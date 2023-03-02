import os
from random import randint
import time

player_guesses=[]
player_name=[]
player_range=[]
player_attempt=[]

def check_enough(player_name,player_guesses,player_range,player_attempt):
    if len(player_name) == 10:
        player_guesses.pop()
        player_name.pop()
        player_range.pop()
        player_attempt.pop()

def show_score():
    check_enough(player_name,player_guesses,player_range,player_attempt)
    cls()
    print("\n                           LEADERBOARD")
    print("\n   Name                   Attempt            Range            Guesses")
    if(len(player_name)==len(player_attempt)==len(player_guesses)==len(player_range)):
        for x in range(len(player_name)):
            print("   {}                  ".format(player_name[x]),end="")
            print("    {}             ".format(player_attempt[x]),end="")
            print("    {}           ".format(player_range[x]),end="")
            print("    {}".format(player_guesses[x]),end="\n")
    else:
        return

def cls():
    os.system('cls')

def tell_time():
    if time.localtime().tm_hour>=19:
        return "evening"
    
    elif time.localtime().tm_hour<=19 and time.localtime().tm_hour>12:
        return "afternoon"
   
    else:
        return "morning"


def play_the_game(users_input_range,users_input_guesses):
    guesses=users_input_guesses
    random_number=randint(1,users_input_range)
    print("You have {} guesses left".format(users_input_guesses))
    while True:
        try:
            print("You can press stop to stop playing")
            users_guess=input("Please pick a number from 1 to %d:"%users_input_range)    
            if users_guess.lower()=="stop":
                cls()
                player_guesses.insert(1,"GIVE UP")
                print("GAME OVER!")
                return

            if int(users_guess)<1 or int(users_guess)>users_input_range:
                raise ValueError("Please guess the correct value in the range")
            
            if int(users_guess)>random_number:
                cls()
                guesses-=1
                print("{} is higher than the generated number".format(users_guess))
                print("You have {} guesses left".format(guesses))
                print("The answer is between 1 and {}".format(users_input_range))
            
            elif int(users_guess)<random_number:
                cls()
                guesses-=1
                print("{} is lower than the generated number".format(users_guess))
                print("You have {} guesses left".format(guesses))
                print("The answer is between 1 and {}".format(users_input_range))
            
            else:
                cls()
                print("Congrats, {} is the number!!".format(random_number))
                player_attempt.insert(1,guesses)
                return
            
            if guesses==0:
                cls()
                player_attempt.insert(1,"LOSE")
                print("GAME OVER!")
                return
        except ValueError as err:
            print("Oh no, that is not a valid value, please try again...")
            print("({})\n".format(err))
    
def check_users_name(users_name):
    if len(users_name)!=3:
        return False
    return True

def start_game():
    wanna_play=input("Good {} ".format(tell_time())+"travellers, would you love to play the game? (Enter Yes/No) ")
    while wanna_play.strip().lower()=="yes":
        users_name=input("Please enter your name (Please only type in three letters):")
        while check_users_name(users_name)==0:
            users_name=input("Please enter your name again (Please only type in three letters):")
        player_name.insert(1,users_name)
        try:
            users_input_range=int(input("Please pick a range:"))
            player_range.insert(1,users_input_range)
            users_input_guesses=int(input("Please pick the amount of guesses:"))
            player_guesses.insert(1,users_input_guesses)
            cls()
            play_the_game(users_input_range,users_input_guesses)
            wanna_play=input("\nDo you wish to play another game? (Enter Yes/No) ")
        except ValueError as error:
            cls()
            print("Oh no, that is not a valid value,please try again...")
            print("({})\n".format(error))
    else:
        cls()
        print("That's cool, have a good one!")
        leaderboard=input("Do you wish to view the leaderboard? (Enter Yes/No)")
        if leaderboard.lower()=="yes":
            show_score()

if __name__ == '__main__':
    start_game()