''' A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user Number of classes held Number of classes attended.
And print percentage of class attended Is student is allowed to sit in exam or not.
'''
total_class=int(input("Enter Total classes held: "))
attended=int(input("Enter classes attended: "))

if total_class<=0 or attended<0 or attended>total_class:
    print("Invalid input")
else:
    att_percentage=(attended/total_class) * 100
    print(f"Attendance percentage:{att_percentage:.2f}%")
    if att_percentage >=75:
        print("You are Allowed to sit in exams ")
    else:
        print("Not allowed")         