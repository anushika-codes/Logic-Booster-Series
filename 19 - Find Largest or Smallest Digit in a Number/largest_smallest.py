# Find largest and smallest digit in a number

# Input
num = input("Enter a number: ")

# Initialize variables
largest = int(num[0])
smallest = int(num[0])

# Loop through each digit
for digit in num:
    digit = int(digit)
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit

# Output 
print("Largest digit:", largest)
print("Smallest digit:", smallest)
