# Program: Print Star Pyramid

# Input
n = int(input("Enter the number of rows: "))

# Print the pyramid
for i in range(1, n + 1):
    # Print spaces
    print(" " * (n - i), end="")
    # Print stars
    print("* " * i)
