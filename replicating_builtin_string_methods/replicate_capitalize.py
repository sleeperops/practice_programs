# Prompt user to enter a text.
input_text = input("Enter a text in any casing: ")

# Write the first letter of the input into the output and capitalizes it.
output_text = input_text[0].upper()

# Convert the original text into lowercase
input_text = input_text.lower()

# Write the rest of the text (exluding the first character) into the output.
for char in input_text[1:]:
    output_text += char

# Print the result.
print(output_text)

