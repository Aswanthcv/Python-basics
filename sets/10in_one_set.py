# Write a program that takes two sets as input and returns a new set containing the elements that
#  are present in the first set but not in the second set

set1 = set(map(int, input("Enter elements to set 1: ").split()))
set2 = set(map(int, input("Enter elements to set 2: ").split()))

difference=set1.difference(set2)
print("elements present in set1 but not set2",difference)