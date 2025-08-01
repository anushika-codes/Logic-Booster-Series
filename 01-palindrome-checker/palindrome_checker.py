# Palindrome Checker Program

def palindrom(text):
    # Step 1: Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()

    # Step 2: Reverse the cleaned text
    reversed_text = cleaned[::-1]

    # Step 3: Compare original and reversed
    return cleaned == reversed_text

# Main program
print("Palindrome Checker")
user_input = input("Enter a word or number: ")

# Check and print result
if palindrom(user_input):
    print("It's a palindrome.")
else:
    print("Not a palindrome.")
