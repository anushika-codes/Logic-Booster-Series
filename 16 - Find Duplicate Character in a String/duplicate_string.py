# Program to find duplicate characters in a string

# Take input from user
string = input("Enter a string: ")

# Convert string to lowercase to handle case sensitivity
string = string.lower()

# Dictionary to store character counts
char_count = {}

# Count each character
for char in string:
    if char != " ":  # ignoring spaces
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

# Display duplicates
print("Duplicate characters are:")
for char, count in char_count.items():
    if count > 1:
        print(char, ":", count, "times")
