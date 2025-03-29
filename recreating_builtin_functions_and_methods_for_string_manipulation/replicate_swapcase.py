# Prompt the user to input a text 
# Loop through the text. If the character is in uppercase, create a lowercase version and write it into the output_text
# Else if the character is in lowercase, create an uppercase version and write it into the output_text
# Print the output

text = "this IS A tEsT StRiNG"
output_text = ""

for char in text:
    if char == char.upper(): # character is in uppercase
        char = char.lower()
        output_text += char
    elif char == char.lower(): # character is in lowercase
        char = char.upper()
        output_text += char
print(text)
print(output_text)