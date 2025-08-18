# Write a program that calculates the sum of all even numbers from 1 to 100 using a while loop.

num=1
sum=0
while num<=100:
    if num%2 == 0:
        sum=sum+num
    num=num+1
print("sum:",sum)            