# use a for loop to run 101 times(for loop excludes last number)
# if the number in the current loop is divisible by ten
# continue through the loop
# else, print the number

def no_zero():
    for num in range(101):
        if num % 10 == 0:
            continue
        else:
            print(num)
no_zero()
