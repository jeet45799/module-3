#In Python, the difference between the append() and extend() method is that:

#The append() method adds a single element to the end of a list.
#The extend() method adds multiple items.

a = [1, 2, 3]
a.append(4)
print(a)

a = [1, 2, 3]
a.append([4, 5])
print(a)

a = [1, 2, 3]
a.extend([4, 5])
print(a)

a = [1, 2, 3]
a.extend("45")
print(a)
