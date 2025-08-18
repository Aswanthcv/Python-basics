'''Use a while loop to generate and print the Fibonacci sequence up to the nth number,
 where n is provided by the user.'''
num=int(input("Enter the number:"))
a=0
b=1
count=0
while count<num:
    print(a)
    c=a+b
    a=b
    b=c
    count=count+1