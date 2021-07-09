def transpose(data):
	return list(map(list, zip(*data)))

def range_of(data: list):
	from operator import itemgetter
	results = []

	is_array = type(data[0]) is not list
	if is_array:
		data = [data]

	for matrix in data:
		a = [ i for (i,j) in sorted(enumerate(matrix), key=itemgetter(1))]

		result = [element for _, element in sorted(zip(a, range(1,len(a)+1)))]

		current = None
		i = j = None
		for r in range(1,len(a)+1):
			if current is None:
				current = matrix[result.index(r)]
				i = j = r
				continue

			if current == matrix[result.index(r)]:
				j += 1
			else:
				if j - i > 0:
					val = avg_of([n for n in range(i,j+1)])
					for n in range(i,j+1):
						result[result.index(n)] = val
				current = matrix[result.index(r)]
				i = j = r

		if j - i > 0:
			val = avg_of([n for n in range(i,j+1)])
			for n in range(i,j+1):
				result[result.index(n)] = val
		results.append(result)
	return results if not is_array else results[0]

def avg_of(matrix: list):
	if type(matrix[0]) is list:
		return avg_of([avg_of(m) for m in matrix])
	else:
		return sum(matrix)/len(matrix)

def size_of(matrix):
	if type(matrix[0]) is list:
		return sum([len(m) for m in matrix])
	else:
		return len(matrix)

def friedman(variable: dict):
	n = len(variable['patients'])
	k = len(variable['treatments'])

	sum_R_sqrd = sum([ sum(r)**2 for r in transpose(range_of(variable['patients']))])

	return (12/(n*k*(k+1))*sum_R_sqrd) - 3*n*(k+1)

functions = {
	'range': range_of,
	'size' : size_of,
	'avg' : avg_of,
	'friedman': friedman,
}

