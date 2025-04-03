# Prompt the user to enter a text in random casing
text_input = input("Input a text in random casing: ")

# Apply .upper() on the text to capitalize all characters
text_input = text_input.upper()

# Apply .swapcase() to reverse the casing
text_input = text_input.swapcase()

# Print the result
print(text_input)
