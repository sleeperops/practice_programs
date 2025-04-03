# Prompt the user to input a text.
text = input("Enter a text: ")

# Variable in which the output will be written into.
output_text = ""

# If the character is in lowercase, write in uppercase. Otherwise if it is in uppercase, write it in lowercase.
for char in text:
    if char == char.upper(): # character is in uppercase
        char = char.lower()
        output_text += char
    elif char == char.lower(): # character is in lowercase
        char = char.upper()
        output_text += char

# Print the output
print(f"Swapped casing: {output_text}")