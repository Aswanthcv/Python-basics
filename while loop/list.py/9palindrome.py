# Check if a List Is Palindromic
num=list(map(int,input("Enter numberes to the list: ").split()))
new_list=[]
if num == num[::-1]:
    print("palindrome")
else:
    print("not a palindrome.")    
