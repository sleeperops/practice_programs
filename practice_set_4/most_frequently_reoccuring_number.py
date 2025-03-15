# initialize a list_called 'input_list'
# initialize an 'occurrence_counter_dict' dictionary to count how many times the number occured
# initialize a variable named 'most_frequent' which describes how frequent a number appeared
# run a for loop 10 times
# for each loop, ask an input
# append each input in input_list
# run a for loop in the input_list
# for every loop, check if the number is in the occurrence_counter_dict
# if not, append the number in occurrence_counter_dict as a key with a value of 1
# > the key will refer to the number, and the value will refer to the occurence 
# if it already exist in occurrence_counter_dict, add 1 to the value, implying that the number only appeared once

input_list = []
occurrence_counter_dict = {}
most_frequent = 0


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
        
# Loops through the disctionary. Checks if the current key if it has the highest value
for key in occurrence_counter_dict:
    if int(occurrence_counter_dict[key]) > most_frequent:
        most_frequent = key

print(f'Most frequent = {most_frequent}')

print(occurrence_counter_dict)
print(input_list)
   
    

print(occurrence_counter_dict) # test
print(input_list) # test
