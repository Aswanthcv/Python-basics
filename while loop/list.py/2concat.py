# Concatenate Two Lists Index-Wise: 

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
new_list=[]

for i in range(len(list1)):
    new_list.append(list1[i]+list2[i])
print(new_list)