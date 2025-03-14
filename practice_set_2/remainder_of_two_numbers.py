# '''prints the remainder'''
# enter first input
# enter second input
# use modulo operator to get the remainder when the first number is divided by the second
# print the result

first_input = input('Enter the first number: ')
second_input = input('Enter the second number: ')

def remainder_r(input1,input2):
    return input1 % input2

try:
    first_input = int(first_input)
    second_input = int(second_input)
    print(f'remainder: {remainder_r(first_input, second_input)}')
except:
    print('>>Not a number')
# ===============================================
