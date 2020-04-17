class TISC:
    pc = 0
    sp = 0

    vars = []
    instructions = []

    def new_instruction(self, Instruction):
        self.instructions.append(Instruction)


class Instruction(object):

    def __init__(self, label=None, name=None, arg1=None, arg2=None):
        self.label = label
        self.name = name
        self.arg1 = arg1
        self.arg2 = arg2
        #print(f'lable:{self.label},name:{self.name},arg1:{self.arg1},arg2:{self.arg2}')

    def __repr__(self):
        return f'{self.label},{self.name},{self.arg1},{self.arg2}'

