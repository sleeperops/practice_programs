# displays the input with the most numbers of duplicates(most freqeuntly occuring inputs)

# initialize a list_called 'input_list'
# initialize an 'occurrence_counter_dict' dictionary to count how many times the number occured
# run a for loop 10 times
# for each loop, ask an input
# append each input in input_list
# run a for loop in the input_list
# for every loop, check if the number is in the occurrence_counter_dict
# if not, append the number in occurrence_counter_dict as a key with a value of 1
# > the key will refer to the number, and the value will refer to the occurence of that number
# if it already exist in occurrence_counter_dict, add 1 to the value, implying that the number only appeared once

# initialize a list named 'most_frequent' which describes the most frequently occuring numbers
# initialize a variable named 'highest_value' which describes the highest value in the dictionary
# In the occurrence_counter_dict, search for the keys with the highest value and store it as highest_value
# Search occurence_counter_dict for all the keys with the highest values, store them in most_frequent 
# print most_frequent to display all of the most frequently occuring numbers

input_list = []
occurrence_counter_dict = {}



# gets input and stores it in a list
for i in range(10):
    user_input = input('Enter a number: ')
    input_list.append(user_input)
    
# counts occurrence of number
for number in input_list:
# if the number is found in the dictionary, add 1 to count the number of its occurrence
    if number in occurrence_counter_dict:
        occurrence_counter_dict[number] += 1
# if the number is not found in the dictionary, it will create one with a value of 1
    else:
        occurrence_counter_dict[number] = 1
        
# Loops through the dictionary. Checks the current key if it has the highest value, store the highes_value in a variable. Finally, search every key that has that value
most_frequent = []
highest_value = 0
for key in occurrence_counter_dict:
    if occurrence_counter_dict[key] > highest_value: # removed unnecessary casting
        highest_value = occurrence_counter_dict[key]

# check all the keys with the same value as the highest_value and append them to the most_frequent list
for key in occurrence_counter_dict:
    if occurrence_counter_dict[key] == highest_value:
        most_frequent.append(key)


print(f'Number/s with most duplicates = {most_frequent}')

