# Find the Maximum and Minimum Values in a List
num=list(map(int,input("Enter numbers to the list: ").split()))
max=num[0]
min=num[0]
for i in num[1:]:
    if i > max:
        max=i
    if i <min:
        min=i 
print(f"Maximum:{max},Minimum:{min}")           