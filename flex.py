import ply.lex as lex

# List of token names. This is always required
tokens = [
	'NUM',
	'NEW',
	'NAME',
	'OPENB',
	'CLOSEB',
	'OP',
	'SEP',
	'RESERVED'
]


# Regular expression rules for simple tokens
t_ignore_COMMENT = r'(/\*(.|\n)*?\*/)|(//.*)'

t_OPENB  = r'\['
t_CLOSEB  = r'\]'
t_SEP = r','

t_OP = r'\+|\*'

t_RESERVED = r'\.(friedman|size|R|avg)'

def t_NAME(t: lex.LexToken):
	r'[a-zA-Z](\w|\d)*'
	if t.value == 'new':
		t.type = 'NEW'
	return t


# A regular expression rule with some action code
def t_NUM(t: lex.LexToken):
	r'-?\d+(\.\d+)?([eE][+-]?\d+)?'
	t.value = float(t.value)
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