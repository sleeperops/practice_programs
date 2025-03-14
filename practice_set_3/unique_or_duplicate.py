# checks if the number is unique or a duplicate
# initialize a list called input_list
# run a while loop as long as it true
# for every loop, ask the user for an input
# try if the input can be converted to an integer
# > if so, check if the number is already in the number list
# > if it is, print 'duplicate', else, print 'unique'
# > add the number to the input_numbers list
# else if it is not an integer print 'not a number' and break from the loop

input_numbers = []
while True:
    try:
        user_input = int(input(f'Enter a number: '))
        if user_input in input_numbers:
            print('Duplicate')
        else:
            print('Unique')
        input_numbers.append(user_input)
    
    except:
        print('>>Input is not a number! ')
        break
