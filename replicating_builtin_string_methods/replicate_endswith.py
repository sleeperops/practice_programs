# If the characters match, move on to the next character in the suffix.
# Once it fails, break the loop and return FALSE.
# If the loop finished without discepancies, return TRUE.
# Call the function and print the result.

# Prompt the user to input a sample_text and a suffix 
input_text= input("Enter a sample_text: ")
suffix = input("Enter the suffix: ")

# From right to left, search through the suffix and compare it with the input sample_text
def better_endswith(input_text, suffix):
    for suffix_char in suffix[::-1]:
        for input_char in input_text[::-1]:
            if suffix_char != input_char:
                print("FALSE")
                break
        else: 
            print("TRUE")
            break




better_endswith(input_text, suffix)
