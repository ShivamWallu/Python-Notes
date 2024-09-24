n = 6  # Number of rows in Floyd's Triangle

num = 1  # Starting number

for i in range(1, 6):  # Loop through each row
    for j in range(1, i + 1):  # Loop through each number in the current row
        print(num, end=' ')  # Print the current number
        num += 1  # Increment the number
    print()  # Move to the next line after each row
