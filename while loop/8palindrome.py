num=(int(input("Enter a number : ")))
num1=num
rev=0
while num > 0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("Reverse : ",rev)    
if rev == num1:
    print("Palindrome too")
else:
    print("Not Palindrome")    