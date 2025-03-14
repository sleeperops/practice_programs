# prints not equal if two numbers are not equal
# enter first input
# enter second input
# if first input is not equal to second
# print 'not a number'
# else print 'equal'

first_input = input('Enter the first number: ')
second_input = input('Enter the second number: ')

def not_equal(input_1, input_2):
    if input_1 != input_2:
        return 'Not Equal'
    else:
        return 'Equal'
