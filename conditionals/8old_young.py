age1 = int(input("Enter First age: "))
age2 = int(input("Enter Second age: "))
age3 = int(input("Enter Third age: "))

if age1 <= 0 or age2 <= 0 or age3 <= 0:
    print("Enter valid ages (greater than 0)")
else:
    if age1 > age2 and age1 > age3:
        print("Person 1 is the oldest.")
    elif age2 > age1 and age2 > age3:
        print("Person 2 is the oldest.")
    elif age3 > age1 and age3 > age2:
        print("Person 3 is the oldest.")
    else:
        print("There is a tie for the oldest.")
 
    if age1 < age2 and age1 < age3:
        print("Person 1 is the youngest.")
    elif age2 < age1 and age2 < age3:
        print("Person 2 is the youngest.")
    elif age3 < age1 and age3 < age2:
        print("Person 3 is the youngest.")
    else:
        print("There is a tie for the youngest.")
