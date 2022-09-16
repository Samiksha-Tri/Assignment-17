"""Write a python program to add elements of list to a set
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]"""

thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
print("old set :",thisset)
for e in mylist:
    thisset.add(e)
print("new set :",thisset)    
