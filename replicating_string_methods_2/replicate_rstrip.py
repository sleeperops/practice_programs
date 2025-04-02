# The idea is that as long as the program is looking at a whitespace, it will skip.
# Once it sees a character that isnt a whitespace, it will start writing the rest, regardless if it encounters a whitespace again.

# Prompts the user to input a text
# Loops through the characters in the text, backwards.
# If both the character is a whitespace and state = 0, skip.
# If either the character a non-whitespace or state = 1 , write.
# Print result.
