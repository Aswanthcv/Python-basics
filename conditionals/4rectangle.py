side1=int(input("Enter side 1 : "))
side2=int(input("Enter side 2 : "))
if side1 >0 and side2 >0:
    if side1==side2:
        print("This is a square.")
    else:
        print("Just a Rectangle.")    
else:
    print("Enter a valid measurement!")