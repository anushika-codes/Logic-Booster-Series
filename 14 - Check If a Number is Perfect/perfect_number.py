# Perfect number check

# Input from user
num = int(input("Enter a number: "))

# Variable to store sum of divisors
sum_of_divisors = 0

# Find divisors
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

# Check if perfect
if sum_of_divisors == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")
