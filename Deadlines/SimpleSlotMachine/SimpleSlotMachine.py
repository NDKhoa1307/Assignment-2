#   Simple Slot Machine - group 7
#   by
#   Nguyễn Đăng Khoa - DE180891
#   Nguyễn Hồ Nhật Huy - DE180760
#   Nguyễn Văn Nhật Nam - DE180887


import os
import random


from datetime import date
from datetime import datetime


date = date.today()
cur_time = datetime.now().strftime("%H:%M:%S")


def get_slot_machine_numbers():
    slot_machine_show = []
    duplicate = 1
    
    for i in range(0, 3):
        temp = random.randint(0, 9)
        
        if temp in slot_machine_show:
            duplicate += 1
        
        slot_machine_show.append(temp)

    return slot_machine_show, duplicate


def operate(money_remains):
    money_remains -= 0.25
    slot_machine_show, duplicate = get_slot_machine_numbers()
    
    print("The slot machine shows ", end = "")
    
    for x in slot_machine_show:
        print(x, end = "")
    
    if duplicate == 1:
        print("\nSorry, you don't win anything")
        return money_remains
    
    elif duplicate == 2:
        print("\nYou win 50 cents!")
        return money_remains + 0.50

    else:
        print("\nYou win the big prize, $1.00!")
        return money_remains + 1.00


def check_users_input(users_choice):
    while (users_choice) != "1" and (users_choice) != "2" and (users_choice) != "3":
        users_choice = (input("\nYour input is not valid, please re-enter:").strip())

    users_choice = int(users_choice)
    return int(users_choice)


def play_the_slot_machine():
    money_remains = float(10)
    
    os.system('cls')
    users_choice = 1
    print("You have $%0.2f"%money_remains)

    while users_choice != 3:
        print("Choose one of the following menu options:\n1) Play the slot machinie.\n2) Save game.\n3) Cash out.")
        users_choice = (input().strip())
        users_choice = check_users_input(users_choice)
        
        if money_remains == 0:
            os.system('cls')
            print("Your remains is no longer sufficient")
            break
    
        if users_choice == 1:
            money_remains = operate(money_remains)
            print("\nYou have $%0.2f"%money_remains)
        
        
        elif users_choice == 2:
            print("Your money had saved!")
            open('Users_Cash.txt', 'a').write(("{0}\t{1}\t%0.2f$\n" %float(money_remains)).format(date, cur_time))
            print("\n1) Play the slot machinie.\n2) Save game.\n3) Cash out.")
            
            users_choice = (input().strip())
            users_choice = check_users_input(users_choice)

    print("Thank you for playing! You end with $%0.2f" %float(money_remains))


if __name__ == '__main__':
    play_the_slot_machine()