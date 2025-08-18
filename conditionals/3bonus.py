#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount

salary=int(input("Enter your salary: "))
year=float(input("Year of experience: "))
current_sal=salary
if year>=5:
    bonus=salary * 0.05
    salary=bonus+salary
    print("Salary after bonus:",salary)
else:
    print("No hike in the currect salary ",current_sal)

