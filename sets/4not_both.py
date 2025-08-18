# Write a program to return a set of elements present in either set1 or set2, but not both

set1=set(map(int,input("Enter the elements for set1 : ").split()))
set2=set(map(int,input("Enter the elements for set2 : ").split()))
new_set=set1.symmetric_difference(set2)
print(new_set)