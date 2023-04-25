# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 4 - Problem 1
# This program reads a text file that contains a set of numbers. 
# Then, the even and odd numbers will be extracted from the text file and will be transferred to separate files.

import time
import pyfiglet
from colorama import Fore, Style

def user_input():
    # open numbers.txt (write)
    with open("numbers.txt", 'w') as input_file1:   
        print()
        print("INSTRUCTION: Please enter whole numbers only. Type any letter or symbol to stop. \n")     

        while True:
            try:
                # the user will input numbers
                user_input = int(input("\tEnter a number: "))

                # user should only input whole numbers
                if user_input >= 0:
                    # user input will be written to numbers.txt
                    input_file1.write(str(user_input) + '\n')
                    continue
            except:
                # If the user any letter to stop the program
                print("\n\tExtracting odd and even numbers....")
                time.sleep(3)
                break


def main():
# open numbers.txt (read), even.txt(write), odd.txt(write)
    with open("numbers.txt", 'r') as input_file2, open("even.txt", 'w+',) as output_even,  open("odd.txt", 'w') as output_odd:

        # read numbers.txt line by line
        for line in input_file2:  
            # convert each line from numbers.txt into integer
            extracted_number = int(line)

            # if the extracted number is even
            if extracted_number % 2 == 0:  
                # even numbers will be written to even.txt
                output_even.write(str(extracted_number)+ "\n")

            # else if the extracted number is odd
            if extracted_number % 2 == 1:
                # odd numbers will be written to odd.txt
                output_odd.write(str(extracted_number)+ "\n")

def display():
    with open("numbers.txt", 'r') as input_file3, open("even.txt", 'r',) as output_even2,  open("odd.txt", 'r') as output_odd2:
            # print list of numbers from numbers.txt
            lst_numbers = [int(line) for line in input_file3.read().split()]
            lst_numbers.sort()
            print("\n\tNumbers: ", lst_numbers)

            # print list of even numbers
            lst_even = [int(line) for line in output_even2.read().split()]
            lst_even.sort()
            print("\tEven Numbers: ", lst_even)
            
            # print list of odd numbers
            lst_odd = [int(line) for line in output_odd2.read().split()]
            lst_odd.sort()
            print("\tOdd Numbers: ", lst_odd, "\n")

# start
user_input()
main()
display()



                
        

        

        
