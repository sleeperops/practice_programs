# Prompt the user to enter sample_text
sample_text = input("Enter a sample text: ")

# Prompt the user to enter the total string length
target_length = int(input("Enter the length of the text: "))

# Prompt the user to enter the character that will be used to fill the extra spaces 
padding = input("Enter the padding/filler: ")

# Compare the target length 
def mock_ljust(sample_text, length, padding):
    pad_ammount = length - len(sample_text) # Determines how much padding is needed to be printed
    return f"{sample_text}{str(padding * pad_ammount)}"

# Print the result
print(mock_ljust(sample_text, target_length, padding))
