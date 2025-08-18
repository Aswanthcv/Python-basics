'''Turn Every Item of a List into Its Square:
Given: numbers = [1, 2, 3, 4, 5, 6, 7]
Expected output: [1, 4, 9, 16, 25, 36, 49]'''

numbers = [1, 2, 3, 4, 5, 6, 7]
new_list=[]
for i in numbers:
    new_list.append(i ** 2)
print(new_list)    


sq=[i ** 2 for i in numbers]
print(sq)