# Prompt the user to enter a text
input_text = input("Enter a text: ")

def mock_islower(text):
    if text == text.lower(): # If the text is equal to its lowercase counterpart, return TRUE
        return True
    else:
        return False # Otherwise, return FALSE
    
print(mock_islower(input_text))