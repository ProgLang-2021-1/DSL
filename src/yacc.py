import ply.yacc as yacc
from flex import tokens
from utils import internal
var = {}

def p_expression(p):
	"""expression : create
		| data
		| access
	"""
	p[0] = p[1]
	print('variables:\n', var)
	print('\tp[0]', p[0])

def p_expression_creation_treatments(p):
	"""create : NEW NAME OPENB treatments CLOSEB
	treatments : NAME SEP treatments
			| NAME"""
	global var
	if len(p) == 6:
		p[4].reverse()
		var[p[2]] = {'treatments': p[4],'patients': []}
	elif len(p) == 2:
		p[0] = [p[1]]
	elif len(p) == 4:
		# p[3] is treatments
		p[0] = p[3]
		p[0].append(p[1])

def p_expression_data(p):
	"""data : OPENB matrix CLOSEB IN NAME
		| OPENB arr CLOSEB IN NAME"""
	global var
	p[2].reverse()
	if p[5] in var:
		if type(p[2][0]) is list:
			for patient in p[2]:
				patient.reverse()
				var[p[5]]['patients'].append(patient)
		else:
			var[p[5]]['patients'].append(p[2])
	else:
		raise KeyError(f'"{p[5]}" does not exist')

def p_expression_matrix(p):
	"""matrix : OPENB arr CLOSEB SEP matrix
			| OPENB arr CLOSEB """
	
	if len(p) == 4:
		p[0] = [p[2]]
	else:
		p[0] = p[5]
		p[0].append(p[2])

def p_expression_arr(p):
	"""arr : NUM SEP arr
		| NUM
	"""
	if len(p) == 2:
		p[0] = [p[1]]
	else:
		# p[3] is data
		p[0] = p[3]
		p[0].append(p[1])

def p_expression_access(p):
	"""access : NAME OPENB NUM CLOSEB
		| NAME OPENB NUM CLOSEB DOT NAME
		| NAME DOT NAME
	"""
	global var
	

	# data[idx]
	if len(p) == 5:
		if type(p[3]) is int:
			p[0] = var[p[1]]['patients'][p[3]-1]
		else:
			raise TypeError('Index must be integer')

	# data[idx].treatment_name
	elif len(p) == 7:
		treatment_index = var[p[1]]['treatments'].index(p[6])
		if type(p[3]) is int:
			p[0] = var[p[1]]['patients'][p[3]-1][treatment_index]
		else:
			raise TypeError('Index must be integer')

	# data.treatment_name
	elif len(p) == 4:
		treatment_index = var[p[1]]['treatments'].index(p[3])
		p[0] = internal.transpose(var[p[1]])[treatment_index]

def p_error(p):
	if p:
		print("Syntax error at '%s'" % p.value, p)
	else:
		print("Syntax error at EOF")

parser = yacc.yacc(debug=True, start='expression')

if __name__ == '__main__':
	while True:
		try:
			s = input()
		except EOFError:
			break
		if not s: continue
		result = parser.parse(s)
		print(result)
