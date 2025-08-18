#Write a program to display the Fibonacci series up to 10 terms using a for loop.
num=10
a=0
b=1
for i in range(num):
    print(a)
    c=a
    a=b
    b=c+b
