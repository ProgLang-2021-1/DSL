import ply.yacc as yacc
from flex import tokens
from utils import internal
var = {}

def p_expression(p):
	"""expression :
		| create
		| insertion
		| access
	"""
	if len(p) > 1:
		p[0] = p[1]['exec']
		p[1]['exec'] = p[1]['patients']


def p_expression_creation_treatments(p):
	"""create : NEW NAME OPENB treatments CLOSEB
	treatments : treatments SEP NAME
			| NAME"""
	global var
	if len(p) == 6:
		var[p[2]] = {'treatments': p[4],'patients': [],'exec': []}
		p[0] = var[p[2]]
		p[0]['exec'] = p[0]['treatments']

	# treatments
	elif len(p) == 2:
			p[0] = [p[1]]
	elif len(p) == 4:
		# p[1] is treatments
		p[0] = p[1]
		p[0].append(p[3])

def p_expression_insertion(p):
	"""insertion : OPENB matrix CLOSEB IN NAME
		| OPENB arr CLOSEB IN NAME"""
	global var
	if p[5] in var:
		if type(p[2][0]) is list:
			for patient in p[2]:
				var[p[5]]['patients'].append(patient)
		else:
			var[p[5]]['patients'].append(p[2])
		p[0] = var[p[5]]

		# exec must be equal to patients by default
		var[p[5]]['exec'] = p[0]['patients']
	else:
		raise KeyError(f'{p[5]} does not exist')

def p_expression_matrix(p):
	"""matrix : matrix SEP OPENB arr CLOSEB
			| OPENB arr CLOSEB """

	if len(p) == 4:
		p[0] = [p[2]]
	else:
		p[0] = p[1]
		p[0].append(p[4])

def p_expression_arr(p):
	"""arr : arr SEP NUM
		| NUM
	"""
	if len(p) == 2:
		p[0] = [p[1]]
	else:
		# p[1] is arr
		p[0] = p[1]
		p[0].append(p[3])

def p_expression_access(p):
	"""access : other OPENB NUM CLOSEB
		| other OPENB NUM CLOSEB DOT NAME
		| other DOT NAME
		| other
	"""
	global var

	# Important: p[1] is an instance of var

	# other[idx]
	if len(p) == 5:
		if type(p[3]) is int:
			p[1]['exec'] = p[1]['exec'][p[3]-1]
			p[0] = p[1]
		else:
			raise TypeError('Index must be integer')

	# other[idx].treatment_name
	elif len(p) == 7:
		treatment_index = p[1]['treatments'].index(p[6])
		if type(p[3]) is int:
			p[1]['exec'] = p[1]['exec'][p[3]-1][treatment_index]
			p[0] = p[1]
		else:
			raise TypeError('Index must be integer')

	# other.treatment_name
	elif len(p) == 4:
		treatment_index = p[1]['treatments'].index(p[3])
		p[1]['exec'] = internal.transpose(p[1]['exec'])[treatment_index]
		p[0] = p[1]

	elif len(p) == 2:
		p[0] = p[1]


def p_expression_other(p):
	"""other : NAME
		 | function
			"""
	if type(p[1]) is str:
		var[p[1]]['exec'] = var[p[1]]['patients']
		p[0] = var[p[1]]
	else:
		p[0] = p[1]

def p_expression_function(p):
	"""function : RESERVED OPENP access CLOSEP"""
	global var
	# p[3] must be an instance of var
	if type(p[3]['exec']) is int or type(p[3]['exec']) is float:
		raise TypeError('Value in function cannot be a number')

	if p[1] in internal.functions.keys():
		p[3]['exec'] = internal.functions[p[1]](p[3]['exec'])

	p[0] = p[3]

def p_error(p):
	if p:
		print("Syntax error at '%s'" % p.value, p)
	else:
		print("Syntax error at EOF")

parser = yacc.yacc(debug=True, start='expression')

if __name__ == '__main__':
	display = True
	while True:
		try:
			s = input()
		except EOFError:
			break
		if not s: continue
		try:
			result = parser.parse(s)
			if result is not None:
				if display:
					print(">", s, '\n---->', result, end='\n\n')
				else:
					print(result)
		except Exception as e:
			print(">", s, '\n****>', e, end='\n\n')
