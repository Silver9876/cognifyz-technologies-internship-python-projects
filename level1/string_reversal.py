# Heading:
"""
String Reversal Program
"""

# Prompt the user to enter a string
str_input = input("Enter the string: ")

# Initialize an empty string to store the reversed string
reversed_str = ""

# Iterate through each character in the input string
for char in str_input:
    # Concatenate the characters in reverse order
    reversed_str = char + reversed_str

# Print the reversed string
print(reversed_str)
