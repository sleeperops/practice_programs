# Prompt the user to enter a string and store it in 'text'
text = input("Enter a text: ")

# Prompt the user to enter a substring and store it in 'target'
target = input("Enter the text you want to look for: ")

# Initialize the variable that temporarily stores the substrings for comparison
temp_output = ""

# Initialize the variable that counts the number of matching substrings
occurrence_count = 0

# Initialize the variable that determines the index
index = 0

# Use a while loop and an 'index' to simulate a for loop and loop through the string
while index < len(text): 
    for char in text[index:index+len(target)]:  # Get a slice of text equal to the length of the target, starting at the current index
      temp_output += char  # Write each of these characters in 'temp_output'

    # Check if these characters is equal to the target substring
    if target == temp_output:  # If equal
       occurrence_count += 1  # Increment 'occurrence_counter' by 1 and move on to the next index.
       index += 1  
    else:  # If not equal
       temp_output = ""  # Clear the temp_output 
       index += 1  # Move to the next character

# Print the 'occurrence_counter'
print(occurrence_count)





