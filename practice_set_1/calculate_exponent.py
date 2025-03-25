# accept input for first input
# accept input for second input
# check if input is an integer, if not, display 'Not a number'

# raise the first input to the second input
# # display the answer

def exponent_ab(a, b):
    return a ** b


input_a = input('Input the first number: ')
input_b = input('Input the second number: ')
try:
    input_a = int(input_a)
    input_b = int(input_b)
    print(f'Answer: {exponent_ab(input_a, input_b)}')

except:
    print('>>Not numbers')
# ==============================================
