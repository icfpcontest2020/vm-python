class Vm:
    def __init__(self) -> None:
        self.named_functions = {}
        self.builtin_constants = {
            'emptyList': None
        }

        def is_empty_list(a):
            if a is None:
                return 'K'
            if isinstance(a, tuple):
                return 'F'
            raise ValueError("{0} is of type {1}, but None or tuple is expected".format(a, type(a)))

        def assert_type(x, t):
            if isinstance(x, t):
                return x
            raise ValueError("{0} is of type {1}, but type {2} is expected".format(x, type(x), t))

        self.builtin_functions1 = {
            'negate': {'eval_args': True, 'apply': lambda a: -assert_type(a, int)},
            'isEmptyList': {'eval_args': True, 'apply': is_empty_list},
            'head': {'eval_args': True, 'apply': lambda a: assert_type(a, tuple)[0]},
            'tail': {'eval_args': True, 'apply': lambda a: assert_type(a, tuple)[1]},
            'I': {'eval_args': False, 'apply': lambda a: a},
        }
        self.builtin_functions2 = {
            '+': {'eval_args': True, 'apply': lambda a, b: assert_type(a, int) + assert_type(b, int)},
            '-': {'eval_args': True, 'apply': lambda a, b: assert_type(a, int) - assert_type(b, int)},
            '*': {'eval_args': True, 'apply': lambda a, b: assert_type(a, int) * assert_type(b, int)},
            '/': {'eval_args': True, 'apply': lambda a, b: assert_type(a, int) // assert_type(b, int)},
            '==': {'eval_args': True, 'apply': lambda a, b: 'K' if assert_type(a, int) == assert_type(b, int) else 'F'},
            '>': {'eval_args': True, 'apply': lambda a, b: 'K' if assert_type(a, int) > assert_type(b, int) else 'F'},
            '>=': {'eval_args': True, 'apply': lambda a, b: 'K' if assert_type(a, int) >= assert_type(b, int) else 'F'},
            '<': {'eval_args': True, 'apply': lambda a, b: 'K' if assert_type(a, int) < assert_type(b, int) else 'F'},
            '<=': {'eval_args': True, 'apply': lambda a, b: 'K' if assert_type(a, int) <= assert_type(b, int) else 'F'},
            'pair': {'eval_args': True, 'apply': lambda a, b: (a, b)},
            'K': {'eval_args': False, 'apply': lambda a, b: a},
            'F': {'eval_args': False, 'apply': lambda a, b: b},
        }

        self.builtin_functions3 = {
            'S': {'eval_args': False, 'apply': lambda a, b, c: Call(Call(a, c), Call(b, c))},
            'B': {'eval_args': False, 'apply': lambda a, b, c: Call(a, Call(b, c))},
            'C': {'eval_args': False, 'apply': lambda a, b, c: Call(Call(a, c), b)},
        }

    @staticmethod
    def format(exp):
        if exp is None:
            return '[]'

        if isinstance(exp, tuple):
            items = []
            cur = exp
            while True:
                items.append(Vm.format(cur[0]))
                if cur[1] is None:
                    return '[{0}]'.format(', '.join(items))
                if not isinstance(cur[1], tuple):
                    items.append(Vm.format(cur[1]))
                    return '"{0}"'.format(' '.join(items))
                cur = cur[1]

        return str(exp)

    def execute_statement(self, line):
        parts = line.split(' ')
        name = parts[0]
        if parts[1] != '=':
            raise ValueError('invalid line: {0}'.format(line))
        exp, pos = self.__parse_parts(parts, 2)
        self.named_functions[name] = exp

    def parse_exp(self, line):
        parts = line.split(' ')
        exp, pos = self.__parse_parts(parts, 0)
        return exp

    def eval(self, exp):
        if isinstance(exp, Call):
            return exp.eval(self)
        if exp in self.builtin_constants:
            return self.builtin_constants[exp]
        if exp in self.named_functions:
            return self.eval(self.named_functions[exp])
        return exp

    def __parse_parts(self, parts, pos):
        cur = parts[pos]
        if cur == '`':
            fun, next_pos = self.__parse_parts(parts, pos + 1)
            arg, next_pos = self.__parse_parts(parts, next_pos)
            return Call(fun, arg), next_pos

        if cur[0] in '1234567890':
            return int(cur), pos + 1

        return cur, pos + 1


class Call:
    def __init__(self, fun, arg) -> None:
        self.fun = fun
        self.arg = arg
        self.__evaluated = None

    def __str__(self) -> str:
        return '` {0} {1}'.format(self.fun, self.arg)

    def eval(self, vm):
        if self.__evaluated:
            return self.__evaluated

        fun = vm.eval(self.fun)

        if isinstance(fun, tuple):
            self.__evaluated = vm.eval(Call(Call(self.arg, fun[0]), fun[1]))
            return self.__evaluated

        if fun is None:
            self.__evaluated = 'K'
            return self.__evaluated

        if fun in vm.builtin_functions1:
            builtin = vm.builtin_functions1[fun]
            a = vm.eval(self.arg) if builtin['eval_args'] else self.arg
            self.__evaluated = vm.eval(builtin['apply'](a))
            return self.__evaluated

        if isinstance(fun, Call):
            if fun.fun in vm.builtin_functions2:
                builtin = vm.builtin_functions2[fun.fun]
                a = vm.eval(fun.arg) if builtin['eval_args'] else fun.arg
                b = vm.eval(self.arg) if builtin['eval_args'] else self.arg
                self.__evaluated = vm.eval(builtin['apply'](a, b))
                return self.__evaluated

            if isinstance(fun.fun, Call):
                if fun.fun.fun in vm.builtin_functions3:
                    builtin = vm.builtin_functions3[fun.fun.fun]
                    a = vm.eval(fun.fun.arg) if builtin['eval_args'] else fun.fun.arg
                    b = vm.eval(fun.arg) if builtin['eval_args'] else fun.arg
                    c = vm.eval(self.arg) if builtin['eval_args'] else self.arg
                    self.__evaluated = vm.eval(builtin['apply'](a, b, c))
                    return self.__evaluated

            self.__evaluated = self if fun == self.fun else Call(fun, self.arg)
            return self.__evaluated

        if fun not in vm.builtin_functions2 and fun not in vm.builtin_functions3:
            raise ValueError("couldn't apply {0} to {1}".format(fun, self.arg))

        self.__evaluated = self if fun == self.fun else Call(fun, self.arg)
        return self.__evaluated
