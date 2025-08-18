#Write a Python Program to Check weather a candidate Eligible for Vote or not. Age=int(input("enter your age"))
age=int(input("Enter your age: "))
if age>=1:
    if age>=18:
        print("You are eligible.")
    else:
        print("You are not eligibile") 
else:
    print("Enter valid age.")           