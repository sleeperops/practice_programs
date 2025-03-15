# initialize a list_called 'input_list'
# initialize an 'occurence_counter_dict' dictionary to count how many times the number occured
# initialize a variable named 'most_frequent' which describes how frequent a number appeared
# run a for loop 10 times
# for each loop, ask an input
# append each input in input_list
# run a for loop in the input_list
# for every loop, check if the number is in the occurence_counter_dict
# if not, append the number in occurence_counter_dict as a key with a value of 1
# > the key will refer to the number, and the value will refer to the occurence 
# if it already exist in occurence_counter_dict, add 1 to the value, implying that the number only appeared once

input_list = []
occurence_counter_dict = {}
most_frequent = 0


# gets input and stores it in a list
for i in range(10):
    user_input = input('Enter a number: ')
    input_list.append(user_input)
