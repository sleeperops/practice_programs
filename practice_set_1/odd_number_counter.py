# use a for loop to ask for a number ten times
# divide the number by two
# if it returns a remainder of one (the number is odd), increment the count of odd numbers by 1
# print the count of odd numbers

def odd_numbers():
    odd_num_count = 0
    counter = 10  # countdown, for auxillary purposes
    for _ in range(10):  # Asks for a number ------------------------
        number = int(input(f'Input a number ({counter}): '))
        if number % 2 == 1:  # if odd, add 1 to the total amount of odd numbers and continue
            odd_num_count += 1
        counter -= 1  # countdown, for auxillary purposes
    print(f'There are {odd_num_count} odd numbers')

odd_numbers()
      
