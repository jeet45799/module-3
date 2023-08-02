my_dict = {'apple': 5, 'banana': 2, 'orange': 7, 'peach': 1}


sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))

print(sorted_dict)
