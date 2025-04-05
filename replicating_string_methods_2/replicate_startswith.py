input_text = input("Enter a text: ")
prefix = input("Enter the prefix you want to check: ")

def mock_startswith(text, prefix):
    prefix = str(prefix)
    text = str(text)

    if len(prefix) > len(text):  # Error handling
        return False
    
    for index_mark in range(len(prefix)):  # The number of loops depends on the length of the prefix
        if prefix[index_mark] == text[index_mark]:  # If the characters in the current index is equal
            continue
        elif prefix[index_mark] != text[index_mark]:  # If they do not match
            return False
    return True  # If the the program finishes and all character in the prefix matches the start of the text


print(mock_startswith(input_text, prefix))
