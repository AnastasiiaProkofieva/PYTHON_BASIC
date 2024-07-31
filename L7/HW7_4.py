def common_elements():
	lst1 = []
	lst2 = []
	for n in range(100):
		if n % 3 == 0:
			lst1.append(n)
		if n % 5 == 0:
			lst2.append(n)
		n += 1

	set1 = set(lst1)
	set2 = set(lst2)
	set_new = set1.intersection(set2)
	return set_new


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')
