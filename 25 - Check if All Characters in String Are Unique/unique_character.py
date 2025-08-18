# Check if All Characters in String Are Unique

def are_characters_unique(s):
    # Using a set to track seen characters
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

# Input
string = input("Enter a string: ")

if are_characters_unique(string):
    print("All characters in the string are unique.")
else:
    print("The string has duplicate characters.")
