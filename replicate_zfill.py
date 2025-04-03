# Prompt the user to enter a sample text/ number
# Prompt the user to enter the target length 
# To determine the ammount of zeroes to be used, subtract the length of the sample text to the target length
# Print the zeroes along with the text
 
input_text = input("Enter a text or a number: ")
target_length = input("Enter the target length of the text: ")

def mock_zfill(text, target_length):
    zero_ammount = int(target_length) - len(text)
    return f"{'0' * zero_ammount}{text}"

print(mock_zfill(input_text, target_length))
