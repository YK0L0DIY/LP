from collections import deque


class TISC:
    pc = 0
    sp = 0

    vars = []
    instructions = dict()
    avaliation_stack = deque()

    block = ''
    i = 0

    def execute(self, Instruction):
        if Instruction.label != None:
            self.block = Instruction.label
            self.instructions[self.block] = dict()
            self.i = 1
        else:
            self.instructions[self.block][self.i] = Instruction.get_instruction()
            self.i = self.i + 1


class Instruction(object):

    def __init__(self, label=None, name=None, arg1=None, arg2=None):
        self.label = label
        self.name = name
        self.arg1 = arg1
        self.arg2 = arg2

    def execute(self):
        return ''

    def get_label(self):
        return self.label

    def get_instruction(self):
        return str(self.name) + ", " + str(self.arg1) + ", " + str(self.arg2)


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

    def __init__(self, label=None, name='push_var', arg1=None, arg2=None):
        self.label = label
        self.name = name
        self.arg1 = arg1
        self.arg2 = arg2

    def execute(self):
        # coloca na pilha a variavel mº arg2 no bloco com distancia arg1
        av_stack = TISC.avaliation_stack
        av_stack.append()
