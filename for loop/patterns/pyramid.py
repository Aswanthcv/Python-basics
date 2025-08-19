'''
        *
      * * *
    * * * * *
  * * * * * * * 
* * * * * * * * *
'''
row=5
for i in range(1,row+1):
    space=row-i
    print(" "*space,"*"*(2 * i - 1))

#for i in range(1,6) 
# i=1
# space=5-1=4
# " "*4 + "*" * (2 * 1 - 1)   

row=5
for i in range(row-1,0,-1):
    space=row-i
    print(" "*space,"*"*(2 * i - 1))