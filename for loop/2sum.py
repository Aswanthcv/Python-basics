#Create a program that calculates the sum of all numbers from 1 to a given number using a for loop.
num_range=int(input("Enter number range: "))
sum=0
for i in range(1,num_range+1):
    sum=sum+i
print(sum)
