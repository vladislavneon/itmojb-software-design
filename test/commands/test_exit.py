from unittest import TestCase
from src.interpreter import Interpreter


class TestExit(TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def get_command_output(self, command_text):
        return self.interpreter.execute(command_text).stream

    def test(self):
        exp = ['bye']
        actual = self.get_command_output('exit')
        self.assertEqual(exp, actual)
        self.assertEqual(self.interpreter.state.get_should_exit(), True)

    def test_with_other_commands(self):
        exp = ['1 1 3', 'bye']
        actual = self.get_command_output('echo 123 | wc | exit')
        self.assertEqual(exp, actual)
        self.assertEqual(self.interpreter.state.get_should_exit(), True)
