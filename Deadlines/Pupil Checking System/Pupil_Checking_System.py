import os

class Pupil:
    def __init__(self, roll_number: int, name : str, English : int, Maths: int, Physics: int, Chemistry : int, CS : int):
        self.roll_number = roll_number
        self.name = name
        self.English = English
        self.Maths = Maths
        self.Physics = Physics
        self.Chemistry = Chemistry
        self.CS = CS

    def set_Name(self, name : str):
        self.name = name
    def get_Name(self) -> str:
        return self.name
    
    def set_English(self, English: int):
        self.English = English
    def get_English(self) -> int:
        return self.English
    
    def set_Maths(self, Maths: int):
        self.Maths = Maths
    def get_Maths(self) -> int:
        return self.Maths
    
    def set_Physics(self, Physics: int):
        self.Physics = Physics
    def get_Physics(self) -> int:
        return self.Physics
    
    def set_Chemistry(self, Chemistry: int):
        self.Chemistry = Chemistry
    def get_Chemistry(self) -> int:
        return self.Chemistry
    
    def set_CS(self, CS: int):
        self.CS = CS
    def get_CS(self) -> int:
        return self.CS

    def set_Marks(self, English: int, Maths: int, Physics: int, Chemistry: int, CS: int):
        self.English = English
        self.Maths = Maths
        self.Physics = Physics
        self.Chemistry = Chemistry
        self.CS = CS

def check_user_input(user_choice, n) -> int:
    try:
        user_choice = int(user_choice)
        if user_choice <= n:
            return user_choice
        else:
            raise ValueError
    except ValueError:
        while True:
            try:
                user_choice = int(input(f'Your input is not valid, please re-enter your choice (1- {n}): ').strip())
                if user_choice <= n:
                    return user_choice
            except:
                user_choice = input(f'Your input is not valid, please re-enter your choice (1- {n}): ').strip()
                if user_choice.isdigit():
                    user_choice = int(user_choice)
                    if user_choice <= n:
                        return user_choice

def create_pupil_record(Students):
    
    return Students


def display_main_menu() -> int:
    print("MAIN MENU\n1. REPORT MENU\n2. ADMIN MENU\n3. EXIT")
    user_choice = input(f"Enter choice(1-3): ").strip()
    return check_user_input(user_choice, 3)

def display_report_menu(Students) -> int:
    print("REPORT MENU\n1. CLASS RESULT\n2. PUPIL REPORT CARD\n3. BACK TO MAIN MENU")
    user_choice = input(f'Enter choice(1-3): ').strip()
    return check_user_input(user_choice, 3)

def display_admin_menu(Students) -> int:
    print("ADMIN MENU\n1. CREATE PUPIL RECORD\n2. DISPLAY ALL PUPIL RECORDS\n3. SEARCH PUPIL RECORD\n4. MODIFY PUPIL RECORD\n5. DELETE PUPIL RECORD\n6. BACK TO MAIN MENU")
    user_choice = input(f'Enter choice(1-6): ').strip()
    user_choice = check_user_input(user_choice, 6)

def main():
    os.system('cls')
    user_choice = display_main_menu()
    Students = []
    if user_choice == 1:
        display_report_menu(Students)
    elif user_choice == 2:
        display_admin_menu(Students)
    else:
        os.system('cls')
        print("Have a nice day")
        return

if __name__ == '__main__':
    main()
    pass