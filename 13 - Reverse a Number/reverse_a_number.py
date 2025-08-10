# Reverse a Number 

n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10           # get last digit
    reverse = reverse * 10 + digit  # add digit to reverse
    n //= 10                 # remove last digit

print("Reversed number:", reverse)
