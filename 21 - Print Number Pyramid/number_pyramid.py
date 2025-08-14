# Print Number Pyramid 

# Take input from the user
rows = int(input("Enter number of rows for the pyramid: "))

def make_row(i):
    # Build numbers like: 1 2 ... i ... 2 1
    inc = list(range(1, i + 1))
    dec = list(range(i - 1, 0, -1))
    return ' '.join(map(str, inc + dec))

# Find the width of the last line for centering
last_line = make_row(rows)
width = len(last_line)

# Print pyramid
for i in range(1, rows + 1):
    line = make_row(i)
    print(line.center(width))
