#
#  Program consist of all the required functions for the main program to work with
#

#Functions to convert from one numbering system to another
def convert_from_dec_to_bin(users_input):
    users_input = int(users_input)
    res = ""

    while users_input:
        res = str(users_input % 2) + res
        users_input //= 2

    return res

def convert_from_oct_to_bin(users_input):
    users_input = int(users_input)
    res = ""

    while users_input:
        temp = convert_from_dec_to_bin(users_input % 10)
        
        while len(temp) < 3:
            temp = "0" + temp
        
        res = temp + res    
        users_input //= 10
    
    return res   

def convert_from_hex_to_bin(users_input):
    users_input = str(users_input)
    res = ""
    users_input.upper()
    
    for x in users_input:
        if ord(x) >= 47 and ord(x) <= 57:
            temp = convert_from_dec_to_bin(int(x))
            while len(temp) < 4:
                temp = "0" + temp
            res += temp
        
        else:
            match x:
                case "A":
                    temp = convert_from_dec_to_bin(10)
                case "B":
                    temp = convert_from_dec_to_bin(11)
                case "C":
                    temp = convert_from_dec_to_bin(12)
                case "D":
                    temp = convert_from_dec_to_bin(13)
                case "E":
                    temp = convert_from_dec_to_bin(14)
                case "F":
                    temp = convert_from_dec_to_bin(15)
            while len(temp) < 4:
                temp = "0" + temp
            res += temp

    return res
        
def convert_from_bin_to_dec(users_input):
    users_input = int(users_input)
    res = 0
    step = 0
    while users_input:
        if users_input % 10:
            res += pow(2, step)
        
        step += 1    
        users_input //= 10

    return int(res)

def convert_from_bin_to_oct(users_input):
    res = ""
    users_input = str(users_input)
    
    while len(users_input) % 3 != 0:
        users_input = "0" + users_input
    
    for i in range(0, len(users_input), 3):
        temp = "" + users_input[i] + users_input[i + 1] + users_input[i + 2]
        res += str(convert_from_bin_to_dec(int(temp)))

    return int(res)

def convert_from_bin_to_hex(users_input):
    res = ""
    users_input = str(users_input)
    
    while len(users_input) % 4 != 0:
        users_input = "0" + users_input
    
    for i in range(0, len(users_input), 4):
        temp = "" + users_input[i] + users_input[i + 1] + users_input[i + 2] + users_input[i + 3]
        bin_to_dec = convert_from_bin_to_dec(temp)
        match bin_to_dec:
            case 10:
                bin_to_dec = "A"
            case 11:
                bin_to_dec = "B"
            case 12:
                bin_to_dec = "C"
            case 13:
                bin_to_dec = "D"
            case 14:
                bin_to_dec = "E"
            case 15:
                bin_to_dec = "F"
        
        res += str(bin_to_dec)

    return res

def convert_from_dec_to_oct(users_input):
    return convert_from_bin_to_oct(convert_from_dec_to_bin(users_input))

def convert_from_dec_to_hex(users_input):
    return convert_from_bin_to_hex(convert_from_dec_to_bin(users_input))

def convert_from_oct_to_dec(users_input):
    return convert_from_bin_to_dec(convert_from_oct_to_bin(users_input))

def convert_from_hex_to_dec(users_input):
    return convert_from_bin_to_dec(convert_from_hex_to_bin(users_input))

def convert_from_oct_to_hex(users_input):
    return convert_from_bin_to_hex(convert_from_oct_to_bin(users_input))

def convert_from_hex_to_oct(users_input):
    return convert_from_bin_to_oct(convert_from_hex_to_bin(users_input))


#Function to check whether the users input is valid for the program to run
def check_input_numbering_system(input_numbering_system, users_input):
    if (input_numbering_system != "bin") and (input_numbering_system !=  "dec") and (input_numbering_system != "oct") and (input_numbering_system != "hex"):
        return True
    
    #check the input format, then see whether the users input is suitable for the format chosen; if yes, return True; return False otherwise
    if input_numbering_system == "bin":
        for x in users_input:
            if x != "1" and x != "0":
                return True
        return False

    elif input_numbering_system == "dec":
        check_map = {
            "0" : 0,
            "1" : 0,
            "2" : 0,
            "3" : 0,
            "4" : 0,
            "5" : 0,
            "6" : 0,
            "7" : 0,
            "8" : 0,
            "9" : 0,
        }
        
        try:
            for x in users_input:
                check_map[x] += 1
        except KeyError:
            return True
        
        return False

    elif input_numbering_system == "oct":
        check_map = {
            "0" : 0,
            "1" : 0,
            "2" : 0,
            "3" : 0,
            "4" : 0,
            "5" : 0,
            "6" : 0,
            "7" : 0
        }
        
        try:
            for x in users_input:
                check_map[x] += 1
        except KeyError:
            return True
        
        return False

    else:
        check_map = {
            "0" : 0,
            "1" : 0,
            "2" : 0,
            "3" : 0,
            "4" : 0,
            "5" : 0,
            "6" : 0,
            "7" : 0,
            "8" : 0,
            "9" : 0,
            "A" : 0,
            "B" : 0,
            "C" : 0,
            "D" : 0,
            "E" : 0,
            "F" : 0
        }

        try:
            for x in str(users_input).upper():
                check_map[x] += 1
        except KeyError:
            return True
        
        return False


#Function to convert the users input from the input numbering system to the output numbering system
def convert_from_input_to_output(input_numbering_system, users_input, output_numbering_system):
    if input_numbering_system == "bin":
        if output_numbering_system == "bin":
            return users_input
        elif output_numbering_system == "dec":
            return convert_from_bin_to_dec(users_input)
        elif output_numbering_system == "oct":
            return convert_from_bin_to_oct(users_input)
        else:
            return convert_from_bin_to_hex(users_input)

    elif input_numbering_system == "dec":
        if output_numbering_system == "bin":
            return convert_from_dec_to_bin(users_input)
        elif output_numbering_system == "dec":
            return users_input
        elif output_numbering_system == "oct":
            return convert_from_dec_to_oct(users_input)
        else:
            return convert_from_dec_to_hex(users_input)

    elif input_numbering_system == "oct":
        if output_numbering_system == "bin":
            return convert_from_oct_to_bin(users_input)
        elif output_numbering_system == "dec":
            return convert_from_oct_to_dec(users_input)
        elif output_numbering_system == "oct":
            return users_input
        else:
            return convert_from_oct_to_hex(users_input)

    else:
        if output_numbering_system == "bin":
            return convert_from_hex_to_bin(users_input)
        elif output_numbering_system == "dec":
            return convert_from_hex_to_dec(users_input)
        elif output_numbering_system == "oct":
            return convert_from_hex_to_oct(users_input)
        else:
            return users_input


#Function to return the full name of the numbering systems
def print_name_of_numbering_system(numbering_system):
    if numbering_system == "bin":
        return "Binary"
    elif numbering_system == "dec":
        return "Decimal"
    elif numbering_system == "oct":
        return "Octal"
    else:
        return "Hexadecimal"

#Function to convert the input into readable format for the program
def change_into_readable_format(numbering_system):
    if numbering_system == "binary":
        return "bin"
    elif numbering_system == "decimal":
        return "dec"
    elif numbering_system == "octal":
        return "oct"
    elif numbering_system == "hexadecimal":
        return "hex"
    else:
        return numbering_system

