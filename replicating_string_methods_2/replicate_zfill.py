# Prompt the user to enter a sample text/ number
input_text = input("Enter a text or a number: ")

# Prompt the user to enter the target length 
target_length = input("Enter the target length of the text: ")

# Subtract the length of the sample text to the target length
def mock_zfill(text, target_length):
    zero_ammount = int(target_length) - len(text) 
    return f"{'0' * zero_ammount}{text}"

# Print the zeroes along with the text
print(mock_zfill(input_text, target_length))
