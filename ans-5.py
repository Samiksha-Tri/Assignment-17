"""Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}"""

thisset = {"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
print("old set :",thisset)
for e in secondset:
    thisset.add(e)
print("new set :",thisset)    

