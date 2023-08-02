def Remove(tuples):
	for i in tuples:
		if(i==()):
			tuples.remove(i)
	return tuples

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
		('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))
