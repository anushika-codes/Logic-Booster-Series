# Fibonacci Sequence Generator
print("Fibonacci Sequence Generator")

# Get number of terms from user
num = int(input("Enter how many terms you want: "))

# First two terms
a, b = 0, 1
count = 0

# Generate sequence
if num <= 0:
    print("Please enter a positive number.")
elif num == 1:
    print("Fibonacci sequence up to 1 term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < num:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
