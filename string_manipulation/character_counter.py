# Prompt the user to enter their fullname
fullname = input('Enter your fullname: ')

# Loop through the input. Use a counter to record each occurrence of a character
counter = 0
for character in fullname:
    counter += 1

# Print the result
print(counter)

