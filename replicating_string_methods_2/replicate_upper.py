# Prompt the user to enter an input
input_text = input("Enter a text to be capitalized: ")

def mock_upper(text):
    text = str(text)
    text = text.lower() # Apply lower() to lowercase the entire input
    text = text.swapcase() # Apply swapcase() to reverse the casing of the input
    return text

# Print the result
print(mock_upper(input_text))