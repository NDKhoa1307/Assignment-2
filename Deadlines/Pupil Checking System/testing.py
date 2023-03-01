class Students:
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

    def toString(self):
        print("Hello World")

if __name__ == '__main__':
    s1 = Students(1, "Hello World", 10, 10, 10, 10, 10)
    s1.toString()