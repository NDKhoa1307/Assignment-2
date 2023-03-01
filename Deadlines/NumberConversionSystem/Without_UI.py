#
#  Numbering conversion system program with VSC intergrated UI
#  Status: Completed
#


import os
from Functions import *

#Main program
if __name__ == '__main__':
    #Initialize the input format for users input
    os.system('cls')

    #Initialize the input numbering system as well as the users input 
    input_numbering_system = input("Convert from(bin, dec, oct or hex):").strip().lower()
    input_numbering_system = change_into_readable_format(input_numbering_system)
    users_input = input("Enter your number:".format(input_numbering_system)).strip()

    #Check and make the user re-enter if their input is not valid until their input is
    while check_input_numbering_system(input_numbering_system, users_input):
        os.system('cls')
        input_numbering_system = input("Your input is not valid, please re-enter\nConvert from(bin, dec, oct or hex):").strip().lower() 
        users_input = input("Enter {} number:".format(input_numbering_system)).strip()
    
    #Initialize the output numbering system
    output_numbering_system = input("\nConvert to(bin, dec, oct, hex):").strip().lower()
    output_numbering_system = change_into_readable_format(output_numbering_system)

    #Check and make the user re-enter if their input is not valid until their input is
    while True:
        os.system('cls')
        print("Input numbering system: {0}\nEntered input:{1}".format(input_numbering_system, users_input))
        if (output_numbering_system == "bin") or (output_numbering_system == "dec") or (output_numbering_system ==  "oct") or (output_numbering_system == "hex"):
            break
        else:
            output_numbering_system = input("\nYour input is not valid, please re-enter\nConvert to(bin, dec, oct or hex):").strip().lower()

    #Print the result onto the screen
    os.system('cls')
    print("From {0} to {1}".format(print_name_of_numbering_system(input_numbering_system), print_name_of_numbering_system(output_numbering_system)))
    print("Entered {0} number: {1}".format(input_numbering_system, users_input))
    print("{0} number: {1}\n".format(print_name_of_numbering_system(output_numbering_system), convert_from_input_to_output(input_numbering_system, users_input, output_numbering_system)))