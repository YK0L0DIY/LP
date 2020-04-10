import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'ADD',
    'SUB',
    'MULT',
    'DIV',
    'MOD',
    'EXP',

    'PUSH_INT',
    'PUSH_VAR',
    'PUSH_ARG',

    'STORE_VAR',
    'STORE_ARG',

    'SET_ARG',
    'CALL',
    'LOCALS',
    'RETURN',

    'JUMP',
    'JEQ',
    'JLT',

    'PRINT',
    'PRINT_STR',
    'PRINT_NL',

    'IDENTIFICADOR',
    'DOIS_PONTOS',

    'INTEIRO',

    'STRING',

    'ERRO',
    'BRANCOS',
    'COMENTARIO',
)

t_ADD = r'add'
t_SUB = r'sub'
t_MULT = r'mult'
t_DIV = r'div'
t_MOD = r'mod'
t_EXP = r'exp'

t_PUSH_INT = r'push_int'
t_PUSH_VAR = r'push_var'
t_PUSH_ARG = r'push_arg'

t_STORE_VAR = r'store_var'
t_STORE_ARG = r'store_arg'

t_SET_ARG = r'set_arg'
t_CALL = r'call'
t_LOCALS = r'locals'
t_RETURN = r'return'

t_JUMP = r'jump'
t_JEQ = r'jeq'
t_JLT = r'jlt'

t_PRINT = r'print'
t_PRINT_STR = r'print_str'
t_PRINT_NL = r'print_nl'


def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.value = str(t.value)
    return t


t_DOIS_PONTOS = r':'


def t_INTEIRO(t):
    r'-?[0-9]+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'\"(\\[\\\"]|[^\"\\])*\"'
    t.value = str(t.value)
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_BRANCOS = r'[\ \n\t]'
t_COMENTARIO = r'\#.*'

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
program:locals 0 0
	push_int 10
	set_arg 1
	call -1 fact	# calcula fact(10)
	print		# e imprime
	print_nl
	return

fact:	locals 1 2
	push_int 1
	store_var 0 2	# f = 1
	push_int 1
	store_var 0 1	# i = 1
L1:	push_arg 0 1
	push_var 0 1
	jlt L2		# n < i
	push_var 0 2
	push_var 0 1
	mult
	store_var 0 2	# f = f * i
	push_var 0 1
	push_int 1
	add
	store_var 0 1	# i = i + 1
	jump L1
L2:	push_var 0 2
	return		# return f

'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
