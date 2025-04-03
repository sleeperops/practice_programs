# To determine the ammount of padding that will be used to center the text, subtract length_input from len(text_input)
# Divide it by two. In the case of odd numbers wherein the difference is not equal, store the bigger half into 'prefix'.
# Store the smaller half into 'suffix'.
# # Print the prefix at the start, the text_input in the middle and the suffix at the end.

# Prompt the user to enter a sample text, the length of the text and the padding character which will be used to center the text
text_input = input("Enter a sample text: ")
length_input = int(input("Enter the target length of the text: "))
pad_char_input = input("Enter the padding character that will be used to fill the text: ")

def mock_center(text, target_length, pad):
    pad_ammount = target_length - len(text) # Determines the ammount of padding to be used based on the target length
    if pad_ammount % 2 == 1: # if the ammount of padding to be used is an odd number, divide it into two factors.
        prefix = -(-pad_ammount // 2) # This divides the pad_ammount by 2 and rounds it up. This gets the larger factor
        suffix = (pad_ammount//2) # This divides the pad_ammount by 2 and rounds it down. This gets the smaller factor
    else: 
        prefix = (pad_ammount /2) 
        suffix = (pad_ammount /2)

    return f"{pad * int(prefix)}{text}{pad * int(suffix)}"

print(mock_center(text_input, length_input, pad_char_input))