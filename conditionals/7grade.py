'''
A school has following rules for grading system
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.'''

mark=float(input("Enter Your mark: "))
if 0<=mark<=100:
    if mark<25:
        print("Grade:F")
    elif 25<=mark<45:
        print("Grade:E") 
    elif 45<=mark<50:
        print("Grade:D")
    elif 50<=mark<60:
        print("Grade:C")
    elif 60<=mark<80:
        print("Grade:B")            
    else:
        print("Grade A")
else:
    print("Invalid input")        