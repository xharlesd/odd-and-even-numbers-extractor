# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 4 - Problem 1
# This program reads a text file that contains a set of numbers. 
# Then, the even and odd numbers will be extracted from the text file and will be transferred to separate files.

import time
import pyfiglet
from colorama import Fore, Style

def intro():
    # Use pyfiglet formatting to Assignment # 4"
    print("")
    lab = pyfiglet.figlet_format("ODD & EVEN NO.", font = "banner3-d", width = 130, justify = "center")
    print(Style.BRIGHT + Fore.CYAN + lab)

    # format introductory message
    print("\033[0;34m" + "\033[1m-" * 130 + '\033[0m')
    intro = "INSTRUCTION: PLEASE INPUT WHOLE NUMBERS ONLY. TYPE ANY LETTER OR SYMBOL TO STOP." 
    intro_centered = intro.center(130)
    print( "\033[1m" + intro_centered) 
    print("\033[0;34m" + "\033[1m-" * 130 + '\033[0m' + "\n")

    # insert time delay
    time.sleep(1.5)


def user_input():
    # open numbers.txt (write)
    with open("numbers.txt", 'w') as input_file1:   

        while True:
            try:
                # the user will input numbers
                user_input = int(input(Fore.CYAN + "\033[1m\t\t\tEnter a Number:  \033[0m"  + Fore.YELLOW))

                # user should only input whole numbers
                if user_input >= 0:
                    # user input will be written to numbers.txt
                    input_file1.write(str(user_input) + '\n')
                    continue

            except:
                # If the user any letter to stop the program
                print(Fore.GREEN + "\n\t\t\t[Extracting odd and even numbers.........]")
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
            print(Fore.YELLOW + "\033[1m\n\n\t\t\tNUMBERS:       \033[0m" + Fore.CYAN, lst_numbers)

            # print list of even numbers
            lst_even = [int(line) for line in output_even2.read().split()]
            lst_even.sort()
            print(Fore.YELLOW + "\033[1m\t\t\tEVEN NUMBERS:  \033[0m" + Fore.CYAN, lst_even)
            
            # print list of odd numbers
            lst_odd = [int(line) for line in output_odd2.read().split()]
            lst_odd.sort()
            print(Fore.YELLOW + "\033[1m\t\t\tODD NUMBERS:   \033[0m" + Fore.CYAN, lst_odd, "\n")

def outro():
    time.sleep(3.5)
    print(Fore.GREEN + "\n\t\t\t[Program will be terminated..............] \n")
    time.sleep(2)
    
    print("\033[0;34m" + "\033[1m-" * 130 + '\033[0m')
    print(" ")
    lab = pyfiglet.figlet_format("   THANK YOU!   ", font = "banner3",  width = 130, justify = "center")
    print(Style.BRIGHT + Fore.CYAN + lab)
    exit()


# start
intro()
user_input()
main()
display()
outro()




                
        

        

        
