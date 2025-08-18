"Write a Python program to create a new set that contains only unique items from "
"both set1 and set2, removing any duplicates."""
set1=set(map(int,input("Enter the elements for set1 : ").split()))
set2=set(map(int,input("Enter the elements for set2 : ").split()))

new_set=set1.union(set2)
print(new_set)