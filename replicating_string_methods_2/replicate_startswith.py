# Prompt the user to enter an input text
# Prompt the user to enter a prefix to check
# Loop through the prefix and for every character, check if it matches the ones in the input_text.
# If the loop finishes with all characters matching, return TRUE
# Otherwise, return FALSE 

input_text = input("Enter a text: ")
prefix = input("Enter the prefix you want to check: ")

def mock_startswith(text, prefix):
    text= str(prefix)
    prefix = str(prefix)

    # For every character in the prefix, check the input_text
    for prefix_characters in prefix:
        for input_characters in input_text:
            if prefix_characters == input_characters:
                break # problem here, I want it to continue in the main for loop
            elif prefix_characters != input_characters:
                return False
                
        # If program finished without causing an error, return TRUE
        return True
    
print(mock_startswith(input_text, prefix))

# ! If len of prefix is greater than input, return false 
