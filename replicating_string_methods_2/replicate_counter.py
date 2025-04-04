# Prompt the user to enter a string and store it in 'text'
text = "This is a test text this is a test text"

# Prompt the user to enter a substring and store it in 'target'
target = "is"

# Initialize the variable that temporarily stores the substrings for comparison
temp_output = ""

# Initialize the variable that counts the number of matching substrings
occurrence_count = 0

# Initialize the variable that determines the index
index = 0

# Use a while loop and an 'index' to simulate a for loop and loop through the string
while not index >= len(text): # The loop does not exceed the length of the text
    for char in text[index:index+len(target)]: # Start from the current index up until nth number of indices
      print(f"The current index is {index} and it will iterate until {index+len(target)}")
      temp_output += char # Write each of these characters in 'temp_output'
    print(f"The current index right now is at {index}")
    print(f"The current output to be checked is: {temp_output}")

    # Check if these characters is equal to the target substring
    if target == temp_output: # Is equal
       # If it is, increment 'occurrence_counter' by 1 and move to the next index.
       print(f"target is equal to temp_output")
       occurrence_count += 1
       index += 1 # Move to the next character
       print(f"Temp_output: {temp_output}")
    else: # Is not equal
       # Otherwise, move on and clear 'temp_output'
       print("target is not equal to tempt output")
       temp_output = "" # clear the temp_output 
       index += 1 # Move to the next character
       print(f"Temp_output = {temp_output}")

# Print the 'occurrence_counter'
print(f" The total count is {occurrence_count}")
print(f"Count function: {text.count(target)}")




