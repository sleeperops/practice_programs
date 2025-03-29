# Prompt the user to enter an input as a text.
# Convert the text to lowercase.
# Initialize variables 'state' and 'output_text'.
# Loop through the text and do the following:
#    If the the program detects a whitespace, set the state to 0 and write the whitespace to the output_text. Keep state as 0.
#    Elif the program detects a non-whitespace but the state is 0 (meaning it is the first letter in the word.), capitalize it and
#         write it to the output_text. Increment state by 1.
#    Elif it is a non whitespace, and the state is 1 or more, write it to output_text. Increment state by 1.
# Print the result

text = input("Enter a text to be converted into titlecase: ").lower()
state = 0
output_text = ""

for char in text:
    if char == " ": # if whitespace
        state = 0
        output_text += char
    elif char != " " and state == 0: # not whitespace and is first letter in the word
        state += 1
        output_text += char.upper() 
    elif char != " " and state >= 1:
        state += 1
        output_text += char
print(output_text)