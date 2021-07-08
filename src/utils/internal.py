def transpose(data):
	return list(map(list, zip(*data['patients'])))

def range_of(matrix):
	import operator
	a = [ i for (i,j) in sorted(enumerate(matrix), key=operator.itemgetter(1))]
	# Should equal values be averaged?
	return [element for _, element in sorted(zip(a, range(1,len(a)+1)))]
