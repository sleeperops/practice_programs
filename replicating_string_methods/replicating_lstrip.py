# The idea is that as long as the program is looking at a whitespace, it will skip.
# Once it sees a character that isnt a whitespace, it will start writing the rest, regardless if it encounters a whitespace again.

# Prompts the user to input a text
input_string = input("Enter a text with spaces at the beginning: ")
output_string = ""
state = 0

# Loops through the characters in the text.
for characters in input_string:
    if characters == " " and state == 0: # If both the character is a whitespace and state = 0, skip.
        continue
    elif characters != " " or state == 1: # If either the character a non-whitespace or state = 1, write.
        state = 1
        output_string += characters

# Print result.
print(output_string)