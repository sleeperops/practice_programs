# Similar to lstrip, except the loop starts from right to left and not the other way around 
# The idea is that as long as the program is looking at a whitespace, it will skip.
# Once it sees a character that isnt a whitespace, it returns the start of the input until the last iteration.

# Prompts the user to input a text
input_string = input("Enter a text with spaces at the end: ")

def mock_rstrip(input_string):
    input_string = str(input_string) # To allow the function to use string methods like index
    length_of_input = len(input_string) # Will be used in determining how many characters are in the input
    counter = 0 # Will also be used to track how far from the right is the current iteration.

    for characters in input_string[::-1]: # Loops through the characters in the input_text.
        counter += 1 # Will be used to keep track of the index
        if characters != " ":  # If character is not a whitespace
            length_of_input = len(input_string) # Get the length of the input string
            current_index = length_of_input - counter # Subtract the length from the counter to determine the index of the current iteration
            return input_string[0:current_index + 1] # Print the input from the start to the last iteration (+1 to include the last one)
       
# Print result.
print(f"{mock_rstrip(input_string)}This should be close to the text")