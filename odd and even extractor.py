# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 4 - Problem 1
# This program reads a text file that contains a set of numbers. 
# Then, the even and odd numbers will be extracted from the text file and will be transferred to separate files.

# open numbers.txt (read), even.txt(write), odd.txt(write)
with open("numbers.txt", 'r') as input_file, open("even.txt", 'w') as _file2,  open("odd.txt", 'w') as my_file3:
    """
    # read numbers.txt line by line
    #  each line
    #  if even,
        # write to even.txt
    #  if odd,
        #  write to odd.txt
    """
