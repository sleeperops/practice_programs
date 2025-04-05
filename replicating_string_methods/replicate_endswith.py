# Prompt the user to input a sample_text and a suffix 
input_text= input("Enter a sample_text: ")
suffix = input("Enter the suffix: ")

def better_endswith(text, suffix):
    text  = str(text)
    suffix = str(suffix)

    # Determines the index from which the loop will start
    starting_index = len(text) - len(suffix)

    # Return False when the length of the suffix is longer than the text
    if len(suffix) > len(text):
        return False
    
    for index in range(starting_index, len(text) + 1):  
        if suffix[index] == text[index]:
            continue  # Character is matchin with each other
        elif suffix[index] != text[index]:
            return False  # Characters fails to mismatch
    return True  # Loop finishes without any mismatching characters

print(better_endswith(input_text, suffix))
