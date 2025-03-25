# accept input for first input
# accept input for second input
# check if input is an integer, if not, display 'Not a number'

# divide the first input by the second input
# display the quotient


input_a = input('Input the first number: ')
input_b = input('Input the second number: ')

def quotient_ab(a, b):
    if a == 0 or b == 0:
        return 'Undefined'
    else:
        return a / b
try:
    input_a = int(input_a)
    input_b = int(input_b)
    print(f'Answer: {quotient_ab(input_a, input_b)}')
except:
    print('>>Not numbers')
# ==============================================





