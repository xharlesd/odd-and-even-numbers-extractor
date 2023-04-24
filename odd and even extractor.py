# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 4 - Problem 1
# This program reads a text file that contains a set of numbers. 
# Then, the even and odd numbers will be extracted from the text file and will be transferred to separate files.

# open numbers.txt (read), even.txt(write), odd.txt(write)
with open("numbers.txt", 'r') as input_file, open("even.txt", 'w') as output_even,  open("odd.txt", 'w') as output_odd:
    
    for line in input_file:  # read numbers.txt line by line
        extracted_number = int(line)  #  convert each line from numbers.txt into integer

        if extracted_number % 2 == 0:  #  if the extracted no. is even

            """
            # write to even.txt
        #  if odd,
            #  write to odd.txt
            """ 