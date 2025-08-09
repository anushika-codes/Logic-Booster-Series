# Binary to Decimal Converter

# Taking binary input from the user
binary_num = input("Enter a binary number: ")

# Converting binary to decimal
try:
    decimal_num = int(binary_num, 2)  # base 2
    print(f"The decimal value of {binary_num} is {decimal_num}")
except ValueError:
    print("Invalid input! Please enter only 0s and 1s.")
