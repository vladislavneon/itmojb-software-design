from unittest import TestCase
from src.interpreter import Interpreter


class TestCat(TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def get_command_output(self, command_text):
        return self.interpreter.execute(command_text).stream

    def test_1(self):
        exp = ['from src.interpreter import Interpreter',
               '',
               'if __name__ == "__main__":',
               '    interpreter = Interpreter()',
               '    interpreter.run()'
        ]
        actual = self.get_command_output('cat resources/cli.py')
        self.assertEqual(exp, actual)

    def test_2(self):
        exp = ['hello',
               '    i\'m here ',
               '        from where',
               '    ',
               'this wasnot empty',
               '!!!!"""',
               '',
               '',
               'but wis wos'
        ]
        actual = self.get_command_output('cat resources/test.txt')
        self.assertEqual(exp, actual)

    def test_not_found(self):
        exp = ['[Errno 2] No such file or directory: \'cat\'']
        actual = self.get_command_output('cat cat')
        self.assertEqual(exp, actual)

    def test_no_args(self):
        exp = ['command invalid arguments: "cat" takes 1 argument, given 0']
        actual = self.get_command_output('cat')
        self.assertEqual(exp, actual)