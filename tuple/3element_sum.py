# Write a Python program to compute the element-wise sum of given tuples.

t1 = tuple(map(int, input("Enter the numbers in the first tuple: ").split()))
t2 = tuple(map(int, input("Enter the numbers in the second tuple: ").split()))

if len(t1) == len(t2):
    add = tuple(t1[i] + t2[i] for i in range(len(t1)))
    print("Element-wise sum of the tuples is:", add)
else:
    print("Tuples are not of the same size.")
