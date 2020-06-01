class ExecutionMemory:
    stack = []

    def __init__(self):
        self.new_block()

    def new_block(self):
        self.stack.append(None)  # CL
        self.stack.append(None)  # AL
        self.stack.append(None)  # ER
        self.stack.append(None)  # number of Vars
        self.stack.append(None)  # number of Args
        return len(self.stack) - 5

    def set_CL(self, pos, value):
        self.stack[pos] = value

    def set_AL(self, pos, value):
        self.stack[pos + 1] = value

    def set_ER(self, pos, value):
        self.stack[pos + 2] = value

    def set_number_of_vars(self, pos, value):
        self.stack[pos + 3] = value
        self.create_n_spaces(value)

    def set_number_of_args(self, pos, value, args):
        self.stack[pos + 4] = value
        self.create_n_spaces(value)
        for key, value in args.items():
            self.set_arg(pos, key, value)

    def set_var(self, pos, var, value):
        self.stack[pos + 4 + var] = value

    def set_arg(self, pos, arg, value):
        number_of_vars = self.get_number_of_vars(pos)
        self.stack[pos + 4 + number_of_vars + arg] = value

    def get_CL(self, pos):
        return self.stack[pos]

    def get_AL(self, pos):
        return self.stack[pos + 1]

    def get_ER(self, pos):
        return self.stack[pos + 2]

    def get_number_of_vars(self, pos):
        return self.stack[pos + 3]

    def get_number_of_args(self, pos):
        return self.stack[pos + 4]

    def get_var(self, pos, var):
        return self.stack[pos + 4 + var]

    def get_arg(self, pos, arg):
        number_of_vars = self.get_number_of_vars(pos)
        return self.stack[pos + 4 + number_of_vars + arg]

    def create_n_spaces(self, number_of_spaces):
        for index in range(number_of_spaces):
            self.stack.append(None)

    def drop_n_spaces(self, number_of_spaces):
        for index in range(number_of_spaces):
            self.stack.pop()

    def drop_block(self, pos):
        self.drop_n_spaces(self.get_number_of_args(pos))  # drop Args
        self.drop_n_spaces(self.get_number_of_vars(pos))  # drop Vars
        self.stack.pop()  # drop number of Args
        self.stack.pop()  # drop number of Vars
        self.stack.pop()  # drop ER
        self.stack.pop()  # drop AL
        return self.stack.pop()  # drop CL

    def get_value_var(self, pos, distance, var):
        if distance == 0:
            return self.get_var(pos, var)
        else:
            previous_block = self.get_CL(pos)
            return self.get_value_var(previous_block, distance - 1, var)

    def store_value_var(self, pos, distance, var, value):
        if distance == 0:
            return self.set_var(pos, var, value)
        else:
            previous_block = self.get_CL(pos)
            return self.store_value_var(previous_block, distance - 1, var, value)

    def get_value_arg(self, pos, distance, arg):
        if distance == 0:
            return self.get_arg(pos, arg)
        else:
            previous_block = self.get_CL(pos)
            return self.get_value_arg(previous_block, distance - 1, arg)

    def store_value_arg(self, pos, distance, arg, value):
        if distance == 0:
            return self.set_arg(pos, arg, value)
        else:
            previous_block = self.get_CL(pos)
            return self.store_value_arg(previous_block, distance - 1, arg, value)

    def have_blocks(self):
        if len(self.stack) != 0:
            return True
        else:
            return False
