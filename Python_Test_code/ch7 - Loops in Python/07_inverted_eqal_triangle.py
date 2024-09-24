n = 5  # Height of the triangle

# Loop through each level of the triangle
for i in range(n):
    spaces = ' ' * i  # Calculate spaces for the current level
    asterisks = '*' * (2 * (n - i) - 1)  # Calculate asterisks for the current level
    print(spaces + asterisks)  # Print spaces followed by asterisks






# Printing Spaces:

# ' ' * i


# When i = 0, spaces = 0
# When i = 1, spaces = 1
# When i = 2, spaces = 2
# When i = 3, spaces = 3
# When i = 4, spaces = 4
# Printing Asterisks:


# '*' * (2 * (n - i) - 1)
    
# This part calculates the number of asterisks needed. For each row i:

# When i = 0, asterisks = 2 * (5 - 0) - 1 = 9
# When i = 1, asterisks = 2 * (5 - 1) - 1 = 7
# When i = 2, asterisks = 2 * (5 - 2) - 1 = 5
# When i = 3, asterisks = 2 * (5 - 3) - 1 = 3
# When i = 4, asterisks = 2 * (5 - 4) - 1 = 1
# Combining and Printing:


# print(spaces + asterisks)
