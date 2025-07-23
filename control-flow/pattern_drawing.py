# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Start from the first row
row = 0

# While loop will handle each row
while row < size:
    # For loop will print stars in that row
    for col in range(size):
        print("*", end="")  # end="" means: don't move to a new line yet

    print()  # after finishing a row, move to the next line
    row += 1  # move to the next row
