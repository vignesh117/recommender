def flatten(l):
	flattened = []
	if type(l) != list:
		return [l]
	elif len(l) in [0]:
		return l
	else:
		for x in l:
			flattened+=(flatten(x))
	return flattened
