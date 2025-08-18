'''set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Write a program to return a new set containing identical items present in both set1 and set2.'''

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3=set1.intersection(set2)
print(set3)