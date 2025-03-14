# difference of two numbers
# enter first input
# enter second input
# subtract the second number from the first
# print output

first_input = input('Enter the first number: ')
second_input = input('Enter the second number: ')
def difference(input1, input2):
    return input1 - input2
try:
    first_input = int(first_input)
    second_input = int(second_input)
    print(f'Difference: {difference(first_input, second_input)}')
except:
    print('>>Not a number')
 # ===============================================
 
