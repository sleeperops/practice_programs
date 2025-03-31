# Prompt the user to input a text
# Prompt the user to input the suffix 
# Run a backwards for loop through the suffix 

text = input("Enter a text: ")
suffix = input("Enter the suffix: ")

# Starting from right to left, loop through the suffix and compare it to the original input
for suffix_char in suffix[::-1]:
    for letters in text[::-1]: # Compares the suffix to the original input
        if suffix_char == letters: # If the a character in the suffix is equal to that of the input
            print("True")
    else: # if the condition is not met
        print("False")