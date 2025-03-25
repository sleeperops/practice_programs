# Prompt the user to enter a complete statement.
statement = input("Enter a complete statement: ")

# Use .split() method to split the senteces into a list of words
word_list = statement.split(" ")

# Use enumerate() to count the items in the list
# Print the result
print(enumerate(word_list))
