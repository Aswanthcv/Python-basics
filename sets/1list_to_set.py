'''Given a Python set sample_set with elements {"Yellow", "Orange", "Black"} and a list sample_list
 containing ["Blue", "Green", "Red"],  write a program to add all the elements from the list into the set.'''

colors1={"Yellow", "Orange", "Black"}
colors2=["Blue", "Green", "Red"]
colors1.update(colors2)
print (colors1)