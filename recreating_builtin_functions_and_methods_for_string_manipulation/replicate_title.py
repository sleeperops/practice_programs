# # Prompt the user to enter a text: 
# Split the text into words and store that into a list.
# Loop through the words in list.
# First capitalize the first letter, write it into the output_text.
# Second, write the rest of the letters and write it into the output_text.
# Lastly, add the space at the end.
# Print the resulting text.

# User input
text = input("Input a text to be converted into titlecase: ")
text = text.lower()
output_text = ""

# split text into a list
word_list = text.split() 
print(word_list)

# Loop through every word in the list
for word in word_list:
    output_text += word[0].upper() # Write the first letter in uppercase
    output_text += word[1:] # Writes the rest of the letters
    output_text += " " # Writes the space 

# Simply removes the extra space at the end that is produced in the loop.
output_text.rstrip()

# Prints the result.

print(text)
print(output_text)