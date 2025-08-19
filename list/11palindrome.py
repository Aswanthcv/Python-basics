#count palindromes
list1=input("Enter the values: ").split()
count=0
i=0
while i<len(list1):
    if list1[i] == list1[i][::-1]:
        count+=1
    i=i+1
print("Palindrome count: ",count)        