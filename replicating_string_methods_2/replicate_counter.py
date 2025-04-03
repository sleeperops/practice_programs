# Prompt user to enter text
input_main_string = input("Enter a text: ")

# Prompt the user to enter the substring to be looked for
input_substring = input("Enter the word to be searched: ")

# Split the string into words and store it in a list
def mock_counter(main_str,sub_str):
    word_list = main_str.split()
    counter = 0

    for words in word_list:
        if sub_str in words:
            counter+=1
    return counter
    
# Loop through the list and use the 'in' operator to search each word for the substring
# Increment a counter by one for every time the substring is found
# Print the counter

print(mock_counter(input_main_string, input_substring))
