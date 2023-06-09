def find_elements(lst):
	smallest = min(lst)
	largest = max(lst)
	lst.remove(smallest)
	lst.remove(largest)
	second_smallest = min(lst)
	second_largest = max(lst)
	return smallest, largest, second_smallest, second_largest
lst=[12, 45, 2, 41, 31, 10, 8, 6, 4]
print(find_elements(lst))

