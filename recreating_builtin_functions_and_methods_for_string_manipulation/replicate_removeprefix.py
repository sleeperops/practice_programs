# Prompt the user to enter a text as input. 
user_input = input("Enter a text: ")

# Prompt the user to enter the prefix to be removed
prefix = input("Enter the prefix to be removed: ")

# Apply startswith() method to check if the input starts with the prefix
if user_input.startswith(prefix):
    output = user_input[len(prefix):]
    print(output) #If it does, print the result.
