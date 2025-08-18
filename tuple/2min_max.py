#method 1

tuple1 = tuple(map(int, input("Enter the numbers in the tuple : ").split()))
print("Original tuple :", tuple1)
print("Maximum element in the tuple is :", max(tuple1))
print("Minimum element in the tuple is :", min(tuple1))

#method 2

tuple2 = tuple(map(int, input("Enter the numbers in the tuple : ").split()))
print("Original tuple :", tuple1)

max_num = tuple2[0]
min_num = tuple2[0]

for i in tuple2[1:]:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i

print("Maximum element in the tuple is :", max_num)
print("Minimum element in the tuple is :", min_num)

