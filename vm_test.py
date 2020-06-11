import unittest

from parameterized import parameterized

from vm import Vm


class VmTests(unittest.TestCase):

    def setUp(self) -> None:
        self.vm = Vm()

    @parameterized.expand([
        ['+'],
        ['negate'],
        ['` negate 1'],
        ['` ` + 1 2'],
    ])
    def test_parse_exp(self, exp):
        self.assertEqual(exp, str(self.vm.parse_exp(exp)))

    @parameterized.expand([
        ['+', '+'],
        ['1', '1'],
        ['` negate 1', '-1'],
        ['` ` + 1 2', '3'],
        ['` ` pair 1 2', '"1 2"'],
        ['` ` pair 1 emptyList', '[1]'],
        ['` ` pair 2 ` ` pair 1 emptyList', '[2, 1]'],
        ['` isEmptyList ` ` pair 1 emptyList', 'F'],
        ['` isEmptyList emptyList', 'K'],
        ['` ` K a b', 'a'],
        ['` ` K a ` 1 2', 'a'],
        ['` ` F a b', 'b'],
        ['` ` ` S K b c', 'c'],
        ['` ` ` B ` + 1 negate 20', '-19'],
        ['` I 20', '20'],
        ['` ` ` C + 1 2', '3'],
        ['` ` + x x', '20', 'x = 10'],
        ['` head ` ` pair 10 20', '10'],
        ['` tail ` ` pair 10 20', '20'],
        ['` n1035 ` ` pair 10 emptyList', '1', 'n1035 = ` ` S ` ` C isEmptyList 0 ` ` B ` + 1 ` ` B n1035 tail'],
        ['` ` drawClickedPixelProgram emptyList ` ` pair 0 0', '[0, [], [["0 0"]]]', 'drawClickedPixelProgram = ` ` C ` ` B B ` ` B ` B ` pair 0 ` ` C ` ` B B pair ` ` C pair emptyList ` ` C ` ` B pair ` ` C pair emptyList emptyList'],
    ])
    def test_eval(self, exp, expected, *statements):
        for statement in statements:
            self.vm.execute_statement(statement)
        self.assertEqual(expected, Vm.format(self.vm.eval(self.vm.parse_exp(exp))))


if __name__ == '__main__':
    unittest.main()
