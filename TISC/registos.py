import ply.yacc as yacc
import argparse
from tekens import tokens

from TISC import *

tisc = TISC()


# para verificar linha a linha
def p_programa(t):
    'programa : programa etiqueta instrucao '
    pass


def p_prgram_empty(t):
    'programa : '
    pass


# criar uma label para os jumps e funcoes
def p_etiqueta(p):
    '''etiqueta : IDENTIFICADOR DOIS_PONTOS'''

    p[0] = tisc.new_label(p[1])


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

    if p[1] == 'add':
        tisc.add_instruction(add())
    elif p[1] == 'sub':
        tisc.add_instruction(sub())
    elif p[1] == 'mult':
        tisc.add_instruction(mult())
    elif p[1] == 'div':
        tisc.add_instruction(div())
    elif p[1] == 'mod':
        tisc.add_instruction(mod())
    elif p[1] == 'exp':
        tisc.add_instruction(exp())
    elif p[1] == 'return':
        tisc.add_instruction(f_return())
    elif p[1] == 'print':
        tisc.add_instruction(f_print())
    elif p[1] == 'print_nl':
        tisc.add_instruction(f_printnl())
    else:
        pass


def p_instrucao_arg1(p):
    '''instrucao :  PUSH_INT INTEIRO
                |   SET_ARG INTEIRO
                |   JUMP IDENTIFICADOR
	            |   JEQ IDENTIFICADOR
	            |   JLT IDENTIFICADOR
	            |   PRINT_STR STRING'''

    if p[1] == 'push_int':
        tisc.add_instruction(push_int(arg1=p[2]))
    elif p[1] == 'set_arg':
        tisc.add_instruction(set_arg(arg1=p[2]))
    elif p[1] == 'jump':
        tisc.add_instruction(jump(arg1=p[2]))
    elif p[1] == 'jeq':
        tisc.add_instruction(jeq(arg1=p[2]))
    elif p[1] == 'jlt':
        tisc.add_instruction(jlt(arg1=p[2]))
    elif p[1] == 'print_str':
        tisc.add_instruction(print_str(arg1=p[2]))


def p_instrucao_arg2(p):
    '''instrucao : PUSH_VAR INTEIRO INTEIRO
              |   PUSH_ARG INTEIRO INTEIRO
              |   STORE_VAR INTEIRO INTEIRO
              |   STORE_ARG INTEIRO INTEIRO
              |   CALL INTEIRO IDENTIFICADOR
              |   LOCALS INTEIRO INTEIRO'''

    if p[1] == 'push_var':
        tisc.add_instruction(push_var(arg1=p[2], arg2=p[3]))
    elif p[1] == 'push_arg':
        tisc.add_instruction(push_arg(arg1=p[2], arg2=p[3]))
    elif p[1] == 'store_var':
        tisc.add_instruction(store_var(arg1=p[2], arg2=p[3]))
    elif p[1] == 'store_arg':
        tisc.add_instruction(store_arg(arg1=p[2], arg2=p[3]))
    elif p[1] == 'call':
        tisc.add_instruction(call(arg1=p[2], arg2=p[3]))
    elif p[1] == 'locals':
        tisc.add_instruction(f_locals(arg1=p[2], arg2=p[3]))


def p_error(p):
    print('Syntax error')


def main(print_inst, print_labels, filepath=None):
    parser = yacc.yacc()
    if not filepath:
        filepath = input('Path to the file:')

    with open(filepath) as fp:
        parser.parse(fp.read())

    if print_inst:
        tisc.print_instructions()
    if print_labels:
        tisc.print_labels()

    tisc.execute()
