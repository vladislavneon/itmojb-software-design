from unittest import TestCase
from src.interpreter import Interpreter


class TestEcho(TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def get_command_output(self, command_text):
        return self.interpreter.execute(command_text).stream

    def test(self):
        exp = ['123 456']
        actual = self.get_command_output('echo 123 456')
        self.assertEqual(exp, actual)

    def test_substy(self):
        self.get_command_output('a=hello')

        exp = ['hello world']
        actual = self.get_command_output('echo $a world')
        self.assertEqual(exp, actual)

        exp = ['hello world']
        actual = self.get_command_output('echo "$a"world')
        self.assertEqual(exp, actual)

        exp = ['$a world']
        actual = self.get_command_output('echo \'$a world\'')
        self.assertEqual(exp, actual)