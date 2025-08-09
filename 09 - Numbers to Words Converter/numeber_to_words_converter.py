# Numbers to Words Converter

def number_to_words(num):
    """Convert a number into words (supports up to billions)"""

    # Dictionaries for number names
    ones = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen"
    }

    tens = {
        20: "twenty", 30: "thirty", 40: "forty",
        50: "fifty", 60: "sixty", 70: "seventy",
        80: "eighty", 90: "ninety"
    }

    thousands = ["", "thousand", "million", "billion"]

    if num < 0:
        return "minus " + number_to_words(-num)

    if num < 20:
        return ones[num]

    if num < 100:
        if num % 10 == 0:
            return tens[num]
        else:
            return tens[num // 10 * 10] + "-" + ones[num % 10]

    if num < 1000:
        if num % 100 == 0:
            return ones[num // 100] + " hundred"
        else:
            return ones[num // 100] + " hundred and " + number_to_words(num % 100)

    # For numbers 1000 and above
    for i, word in enumerate(thousands):
        if num < 1000 ** (i + 1):
            left_part = num // (1000 ** i)
            right_part = num % (1000 ** i)

            if right_part == 0:
                return number_to_words(left_part) + " " + thousands[i]
            else:
                return number_to_words(left_part) + " " + thousands[i] + ", " + number_to_words(right_part)


# Main Program
print("=== Numbers to Words Converter ===")

while True:
    user_input = input("\nEnter a number (or type 'exit' to quit): ").strip()

    if user_input.lower() == "exit":
        print("Goodbye! 👋")
        break

    if not user_input.isdigit() and not (user_input.startswith('-') and user_input[1:].isdigit()):
        print("❌ Invalid input! Please enter a valid integer.")
        continue

    number = int(user_input)
    words = number_to_words(number)
    print(f"✅ {number} in words is: {words}")
