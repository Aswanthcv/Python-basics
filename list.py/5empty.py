'''Remove Empty Strings from a List of Strings:
Given: 
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
	Expected output:
list1 = ["Mike",  "Emma", "Kelly", "Brad"]'''

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2=[]
for i in list1:
    if i:
        list2.append(i)
print(list2)        

#using list comprehension
l3=[i for i in list1 if i]
print (l3)