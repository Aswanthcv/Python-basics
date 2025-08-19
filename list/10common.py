# Find the common elements between Two Lists
list1=list(map(int,input("Enter numberes to the list: ").split()))
list2=list(map(int,input("Enter numberes to the list: ").split()))
common=[]
for i in list1:
    if i in list2:
        common.append(i)
print("common elements: ",common)
        