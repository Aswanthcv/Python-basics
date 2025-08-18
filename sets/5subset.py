# Write a program to check if set2 is a subset of set1.
set1=set(map(int,input("Enter the elements for set1 : ").split()))
set2=set(map(int,input("Enter the elements for set2 : ").split()))
subset=set2.issubset(set1)
print(subset)
