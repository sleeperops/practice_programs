# displays the highest number
# initialize a list called input_list
# run a while loop as long as it is true
# for every loop, ask the user for an input
# try if the input can be converted to an integer
# > if so add the number to the input_numbers list
# else if it is not an integer print 'not a number' and break from the loop
# sort the input_numbers list using sort() function
# print the [-1] index or the biggest one

# accepts input
input_numbers = []
while True:
    try:
        user_input = int(input(f'Enter a number: '))
        input_numbers.append(user_input)
    
    except:
        print('>>Input is not a number! ')
        break
