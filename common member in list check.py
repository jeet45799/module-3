def commonFunc(list1, list2):
	p_set = set(p)
	q_set = set(q)
	if len(p_set.intersection (q_set)) > 0:
		return True
	return False


p = [4, 10, 15, 20, 25, 30]
print("List1 = ",p)


q = [12, 24, 35, 45, 65]
print("List2 = ",q)

print("Are common elements in both the lists? :",commonFunc(p, q))
