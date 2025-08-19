# Count the Occurrences of an Element in a List
#Method 1
num=list(map(int,input("Enter numberes to the list: ").split()))
element=int(input("Enter the element: "))
count=num.count(element)
print(count)

#method 2
num2=list(map(int,input("Enter numberes to the list: ").split()))
element2=int(input("Enter the element: "))
count2=0

for i in num2:
    if element2 == i:
        count2+=1
print("count =",count2)        
