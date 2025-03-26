# use a for loop to ask for ten numbers
# initialize a list named 'input_numbers' that will store all of the inputs
# initialize an empty list named 'unduplicating_list'
# initialize an empty list named 'marked_as_duplicate'
# run a for loop in the 'input_numbers' list
# for every loop check if the numbers in that list is in the unduplicating list
# if not, add it
# elif its already in the list, add the number to marked_as_duplicate
# run another for loop in unduplicating_list
# for every loop, check if the item is in marked_as_duplicate
# if it is, remove the item from the list
# print the unduplicating list

input_numbers = []
unduplicating_list = []
clone_unduplicating_list = [] # to make sure the program does not remove an item from unduplicatin_list while iterating through it
marked_as_duplicate = []

for i in range(10):
    user_input = input(f'Enter a number {i + 1}: ')
    input_numbers.append(user_input)

for numbers in input_numbers:  # creates an unduplicating list
    if numbers not in unduplicating_list:
        unduplicating_list.append(numbers)
    else:
        marked_as_duplicate.append(numbers)
        
for numbers in unduplicating_list:  # copies all the numbers from the unduplicating list 
    clone_unduplicating_list.append(numbers)
    
for number in unduplicating_list:  # removes all the numbers that is marked as duplicate
    if number in marked_as_duplicate:
        clone_unduplicating_list.remove(number)
        

print(clone_unduplicating_list)
    
