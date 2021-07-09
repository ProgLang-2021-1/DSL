from src.yacc import parse_string

def parse_file(filename: str, display=True):
	with open(filename, 'r') as f:
		for line in f:
			parse_string(line, display)

if __name__ == '__main__':
	from sys import argv
	if len(argv) > 1:
		parse_file('testing/tests/' + argv[1], display=True)
	else:
		print('\nUsage:', argv[0],'filename', 'display')
		print('\tfilename: must be a path to a file located at ./testing/tests')
		print("\tdisplay: it should be either true or false and it determines whether to display the input or not.\n\t\tBy default true.")