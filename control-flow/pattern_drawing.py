# Prompt user for pattern size
try:
    size = int(input("Enter the size of the pattern: "))
except ValueError:
    size = 0
if size <= 0:
    print("Please enter a positive whole number.")
    raise SystemExit(1)

# Draw square pattern using while and for loops
row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1
