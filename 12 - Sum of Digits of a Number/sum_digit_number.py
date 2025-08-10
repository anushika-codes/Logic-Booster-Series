# Sum of Digits of a Number 

n = int(input("Enter a number: "))
sum_digits = 0

while n > 0:
    digit = n % 10       # get last digit
    sum_digits += digit  # add to sum
    n //= 10             # remove last digit

print("Sum of digits:", sum_digits)
