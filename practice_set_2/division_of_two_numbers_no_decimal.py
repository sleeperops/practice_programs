# '''prints the quotient of two numbers without the decimal'''
# enter first input
# enter second input
# divide the first input by the second using floor division
# display the output

first_input = input('Enter the first number: ')
second_input = input('Enter the second number: ')

def quotient_no_dec(input1, input2):
    return f'{input1//input2}'
