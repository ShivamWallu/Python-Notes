n = 6

for i in range(1, n):
    print(str(i) * i)




n = 5  # Number of lines to be printed

# Loop through each line
for i in range(1, n + 1):
    digit_string = str(i)  # Convert the current number to a string
    repeated_string = digit_string * i  # Repeat the string 'i' times
    print(repeated_string)  # Print the repeated string


# Explanation
    
# Initialization:
# n = 5
# This sets the number of lines to be printed to 5.

# Loop:
# for i in range(1, n + 1):
# This loop runs from i = 1 to i = n (i.e., i = 1 to i = 5), iterating through each line to be printed.

       
# print(str(i) * i)
# str(i): Converts the current integer i to a string.
# str(i) * i: Repeats the string i exactly i times.
# For each iteration i:

# When i = 1, it prints 1
# When i = 2, it prints 22
# When i = 3, it prints 333
# When i = 4, it prints 4444
# When i = 5, it prints 55555
    

# Output

# 1
# 22
# 333
# 4444
# 55555