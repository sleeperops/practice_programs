# Prompts the user to enter a sentence.
input_text = input("Enter a sentence to check if it's in uppercase or not: ")

# Checks if the input_text is the same as its uppercase version. 
if input_text == input_text.upper():
    print("True")
else:
    print("False")