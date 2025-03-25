# Prompt user to input their fullname in incorrect casing.
fullname = input("Enter your fullname in incorrect casing: ")

# Convert the casing into title case using .lower().
fullname = fullname.lower()

# Store each word into a list using .split().
word_list = fullname.split()

# Rejoin the list into a single text using the .join() method.
snake = '_'.join(word_list)

# Print the result.
print(snake)
