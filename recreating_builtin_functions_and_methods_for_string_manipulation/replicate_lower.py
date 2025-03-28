# Prompt the user to enter a text in random casing
# Apply .upper() on the text to capitalize all characters
# Apply .swapcase() to reverse the casing
# Print the result

text_input = input("Input a text in random casing: ")

text_input = text_input.upper()
text_input = text_input.swapcase()
print(text_input)
