# Program to count vowels and consonants in a string

# Take input from user
text = input("Enter a string: ")

# Convert to lowercase for uniformity
text = text.lower()

# Define vowels
vowels = "aeiou"

# Initialize counters
vowel_count = 0
consonant_count = 0

# Loop through each character
for char in text:
    if char.isalpha():  # check if it's a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Display result
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
