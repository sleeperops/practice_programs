# Prompt the user to enter a complete statement.
statement = input("Enter a complete statement: ")

# Store each word from the statement to the list using .split() method
word_list = statement.split(" ")

# Use a for loop and a counter to count the number of words in the list.
counter = 0
for word in word_list:
    counter += 1

# Print the result 
print(f"There are {counter} words in that statement.")