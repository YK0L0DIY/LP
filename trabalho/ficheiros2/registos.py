import ply.yacc as yacc
# import pprint
from trabalho.ficheiros2.tekens import tokens

from trabalho.ficheiros2.TISC import TISC, Instruction

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
