# use a for loop to iterate 101 times (for loop is excludes the last number)
# for every loop, use modulo to check if number is divisible by two
# if yes, print
# else, continue the loop

def only_even():
    for num in range(101):
        if num % 2 == 0:
            print(num)
        else:
            continue
   
only_even()
