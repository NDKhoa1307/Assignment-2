#
#   Progress test 2
#   Done 3/1/2023
#   By Nguyen Dang Khoa -  DE180891
#

def number_of_lines(text: tuple) -> str:
    count_line = 0
    for _ in text:
        count_line += 1

    return (f"The number of lines are: {count_line}")

def print_words_less_than(text: tuple, characters: int):
    for word in text.read().split():
        if len(word) >= characters:
            print(word, end = ", ")

    print()

def count_occurence(text: tuple):
    occurence = {}
    for word in text.read().split():
        occurence[word] = occurence.get(word, 0) + 1

    for keys in occurence:
        print(f'{keys}: {occurence[keys]}')

def read_then_change(text: str) -> str:
    res = ""
    for x in text.split():
        if x == "ran":
            x = "run"
        res += (x + " ")

    return res

def main():
    #Read the file using the file name entered from the keyboard
    file_name = input("Please enter the file name:").strip()
    while True:
        try:
            text = open(file_name, 'r')
            break
        except FileNotFoundError:
            file_name = input("Your file does not exist, please re-enter:").strip()
            continue
    
    #Q1    
    print(number_of_lines(text))
    print()

    #Q2
    text = open(file_name, 'r')
    print("Words that are less than 4 characters are:", end = " ")
    print_words_less_than(text, 4)
    print()

    #Q3
    text = open(file_name, 'r')
    print("The occurence of all words are:")
    count_occurence(text)
    print()

    #Q4
    #Reading and then modifying the content of the file
    text = open(file_name, 'r')
    print("The output after changing is:")
    after_change = read_then_change(text.read())
    print(after_change)
    text.close()

    #Updating the content of the file
    text = open(file_name, 'w')
    text.writelines(after_change)


#Main program
if __name__ == '__main__':
    main()