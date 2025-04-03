# Prompt user to input a string
input_string = input("Enter a text: ")

# Prompt user to input a substring 
input_substring = input("Enter the substring to be found: ")

def mock_index(input_str,input_substr):
    """
        Finds the index of the first occurrence of a substring in a string.
    It takes in a string and its substring as parameters.
    If the substring does not exist within the string, return 'Substring not detected'.
    Otherwise return it's index.
    """
    input_str = str(input_str)
    input_substr = str(input_substr)

    result =  input_str.find(input_substr)
    if result == -1:
        return "Substring not detected"
    else:
        return result

# Print the result.
print(mock_index(input_string, input_substring))