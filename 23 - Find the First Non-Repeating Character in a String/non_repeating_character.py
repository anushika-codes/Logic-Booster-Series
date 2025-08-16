# Program: Find the First Non-Repeating Character in a String

def first_non_repeating(s):
    # Count occurrences of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

# Take input from user
string = input("Enter a string: ")

result = first_non_repeating(string)

if result:
    print("The first non-repeating character is:", result)
else:
    print("No non-repeating character found.")
