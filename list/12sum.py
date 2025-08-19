
# list1=[1,2,3,4,5,6,7,8]
list1=list(map(int,input("Enter the values: ").split()))
i=0
sum=0
while i<len(list1):
    if list1[i] % 2 == 0:
        sum=sum+list1[i]
    i=i+1
print("Sum of even numbers in the list:",sum)    

