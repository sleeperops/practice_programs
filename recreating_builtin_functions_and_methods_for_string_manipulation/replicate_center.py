# Prompt the user to enter a sample text, the length of the text and the padding character which will be used to center the text
# Initialize text_input as the sample text, length_input as the length of the sentence and pad_char_input as the padding character.
# To determine the ammount of padding that will be used to center the text, subtract length_input from len(text_input)
# Divide it by two. In the case of odd numbers wherein the difference is not equal, store the bigger half into 'prefix'.
# Store the smaller half into 'suffix'.
# # Print the prefix at the start, the text_input in the middle and the suffix at the end.

text_input = input("Enter a sample text: ")
length_input = int(input("Enter the target length of the text: "))
pad_char_input = input("Enter the padding character that will be used to fill the text: ")

def mock_center(text, length, pad):
    pad_ammount = length - len(text)
    if pad_ammount % 2 == 1: # if odd
        prefix = -(-pad_ammount // 2) # This divides the pad_ammount by 2 and rounds it up
        suffix = (pad_ammount//2) # This divides the pad_ammount by 2 and rounds it down
    else: 
        prefix = (int(pad_ammount /2))
        suffix = (int(pad_ammount /2))
    
    return f"{pad * int(prefix)}{text}{pad * int(suffix)}"

print(mock_center(text_input, length_input, pad_char_input))