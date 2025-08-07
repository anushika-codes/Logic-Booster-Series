def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    return abs(a * b) // gcd

def main():
    print("🔢 LCM Finder")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    lcm = find_lcm(num1, num2)
    print(f"✅ The LCM of {num1} and {num2} is {lcm}")

if __name__ == "__main__":
    main()
