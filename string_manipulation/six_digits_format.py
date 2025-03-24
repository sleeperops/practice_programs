# Ask for input 
# Use f-string to format number to a 6 digit format
# print the result

user_input = int(input('Enter a number from 0-1000: '))
six_digit = f'{user_input:06d}'
print(six_digit)