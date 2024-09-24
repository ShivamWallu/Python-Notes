num = int(input("Eneter a number : "))

for i in range(1, num):
    if(num%2) == 0:
        print("Number is not prime")
        break
else:
    print("this is a prime number")  