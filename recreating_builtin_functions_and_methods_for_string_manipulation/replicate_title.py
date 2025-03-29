# # Prompt the user to enter a text: 
# Split the text into words and store that into a list.
# Loop through each list and capitalize the first letter of each word.
# Rejoin the list into as a single text and print the output. 

text = "What a beautiful face"
text = text.lower()
output_text = []

# split text into a list
word_list = text.split() 
print(word_list)

# Capitalize each first letter of the word
for word in word_list:
    word[0].upper()
    output_text.append(word[0].upper())

# rejoin the list into a text
print(" ".join(output_text))