# Similar to lstrip, except the loop starts from right to left and not the other way around 
# The idea is that as long as the program is looking at a whitespace, it will skip.
# Once it sees a character that isnt a whitespace, it will start writing the rest, regardless if it encounters a whitespace again.

# Prompts the user to input a text
input_string = input("Enter a text with spaces at the end: ")


def mock_lstrip(input_string):
    output_string = ""
    state = 0
    for characters in input_string[::-1]: # Loops through the characters in the input_text.
        if characters == " " and state == 0: # If both the character is a whitespace and state = 0, skip.
            continue
        elif characters != " " or state == 1: # If either the character a non-whitespace or state = 1, write.
            state = 1
            output_string += characters
    return output_string

# Print result.
print(f"{mock_lstrip(input_string)}This should be close to the text")