def is_leap_year(year):
    # A year is a leap year if it is divisible by 4,
    # except for years divisible by 100, unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Main program
try:
    year = int(input("Enter a year to check if it's a leap year: "))

    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is NOT a leap year.")
except ValueError:
    print("Please enter a valid integer year.")
