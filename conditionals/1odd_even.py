#Write a Python Program to Check weather a Given Number is odd or Even. n=10

n=int(input("enter a number"))
if n>=0:
    if n%2==0:
        print("Even number.")
    else:
        print("Odd number.")    
else:
    print("invalid input!")         