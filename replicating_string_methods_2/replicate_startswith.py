# Prompt the user to enter an input text
# Prompt the user to enter a prefix to check
# Check if the beginning of both text matches
# If the loop finishes with all characters matching, return TRUE
# Otherwise, return FALSE 

input_text = input("Enter a text: ")
prefix = input("Enter the prefix you want to check: ")

def mock_startswith(text, prefix):
    prefix = str(prefix)
    text = str(text)
    
    index_mark = 0 # Serves to mark the index of the loop 
    for _ in range(len(prefix)): # The number of loops depends on the length of the prefix
        if prefix[index_mark] == text[index_mark]:
            index_mark += 1
            continue
        elif prefix[index_mark] != text[index_mark]:
            return False
    return True


print(mock_startswith(input_text, prefix))
