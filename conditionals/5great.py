#Take two int values from user and print greatest among them.
n1=int(input("Enter a number: "))
n2=int(input("Enter another number: "))

if n1>n2:
    print(f"{n1} is greater")
elif n1<n2:
    print(f"{n2} is greater")
else:
    print("Both are same")        