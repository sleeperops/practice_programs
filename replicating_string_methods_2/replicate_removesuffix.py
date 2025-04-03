# Prompt the user to enter a text 
input_text = input("Enter a text: ")

# Prompt the user to enter a text 
input_suffix = input("Enter the suffix to be removed: ")

def mock_removesuffix(text, suffix):
    """
    Detects and removes the suffix of the text.
    Takes in the text and the suffix as parameters.
    If suffix is detected return the suffixless text,
    otherwise, return None.

    """
    text = str(text)
    suffix = str(suffix)

    if text.endswith(suffix):
        suffix_index = len(text) - len(suffix)
        return text[0:suffix_index]
    else:
        return None
    
# Print the result
print(mock_removesuffix(input_text, input_suffix))