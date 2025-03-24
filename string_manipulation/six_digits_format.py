# Ask for input 
user_input = int(input('Enter a number from 0-1000: '))

# Use f-string to format number to a 6 digit format
six_digit = f'{user_input:06d}'

# prints the result
print(six_digit)

