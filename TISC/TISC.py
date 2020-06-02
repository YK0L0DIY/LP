from executionmemory import ExecutionMemory


class TISC:
    pc = 0
    sp = 0

    labels = {}
    instructions: list = []
    avaliation_stack = []
    execution_memory = ExecutionMemory()
    number_instructions = 0
    set_args = {}
    set_AL = 0

    def new_label(self, label):
        self.labels[label] = self.number_instructions

    def add_instruction(self, instruction):
        self.instructions.append(instruction)
        self.number_instructions = self.number_instructions + 1

    def print_instructions(self):
        print("\n_____Instructions memory_____")
        for count, inst in enumerate(self.instructions):
            inst.imprimir(count)

    def print_labels(self):
        print("\n_____Lables______")
        for x in self.labels:
            print(x, ': ', self.labels[x])

    def execute(self):
        self.pc = self.labels['program'] or 0
        while self.execution_memory.have_blocks():
            self.pc = self.pc + 1
            self.instructions[self.pc - 1].execute(self)

        return


class Instruction(object):

    def __init__(self, name=None, arg1=None, arg2=None):
        self.name = name
        self.arg1 = arg1
        self.arg2 = arg2

    def execute(self, TISC):
        return ''

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1) + ", " + str(self.arg2)

    def imprimir(self, count):
        print(str(count) + " " + self.__repr__())


class add(Instruction):

    def __init__(self, name='add'):
        super().__init__(name)

    def execute(self, TISC):
        # arg2 + arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 + arg1
        av_stack.append(res)

    def __repr__(self):
        return str(self.name)

    def imprimir(self, count):
        super().imprimir(count)


class sub(Instruction):

    def __init__(self, name='sub'):
        super().__init__(name)

    def execute(self, TISC):
        # arg2 - arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 - arg1
        av_stack.append(res)

    def __repr__(self):
        return str(self.name)

    def imprimir(self, count):
        super().imprimir(count)


class mult(Instruction):

    def __init__(self, name='mult'):
        super().__init__(name)

    def execute(self, TISC):
        # arg2 * arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 * arg1
        av_stack.append(res)

    def __repr__(self):
        return str(self.name)

    def imprimir(self, count):
        super().imprimir(count)


class div(Instruction):

    def __init__(self, name='div'):
        super().__init__(name)

    def execute(self, TISC):
        # arg2 / arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 / arg1
        av_stack.append(int(res))

    def __repr__(self):
        return str(self.name)

    def imprimir(self, count):
        super().imprimir(count)


class mod(Instruction):

    def __init__(self, name='mod'):
        super().__init__(name)

    def execute(self, TISC):
        # arg2 % arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 % arg1
        av_stack.append(res)

    def __repr__(self):
        return str(self.name)

    def imprimir(self, count):
        super().imprimir(count)


class exp(Instruction):

    def __init__(self, name='exp'):
        super().__init__(name)

    def execute(self, TISC):
        # arg2 ** arg1, nd arg1=1º elemento da pilha e arg2=2ºelemento da pilha
        av_stack = TISC.avaliation_stack
        arg1 = av_stack.pop()
        arg2 = av_stack.pop()
        res = arg2 ** arg1
        av_stack.append(res)

    def __repr__(self):
        return str(self.name)

    def imprimir(self, count):
        super().imprimir(count)


class push_int(Instruction):

    def __init__(self, name='push_int', arg1=None):
        super().__init__(name, arg1)

    def execute(self, TISC):
        # envia para a pilha
        av_stack = TISC.avaliation_stack
        av_stack.append(self.arg1)

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1)

    def imprimir(self, count):
        super().imprimir(count)


class set_arg(Instruction):

    def __init__(self, name='set_arg', arg1=None):
        super().__init__(name, arg1)

    def execute(self, TISC):
        value = TISC.avaliation_stack.pop()
        TISC.set_args[self.arg1] = value

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1)

    def imprimir(self, count):
        super().imprimir(count)


class jump(Instruction):

    def __init__(self, name='jump', arg1=None):
        super().__init__(name, arg1)

    def execute(self, TISC):
        TISC.pc = TISC.labels[self.arg1]

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1)

    def imprimir(self, count):
        super().imprimir(count)


class jeq(Instruction):

    def __init__(self, name='jeq', arg1=None):
        super().__init__(name, arg1)

    def execute(self, TISC):
        value1 = TISC.avaliation_stack.pop()
        value2 = TISC.avaliation_stack.pop()
        if value1 == value2:
            TISC.pc = TISC.labels[self.arg1]

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1)

    def imprimir(self, count):
        super().imprimir(count)


class jlt(Instruction):

    def __init__(self, name='jlt', arg1=None):
        super().__init__(name, arg1)

    def execute(self, TISC):
        value1 = TISC.avaliation_stack.pop()
        value2 = TISC.avaliation_stack.pop()
        if value1 > value2:
            TISC.pc = TISC.labels[self.arg1]

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1)

    def imprimir(self, count):
        super().imprimir(count)


class print_str(Instruction):

    def __init__(self, name='print_str', arg1=None):
        super().__init__(name, arg1)

    def execute(self, TISC):
        print(self.arg1.replace('"', ''), end='')
        return

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1)

    def imprimir(self, count):
        super().imprimir(count)


class push_var(Instruction):

    def __init__(self, name='push_var', arg1=None, arg2=None):
        super().__init__(name, arg1, arg2)

    def execute(self, TISC):
        # coloca na pilha a variavel mº arg2 no bloco com distancia arg1
        value = TISC.execution_memory.get_value_var(TISC.sp, self.arg1, self.arg2)
        TISC.avaliation_stack.append(value)

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1) + ", " + str(self.arg2)

    def imprimir(self, count):
        super().imprimir(count)


class push_arg(Instruction):

    def __init__(self, name='push_arg', arg1=None, arg2=None):
        super().__init__(name, arg1, arg2)

    def execute(self, TISC):
        value = TISC.execution_memory.get_value_arg(TISC.sp, self.arg1, self.arg2)
        TISC.avaliation_stack.append(value)

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1) + ", " + str(self.arg2)

    def imprimir(self, count):
        super().imprimir(count)


class store_var(Instruction):

    def __init__(self, name='store_var', arg1=None, arg2=None):
        super().__init__(name, arg1, arg2)

    def execute(self, TISC):
        value = TISC.avaliation_stack.pop()
        TISC.execution_memory.store_value_var(TISC.sp, self.arg1, self.arg2, value)

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1) + ", " + str(self.arg2)

    def imprimir(self, count):
        super().imprimir(count)


class store_arg(Instruction):

    def __init__(self, name='store_arg', arg1=None, arg2=None):
        super().__init__(name, arg1, arg2)

    def execute(self, TISC):
        value = TISC.avaliation_stack.pop()
        TISC.execution_memory.store_value_arg(TISC.sp, self.arg1, self.arg2, value)

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1) + ", " + str(self.arg2)

    def imprimir(self, count):
        super().imprimir(count)


class call(Instruction):

    def __init__(self, name='call', arg1=None, arg2=None):
        super().__init__(name, arg1, arg2)

    def execute(self, TISC):
        sp = TISC.sp
        TISC.sp = TISC.execution_memory.new_block()
        TISC.execution_memory.set_CL(TISC.sp, sp)
        TISC.execution_memory.set_ER(TISC.sp, TISC.pc)
        TISC.pc = TISC.labels[self.arg2]

        if self.arg1 == -1:
            TISC.set_AL = sp
        elif self.arg1 >= 0:
            TISC.set_AL = TISC.execution_memory.get_correct_AL(sp, self.arg1)

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1) + ", " + str(self.arg2)

    def imprimir(self, count):
        super().imprimir(count)


class f_locals(Instruction):

    def __init__(self, name='locals', arg1=None, arg2=None):
        super().__init__(name, arg1, arg2)

    def execute(self, TISC):
        TISC.execution_memory.set_number_of_vars(TISC.sp, self.arg2)
        TISC.execution_memory.set_number_of_args(TISC.sp, self.arg1, TISC.set_args)
        TISC.execution_memory.set_AL(TISC.sp, TISC.set_AL)
        TISC.set_args = {}

    def __repr__(self):
        return str(self.name) + ", " + str(self.arg1) + ", " + str(self.arg2)

    def imprimir(self, count):
        super().imprimir(count)


class f_return(Instruction):

    def __init__(self, name='return'):
        super().__init__(name)

    def execute(self, TISC):
        TISC.pc = TISC.execution_memory.get_ER(TISC.sp)
        TISC.sp = TISC.execution_memory.drop_block(TISC.sp)

    def __repr__(self):
        return str(self.name)

    def imprimir(self, count):
        super().imprimir(count)


class f_print(Instruction):

    def __init__(self, name='print'):
        super().__init__(name)

    def execute(self, TISC):
        value = TISC.avaliation_stack.pop()
        print(value, end='')

    def __repr__(self):
        return str(self.name)

    def imprimir(self, count):
        super().imprimir(count)


class f_printnl(Instruction):

    def __init__(self, name='print_nl'):
        super().__init__(name)

    def execute(self, TISC):
        print('')
        return

    def __repr__(self):
        return str(self.name)

    def imprimir(self, count):
        super().imprimir(count)
