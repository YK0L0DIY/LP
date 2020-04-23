from collections import deque

class TISC:
    pc = 0
    sp = 0

    vars = []
    instructions = []
    avaliation_stack = deque()

    def execute(self, Instruction):
        self.instructions.append(Instruction)
        Instruction.execute()


class Instruction(object):

    def __init__(self, label=None, name=None, arg1=None, arg2=None):
        self.label = label
        self.name = name
        self.arg1 = arg1
        self.arg2 = arg2
        #print(f'lable:{self.label},name:{self.name},arg1:{self.arg1},arg2:{self.arg2}')

    #def __repr__(self):
    #    return f'{self.label},{self.name},{self.arg1},{self.arg2}'

    def execute(self):
        return ''

class add(Instruction):

    def __init__(self, label=None, name='add'):
        self.label = label
        self.name = name

    def execute(self):
        # arg2 + arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 + arg1
        av_stack.append(res)

class sub(Instruction):

    def __init__(self, label=None, name='sub'):
        self.label = label
        self.name = name

    def execute(self):
        # arg2 - arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 - arg1
        av_stack.append(res)

class mult(Instruction):

    def __init__(self, label=None, name='mult'):
        self.label = label
        self.name = name

    def execute(self):
        # arg2 * arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 * arg1
        av_stack.append(res)

class div(Instruction):

    def __init__(self, label=None, name='div'):
        self.label = label
        self.name = name

    def execute(self):
        # arg2 / arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 / arg1
        av_stack.append(res)

class mod(Instruction):

    def __init__(self, label=None, name='mod'):
        self.label = label
        self.name = name

    def execute(self):
        # arg2 % arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 % arg1
        av_stack.append(res)

class exp(Instruction):

    def __init__(self, label=None, name='exp'):
        self.label = label
        self.name = name

    def execute(self):
        # arg2 ** arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 ** arg1
        av_stack.append(res)

class push_int(Instruction):

    def __init__(self, label=None, name='push_int', arg1=None):
        self.label = label
        self.name = name
        self.arg1 = arg1

    def execute(self):
        # envia para a pilha
        av_stack = TISC.avaliation_stack
        av_stack.append(self.arg1)

class push_var(Instruction):

    def __init__(self, label = None, name = 'push_var', arg1 = None, arg2 = None):
        self.label = label
        self.name = name
        self.arg1 = arg1
        self.arg2 = arg2

    def execute(self):
        # coloca na pilha a variavel mº arg2 no bloco com distancia arg1
        av_stack = TISC.avaliation_stack
        av_stack.append()