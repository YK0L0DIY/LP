class TISC:
    pc = 0
    sp = 0

    labels = {}
    instructions = []
    avaliation_stack = []
    number_instructions = 0

    block = ''
    i = 0

    def new_label(self, label):
        self.labels[label] = self.number_instructions

    def add_instruction(self, instruction):
        self.instructions.append(instruction)
        self.number_instructions = self.number_instructions + 1

    def print_instructions(self):
        print("\n_____Instructions memory_____")
        for count, x in enumerate(self.instructions):
            print(count, x)

    def print_labels(self):
        print("\n_____Lables______")
        for x in self.labels:
            print(x, ': ', self.labels[x])

    def execute(self, Instruction):
        '''TO IMPLEMENT'''
        return


class Instruction(object):

    def __init__(self, name=None, arg1=None, arg2=None):
        self.name = name
        self.arg1 = arg1
        self.arg2 = arg2

    def execute(self):
        return ''

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1) + ", " + str(self.arg2)


class add(Instruction):

    def __init__(self, name='add'):
        super().__init__(name)

    def execute(self):
        # arg2 + arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 + arg1
        av_stack.append(res)


class sub(Instruction):

    def __init__(self, name='sub'):
        super().__init__(name)

    def execute(self):
        # arg2 - arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 - arg1
        av_stack.append(res)


class mult(Instruction):

    def __init__(self, name='mult'):
        super().__init__(name)

    def execute(self):
        # arg2 * arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 * arg1
        av_stack.append(res)


class div(Instruction):

    def __init__(self, name='div'):
        super().__init__(name)

    def execute(self):
        # arg2 / arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 / arg1
        av_stack.append(res)


class mod(Instruction):

    def __init__(self, name='mod'):
        super().__init__(name)

    def execute(self):
        # arg2 % arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 % arg1
        av_stack.append(res)


class exp(Instruction):

    def __init__(self, name='exp'):
        super().__init__(name)


    def execute(self):
        # arg2 ** arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 ** arg1
        av_stack.append(res)


class push_int(Instruction):

    def __init__(self, name='push_int', arg1=None):
        super().__init__(name, arg1)

    def execute(self):
        # envia para a pilha
        av_stack = TISC.avaliation_stack
        av_stack.append(self.arg1)


class set_arg(Instruction):

    def __init__(self, name='set_arg', arg1=None):
        super().__init__(name, arg1)

    def execute(self):
        '''TO IMPLEMENT'''
        return


class jump(Instruction):

    def __init__(self, name='jump', arg1=None):
        super().__init__(name, arg1)

    def execute(self):
        '''TO IMPLEMENT'''
        return


class jeq(Instruction):

    def __init__(self, name='jeq', arg1=None):
        super().__init__(name, arg1)

    def execute(self):
        '''TO IMPLEMENT'''
        return


class jlt(Instruction):

    def __init__(self, name='jlt', arg1=None):
        super().__init__(name, arg1)

    def execute(self):
        '''TO IMPLEMENT'''
        return


class print_str(Instruction):

    def __init__(self, name='print_str', arg1=None):
        super().__init__(name, arg1)

    def execute(self):
        '''TO IMPLEMENT'''
        return


class push_var(Instruction):

    def __init__(self, name='push_var', arg1=None, arg2=None):
        super().__init__(name, arg1, arg2)

    def execute(self):
        # coloca na pilha a variavel mº arg2 no bloco com distancia arg1
        av_stack = TISC.avaliation_stack
        av_stack.append()


class push_arg(Instruction):

    def __init__(self, name='push_arg', arg1=None, arg2=None):
        super().__init__(name, arg1, arg2)

    def execute(self):
        '''TO IMPLEMENT'''
        return


class store_var(Instruction):

    def __init__(self, name='store_var', arg1=None, arg2=None):
        super().__init__(name, arg1, arg2)

    def execute(self):
        '''TO IMPLEMENT'''
        return


class store_arg(Instruction):

    def __init__(self, name='store_arg', arg1=None, arg2=None):
        super().__init__(name, arg1, arg2)

    def execute(self):
        '''TO IMPLEMENT'''
        return


class call(Instruction):

    def __init__(self, name='call', arg1=None, arg2=None):
        super().__init__(name, arg1, arg2)

    def execute(self):
        '''TO IMPLEMENT'''
        return


class f_locals(Instruction):

    def __init__(self, name='locals', arg1=None, arg2=None):
        super().__init__(name, arg1, arg2)

    def execute(self):
        '''TO IMPLEMENT'''
        return


class f_return(Instruction):

    def __init__(self, name='return'):
        super().__init__(name)

    def execute(self):
        '''TO IMPLEMENT'''
        return


class f_print(Instruction):

    def __init__(self, name='print'):
        super().__init__(name)

    def execute(self):
        '''TO IMPLEMENT'''
        return


class f_printnl(Instruction):

    def __init__(self, name='print_nl'):
        super().__init__(name)

    def execute(self):
        '''TO IMPLEMENT'''
        return
