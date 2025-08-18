# Write a while loop that calculates the factorial of a given number
num=int(input("Enter number: "))
fact=1
while num>0:
    fact=fact*num
    num=num-1
print("Factorial is, ",fact)    