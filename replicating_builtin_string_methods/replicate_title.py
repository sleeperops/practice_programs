# Prompt the user to enter an input as a text. Convert it to lowercase
text = input("Enter a text to be converted into titlecase: ").lower()

# Initialize variables 'state' and 'output_text'.
state = 0
output_text = ""


for char in text:
    if char == " ": # If the current character is a whitespace
        state = 0
        output_text += char # Write the character
    elif char != " " and state == 0: # If the current character is not a whitespace but the previous character is a whitespace
        state += 1
        output_text += char.upper() # Capitalize and write the character
    elif char != " " and state >= 1: # If the current and previous characters are not whitespaces
        state += 1
        output_text += char # Just write the character

# Print the result
print(output_text)