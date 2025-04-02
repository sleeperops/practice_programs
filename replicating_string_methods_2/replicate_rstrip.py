# Similar to lstrip, except the loop starts from right to left and not the other way around 
# The idea is that as long as the program is looking at a whitespace, it will skip.
# Once it sees a character that isnt a whitespace, it will start writing the rest.

# Prompts the user to input a text
input_string = input("Enter a text with spaces at the end: ")


def mock_rstrip(input_string):
    input_string = str(input_string) # To allow the function to use string methods like index
    output_string = ""
    for characters in input_string[::-1]: # Loops through the characters in the input_text.
        if characters == " ": # If both the character is a whitespace and state = 0, skip.
            continue
        elif characters != " ": # If either the character a non-whitespace or state = 1, write.
            state = 1
            break
    return input_string[0:input_string.index(characters)+1] # returns from the start without the whitespace at the end

# Print result.
print(f"{mock_rstrip(input_string)}This should be close to the text")