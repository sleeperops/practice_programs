# prints all odd numbers from 0 - 100 using while loop

# initialize counter
# while counter is not equal to a hundred
# increment it by 1
# if the current number(counter) is not divisible by 2 (is odd), print it


counter = 0
while counter != 100:
    counter += 1
    if counter % 2 == 1:
        print(counter, end = ' ')
    
    
