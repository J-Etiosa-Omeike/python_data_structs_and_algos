import math

# iterative method: divide integer by two repeatedly until it's less than 2 
def number_of_times1(integer):
    count = 0

    while integer >= 2:
        integer = integer / 2
        count += 1
    
    return count

print(number_of_times1(10))

# math method: log_2 tells you the number of time you can divide a number by 2 before getting to 1. round this down to get an int and you get one line of code 
def number_of_times2(integer):

    return math.floor(math.log2(integer))


print(number_of_times2(10))


