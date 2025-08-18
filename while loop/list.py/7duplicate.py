# Remove Duplicates from a List
num=list(map(int,input("Enter elements: ").split()))
new_list=[]
print("original list: ",num)
for i in num:
    if i not in new_list:
        new_list.append(i)
print("Updated list: ",new_list)        