file_input = input("Input file:").strip()
while True:
    try:
        the_file = open(file_input)
        break
    except FileNotFoundError:
        file_input = input("Cannot find file, please re-enter file:").strip()
        continue

for line in the_file:
    print(line)