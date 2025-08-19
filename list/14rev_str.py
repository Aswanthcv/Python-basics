#second largest element in the list

list1=list(map(int,input("Enter elements: ").split()))
list1.sort(reverse=True)
print("Second largest element is: ",list1[1])