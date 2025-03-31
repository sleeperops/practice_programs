# Prompt the user to input a text
# Prompt the user to input the suffix 
# From right to left, search through the suffix and compare it with the input text
# As long as the characters match, keep on going.
# If one character does not match, return FALSE.
# If the loop finished without discepancies, return TRUE.
# Call the function and print the result.

input_text= input("Enter a text: ")
suffix = input("Enter the suffix: ")

def better_endswith(input_text, suffix):
    for input_char in suffix[::-1]:
        for suffix_char in input_text[::-1]:
            if suffix_char != input_char:
                print("FALSE")
                break
        else:
            print("TRUE")



better_endswith(input_text, suffix)
