# Factorial Calculator
print("Factorial Calculator")

# Get input from user
num = int(input("Enter a non-negative number: "))

# Factorial of negative number doesn't exist
if num < 0:
    print("❌ Factorial does not exist for negative numbers.")
elif num == 0 or num == 1:
    print(f"The factorial of {num} is 1")
else:
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
  
