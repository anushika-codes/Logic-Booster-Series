# Program: Sort Words in a Sentence Alphabetically

# Take input from user
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Sort words alphabetically (case-insensitive)
words.sort(key=str.lower)

# Print sorted words
print("\nWords in alphabetical order:")
for word in words:
    print(word)
