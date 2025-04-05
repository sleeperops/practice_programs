# Prompt the user to input a sample_text and a suffix 
input_text= input("Enter a sample_text: ")
suffix = input("Enter the suffix: ")

def better_endswith(text, suffix):
    """
    Checks if a suffix is present in the end of a text.
    Accepts text and suffix as parameters,
    returns a boolean value of True or False
    """

    # Converts the parameters to string to allow iteration
    text  = str(text)
    suffix = str(suffix)

    # Initialize starting index for the main text
    starting_index = len(text) - len(suffix)

    # Initialize starting index for the suffix
    suffix_index = 0 

    # Return False when the length of the suffix is longer than the text
    if len(suffix) > len(text):
        return False
    
    # Cuts a section in the end of the text based on the length of the suffix
    for index in range(starting_index, len(text)):  # Loop through that section

        # If characters match
        if suffix[suffix_index] == text[index]:
            suffix_index += 1  # Increments by 1 to move through the suffix
            continue  # Continue through the loop

        # If characters fails to smatch
        elif suffix[suffix_index] != text[index]:  
            return False  
    return True  # If loop finishes without any mismatching characters

# Prints the result
print(better_endswith(input_text, suffix))

