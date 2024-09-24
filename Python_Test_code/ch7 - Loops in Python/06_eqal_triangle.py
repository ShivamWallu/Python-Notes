n=5
for i in range(n):
    print(' '*(n-i-1)+'*'*(2*i+1))                      # WAY- 1




n = 5  # Height of the pyramid                                      # WAY - 2

# Loop through each level of the pyramid
for i in range(n):
    spaces = ' ' * (n - i - 1)  # Calculate spaces for the current level
    asterisks = '*' * (2 * i + 1)  # Calculate asterisks for the current level
    print(spaces + asterisks)  # Print spaces followed by asterisks





# STEP -1 

# ' ' * (n - i - 1)
    
# This part calculates the number of spaces needed before the asterisks. For each row i:
    
# When i = 0, spaces = 5 - 0 - 1 = 4
# When i = 1, spaces = 5 - 1 - 1 = 3
# When i = 2, spaces = 5 - 2 - 1 = 2
# When i = 3, spaces = 5 - 3 - 1 = 1
# When i = 4, spaces = 5 - 4 - 1 = 0
# Printing Asterisks:



# STEP -2 

# '*' * (2 * i + 1)
    
# This part calculates the number of asterisks needed. For each row i:

# When i = 0, asterisks = 2 * 0 + 1 = 1
# When i = 1, asterisks = 2 * 1 + 1 = 3
# When i = 2, asterisks = 2 * 2 + 1 = 5
# When i = 3, asterisks = 2 * 3 + 1 = 7
# When i = 4, asterisks = 2 * 4 + 1 = 9
# Combining and Printing:



# STEP -3
    
# print(' ' * (n - i - 1) + '*' * (2 * i + 1))
