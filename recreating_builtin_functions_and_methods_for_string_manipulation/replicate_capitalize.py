# Prompt user to enter a text.
# Apply .lower() to the string.
# Use .replace() to replace the first index of the string with an uppercase version.
# Print the result.

text_input = input("Enter a text in any casing: ")
text_input = text_input.lower()
text_input = text_input.replace(text_input[0], text_input[0].upper())
print(text_input)
