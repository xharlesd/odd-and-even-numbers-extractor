# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 4 - Problem 1
# This program reads a text file that contains a set of numbers. 
# Then, the even and odd numbers will be extracted from the text file and will be transferred to separate files.

def user_input():
    # open numbers.txt (write)
    with open("numbers.txt", 'w') as input_file1:        
        while True:
            # the user will input numbers
            user_input = input("Input number: ")

            # if user input is a number

            # user input will be written to numbers.txt
            input_file1.write(user_input)

            # if user input is not a number

def main():
# open numbers.txt (read), even.txt(write), odd.txt(write)
    with open("numbers.txt", 'r') as input_file2, open("even.txt", 'w+') as output_even,  open("odd.txt", 'w') as output_odd:

        # read numbers.txt line by line
        for line in input_file2:  
            # convert each line from numbers.txt into integer
            extracted_number = int(line) 

            # if the extracted number is even
            if extracted_number % 2 == 0:  
                    
                # even numbers will be written to even.txt
                output_even.write(str(extracted_number)+ "\n")

            # else if the extracted number is odd
            elif extracted_number % 2 == 1: 

                # odd numbers will be written to odd.txt
                output_odd.write(str(extracted_number)+ "\n")

# start
user_input()
main()




                
        

        

        
