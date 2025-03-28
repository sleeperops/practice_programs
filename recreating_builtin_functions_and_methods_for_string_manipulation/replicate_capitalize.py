# Prompt user to enter a text.
# Write the first letter of the input_text to another variable called "output_text"
# Apply .upper() to output text
# Apply .lower() to input text
# Loop through the input_text (excluding index zero) and write it into the output_text
# Print the result

input_text = input("Enter a text in any casing: ")
output_text = input_text[0].upper()
input_text = input_text.lower()

for char in input_text[1:]:
    output_text += char

print(output_text)

