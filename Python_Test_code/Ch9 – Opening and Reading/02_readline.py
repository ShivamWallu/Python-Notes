# Open the file in read mode
f = open("this.txt", "r")

# Read the first line (and discard it)
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
line4 = f.readline()

# Print each of the four lines
print("Line 1:", line1.strip())  # strip() removes any extra newlines or spaces
print("Line 2:", line2.strip())
print("Line 3:", line3.strip())
print("Line 4:", line4.strip())

# Close the file
f.close()
