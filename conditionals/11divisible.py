num=int(input("Enter a number: "))
if num >0 and num%5==0:
    print("The number is positive and divisible by 5")
elif num>0 and num%5!=0:
    print("Positive but not divisible by 5")
elif num==0:
    print("The number is zero")
else:
    print("The number is Negative")        
