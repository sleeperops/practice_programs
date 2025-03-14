# initialize a variable named 'total' and set it to zero
# use a for loop to ask for a number ten times
# for every iteration, add the input to the total
# once ten iterations have completed, print the total

def summate():
    total = 0
    for _ in range(10):
        number = int(input(f'Input a number: '))
        total += number
    print(f'The sum of all the numbers is: {total}')
    
summate()
