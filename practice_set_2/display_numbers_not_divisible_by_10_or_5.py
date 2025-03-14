# prints all numbers from 0 - 100 not ending in 5 or 0

# run a for loop that counts to 100
# for every loop, check if the current number is divisible by 5 or 10
# if it is, skip that number
# else, print it

for num in range(100):
    if num % 5 == 0 or num % 10 == 0:
        continue
    else:
        print(num, end = ' ')
