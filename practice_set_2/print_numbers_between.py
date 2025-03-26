# prints all numbers in between two numbers

# enter the first input
# enter the second input
# use try and except to make sure the outputs are integers
# if first input is smaller, make it as the minimum value(floor), and make the second input the maximum value (ceiling)
# if second input is smaller, make it as the minimum value(floor), and make the first input the maximum value (ceiling)
# else make it equal
# run a for loop from the minimum(floor) value up to the maximum value(ceiling)
# print the numbers in between

def in_between():
    first_input = input('Enter the first number: ')
    second_input = input('Enter the second number: ')



    if first_input < second_input: # if first input is smaller, make it as the minimum value
        floor_num = first_input
        ceiling_num = second_input
    elif first_input > second_input: # if first input is larger, make it as the maximum value
        ceiling_num = first_input
        floor_num = second_input
    else:
        floor_num = first_input
        ceiling_num = second_input    


    for numbers_in_between in range(floor_num + 1, ceiling_num): # +1 on minimum number to make sure it is not included
        print(numbers_in_between, end = ' ')


