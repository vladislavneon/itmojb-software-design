from unittest import TestCase
from src.interpreter import Interpreter


class TestWc(TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def get_command_output(self, command_text):
        return self.interpreter.execute(command_text).stream

    def test_one_line(self):
        exp = ['1 4 18']
        actual = self.get_command_output('echo hello world to all | wc')
        self.assertEqual(exp, actual)

    def test_with_file(self):
        exp = ['5 12 117']
        actual = self.get_command_output('wc resources/cli.py')
        self.assertEqual(exp, actual)

    def test_file_pipe(self):
        exp = ['9 12 75']
        actual = self.get_command_output('cat "resources/test.txt" | wc')
        self.assertEqual(exp, actual)
