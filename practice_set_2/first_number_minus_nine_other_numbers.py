# prints the difference between the first number and the rest

#enter the first number
# use a for loop to get the value of the other 9 numbers
# for every loop, ask for an input and add it to a variable named 'total'(total has an initial value of zero)
# subtract total from the first number
# print the result

def difference_ten_numbers():
    total = 0
    counter = 9  # countdown, for auxillary purposes
    first_number = int(input('Input the first number as the minuend (10): ')) # to divide the other numbers to
    for _ in range(9):
        number = int(input(f'Input the rest as a subtrahend ({counter}): '))
        total += number
        counter -= 1 # countdown, for auxillary purposes
    return first_number - total
    
print(f'The first number minus the rest: {difference_ten_numbers()}')
