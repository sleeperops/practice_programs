# Prompt the user to enter a string and store it in 'text'
# Prompt the user to enter a substring and store it in 'target'
# Use a while loop and an 'index' to simulate a for loop
# Loop through the string
# For every item in the string, run another for loop.
# Start from the current index up until nth number of indices
# n is equal to the length of the subtring
# Example: 
#   string = "abcde", substring = "cde"
#   iteration 1: "abc"
#   iteration 2: "bcd"
#   iteration 3: "cde" <- is equal to substring
#   iteration 4: "de"
#   iteration 5: "e"
# Write each of these characters in 'temp_output'
# Check if these characters is equal to the target substring
# If it is, increment 'occurrence_counter' by 1 and move to the next index.
# Otherwise, move on and clear 'temp_output'
# Print the 'occurrence_counter'