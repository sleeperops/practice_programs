# Prompt user to enter a sample text
input_text = input("Enter a text: ")

# Prompt user to enter the target length of the text
input_target_length = int(input("Enter the target length: "))

# Prompt user to enter the padding that will be used to fill up the spaces
input_pad = input("Enter the padding that will be used to fill up the spaces: ")

def mock_rjust(text, target_length, pad):
    text_length = len(text)
    padding_ammount = target_length - text_length # Determines how much padding will be used to fill the spaces
    
    return f"{pad * padding_ammount}{text}"

print(mock_rjust(input_text, input_target_length, input_pad))