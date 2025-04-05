# Prompt the user to input a sample_text and a suffix 
input_text= input("Enter a sample_text: ")
suffix = input("Enter the suffix: ")

def better_endswith(text, suffix):
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
        print(f"Current text index: {index}, current suffix index {suffix_index}")

        if suffix[suffix_index] == text[index]:
            suffix_index += 1  # Increments to move through the suffix by one value
            print(f"Current characters match")
            continue  # Character is matching with each other
        elif suffix[suffix_index] != text[index]:
            return False  # Characters fails to mismatch
    return True  # Loop finishes without any mismatching characters

print(better_endswith(input_text, suffix))
print(input_text.endswith(suffix))
