# Create a while loop that checks whether a number is prime.
num = int(input("Enter your number: "))
i = 2

if num <= 1:
    print("Not a prime number.")
else:
    while i <= num // 2:
        if num % i == 0:
            print("not a prime")    
            break
        i = i + 1
    else:
        print("number is Prime")
