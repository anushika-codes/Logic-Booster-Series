# Program to check Armstrong numbers in a range

# Take range input from user
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print(f"Armstrong numbers between {lower} and {upper} are:")

# Loop through the range
for num in range(lower, upper + 1):
    # Find number of digits
    order = len(str(num))
    
    # Calculate sum of digits raised to the power of order
    sum_of_powers = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** order
        temp //= 10
    
    # Check if Armstrong
    if num == sum_of_powers:
        print(num)
