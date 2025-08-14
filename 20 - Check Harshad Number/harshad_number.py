# Check for Harshad (Niven) Number

# Input
num = int(input("Enter a number: "))

# Calculate sum of digits
sum_of_digits = 0
for digit in str(num):
    sum_of_digits += int(digit)

# Check Harshad condition
if num % sum_of_digits == 0:
    print(num, "is a Harshad (Niven) Number")
else:
    print(num, "is NOT a Harshad (Niven) Number")
