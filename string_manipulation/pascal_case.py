# Prompt user to input their fullname in incorrect casing.
fullname = input("Enter your fullname in incorrect casing: ")

# Convert the casing into title case using .title().
fullname = fullname.title()

# Store each word into a list using .split().
word_list = fullname.split()

# Rejoin the list into a single text using the .join() method.
pascal = ''.join(word_list)

# Print the result.
print(pascal)
