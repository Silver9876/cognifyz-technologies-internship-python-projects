
password = input("Enter the password: ")

# Define a list of special characters
special = ['@', '#', '$', '&', '*']

# Define the minimum length requirement for a strong password
length = 8

# Initialize counters for uppercase, lowercase, digit, and special characters
upper, lower, digit, spec = 0, 0, 0, 0

# Iterate through each character in the password
for char in password:
    # Check if the character is an uppercase letter
    if char.isupper():
        upper += 1
    # Check if the character is a lowercase letter
    elif char.islower():
        lower += 1
    # Check if the character is a special character
    elif char in special:
        spec += 1
    # Check if the character is a digit
    elif char.isdigit():
        digit += 1

# Check if the password meets the criteria for a strong password
if upper > 0 and lower > 0 and digit > 0 and spec > 0 and len(password) > 7:
    print("Strong password")
else:
    print("Weak password")
