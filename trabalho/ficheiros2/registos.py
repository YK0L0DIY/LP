import ply.lex as lex
import ply.yacc as yacc
#import pprint
import json
from LP.trabalho.ficheiros2.TISC import TISC, Instruction

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
    'COMENTARIO',
)


def t_ADD(t):
    'add'
    t.value = 'add'
    return t


def t_SUB(t):
    'sub'
    t.value = 'sub'
    return t


def t_MULT(t):
    'mult'
    t.value = 'mult'
    return t


def t_DIV(t):
    'div'
    t.value = 'div'
    return t


def t_MOD(t):
    'mod'
    t.value = 'mod'
    return t


def t_EXP(t):
    'exp'
    t.value = 'exp'
    return t


def t_PUSH_INT(t):
    'push_int'
    t.value = 'push_int'
    return t


def t_PUSH_VAR(t):
    'push_var'
    t.value = 'push_var'
    return t


def t_PUSH_ARG(t):
    'push_arg'
    t.value = 'push_arg'
    return t


def t_STORE_VAR(t):
    'store_var'
    t.value = 'store_var'
    return t


def t_STORE_ARG(t):
    'store_arg'
    t.value = 'store_arg'
    return t


def t_SET_ARG(t):
    'set_arg'
    t.value = 'set_arg'
    return t


def t_CALL(t):
    'call'
    t.value = 'call'
    return t


def t_LOCALS(t):
    'locals'
    t.value = 'locals'
    return t


def t_RETURN(t):
    'return'
    t.value = 'return'
    return t


def t_JUMP(t):
    'jump'
    t.value = 'jump'
    return t


def t_JEQ(t):
    'jeq'
    t.value = 'jeq'
    return 'jeq'


def t_JLT(t):
    'jlt'
    t.value = 'jlt'
    return t


def t_PRINT_NL(t):
    'print_nl'
    t.value = 'print_nl'
    return t


def t_PRINT_STR(t):
    r'print_str'
    t.value = 'print_str'
    return t


def t_PRINT(t):
    r'print'
    t.value = 'print'
    return t


def t_STRING(t):
    r'\"(\\[\\\"]|[^\"\\])*\"'
    t.value = str(t.value)
    return t


def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.value = str(t.value)
    return t


t_DOIS_PONTOS = r':'


def t_INTEIRO(t):
    r'-?[0-9]+'
    t.value = int(t.value)
    return t


# Error handling rule
def t_error(t):
    r'.'
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_ignore = '[ \n\t]'


# ignore comments
def t_COMENTARIO(t):
    r'\#.*'
    return


# Build the lexer
lexer = lex.lex()

tisc = TISC()

# para verificar linha a linha
def p_programa(t):
    'programa : programa etiqueta instrucao '
    pass
    # t[0] = Instruction(label=t[2])


def p_prgram_empty(t):
    'programa : '
    pass


# criar uma lable para os jumps e funcoes
def p_etiqueta(p):
    '''etiqueta : IDENTIFICADOR DOIS_PONTOS'''

    p[0] = Instruction(label=p[1])
    tisc.execute(p[0])


def p_etiqueta_empty(p):
    '''etiqueta : '''
    pass


def p_instrucao(p):
    '''instrucao :  ADD
                |   SUB
                |   MULT
                |   DIV
                |   MOD
                |   EXP
                |   RETURN
                |   PRINT
                |   PRINT_NL
                |   COMENTARIO'''

    p[0] = Instruction(name=p[1])
    tisc.execute(p[0])


def p_instrucao_arg1(p):
    '''instrucao :  PUSH_INT INTEIRO
                |   SET_ARG INTEIRO
                |   JUMP IDENTIFICADOR
	            |   JEQ IDENTIFICADOR
	            |   JLT IDENTIFICADOR
	            |   PRINT_STR STRING'''

    p[0] = Instruction(name=p[1], arg1=p[2])
    tisc.execute(p[0])


def p_instrucao_arg2(p):
    '''instrucao : PUSH_VAR INTEIRO INTEIRO
              |   PUSH_ARG INTEIRO INTEIRO
              |   STORE_VAR INTEIRO INTEIRO
              |   STORE_ARG INTEIRO INTEIRO
              |   CALL INTEIRO IDENTIFICADOR
              |   LOCALS INTEIRO INTEIRO'''

    p[0] = Instruction(name=p[1], arg1=p[2], arg2=p[3])
    tisc.execute(p[0])


def p_error(p):
    print('Syntax error')


def main():
    parser = yacc.yacc()
    filepath = input('Path to the file:')

    with open(filepath) as fp:
        for line in fp:
            parser.parse(line)
    for block, instr in tisc.instructions.items():
        print(block)
        for inst in instr.items():
            print(inst[1])

if __name__ == '__main__':
    main()