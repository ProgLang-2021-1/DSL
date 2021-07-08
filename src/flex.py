import ply.lex as lex

# List of token names. This is always required
tokens = [
	'NUM',
	'NEW',
	'NAME',
	'OPENB',
	'CLOSEB',
	'OPENP',
	'CLOSEP',
	'SEP',
	'DOT',
	'IN',
	'RESERVED'
]


# Regular expression rules for simple tokens
t_ignore_COMMENT = r'(/\*(.\r?\n)*?\*/)|(//.*)'

t_OPENB  = r'\['
t_CLOSEB  = r'\]'
t_OPENP  = r'\('
t_CLOSEP  = r'\)'

t_SEP = r','
t_DOT = r'\.'

t_IN = r'->'

def t_NAME(t: lex.LexToken):
	r'[a-zA-Z](\w|\d)*'
	import re
	if t.value == 'new':
		t.type = 'NEW'
	elif re.match(r'(friedman|size|range|avg)', t.value):
		t.type = 'RESERVED'
	elif re.match(r'in', t.value):
		t.type = 'IN'
	return t


# A regular expression rule with some action code
def t_NUM(t: lex.LexToken):
	r'-?\d+(\.\d+)?([eE][+-]?\d+)?'
	if '.' in t.value:
		t.value = float(t.value)
	else:
		t.value = int(t.value)
	return t

# Define a rule so we can track line numbers
def t_newline(t: lex.LexToken):
	r'\n+'
	t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t: lex.LexToken):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

# EOF handling rule
# def t_eof(t: lex.LexToken):
# 	# Get more input (Example)
# 	more = input('... ')
# 	if more:
# 		t.lexer.input(more)
# 		return t.lexer.token()
# 	return None

# Build the lexer
lexer = lex.lex()


if __name__ == '__main__':
	# Give the lexer some input
	lexer.input(input("> "))

	# Tokenize
	while True:
		tok = lexer.token()
		if not tok:
			break      # No more input
		print(tok)