row=5
for i in range(row):
    for j in range(row):
        if (j == 0)or (j == 4) or (i==2 and j!=1 and j!=3) or ( i==3 and j!=2 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            