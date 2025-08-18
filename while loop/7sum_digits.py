# Write a program that calculates the sum of digits of a given number using a while loop.
num=int(input("Enter a number: "))
sum=0
while num > 0:
    digit = num % 10
    sum+=digit
    num=num//10
print("sum of digits is: ",sum)        