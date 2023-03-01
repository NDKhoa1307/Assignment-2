file_input = input("Input file:").strip()
while True:
    try:
        the_file = open(file_input)
        break
    except FileNotFoundError:
        file_input = input("Cannot find file, please re-enter file:").strip()
        continue

print(the_file.read())