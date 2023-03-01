def number_of_lines(text: tuple) -> str:
    count_line = 0
    for _ in text:
        count_line += 1

    return (f"The number of lines are: {count_line}")

def print_words_less_than(text: tuple, characters: int):
    for x in text.read().split():
        if len(x) >= characters:
            print(x, end = " ")

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

    #Q2
    text = open(file_name, 'r')
    print_words_less_than(text, 4)

if __name__ == '__main__':
    main()