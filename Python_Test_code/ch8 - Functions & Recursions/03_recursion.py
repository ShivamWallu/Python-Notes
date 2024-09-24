'''
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(3) = 3 X 2 X 1
factorial(2) = 2 X 1
factorial(1) = 1
factorial(0) = 1
factorial(n) = n X n-1 X ..........3 X 2 X 1


factorial(n) = n * factorial(n-1)
'''

def factorail(n):
    if(n==1 or n==0):
        return 1
    return n * factorail(n-1)

n = int(input("Enter the number: "))
print(f"the factorila of this number is {factorail(n)}")