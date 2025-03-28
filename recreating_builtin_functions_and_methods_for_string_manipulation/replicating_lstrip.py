# The idea is that as long as the program is looking at a whitespace, it will skip.
# Once it sees a character that isnt a whitespace, it will start writing those characters.

# Prompt the user to input a text
# Loop through the text, if both the character is a whitespace and the state is equal to 0, skip
# Once it sees a non-whitespace character, set the state to 1 and write the character into 'output_string'
# After the state is set to 1, the program will never skip anymore, which means the rest of the character will be written.

input_string = input("Enter a text with spaces at the beginning: ")
output_string = ""
state = 0
for characters in input_string:
    if characters == " " and state == 0:
        continue
    elif characters != " ": # use or?
        state = 1
        output_string += characters
    elif state == 1:
        output_string += characters

print(output_string)