import os
from unittest import TestCase
from src.interpreter import Interpreter


class TestPwd(TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def get_command_output(self, command_text):
        return self.interpreter.execute(command_text).stream

    def test(self):
        exp = [os.getcwd()]
        actual = self.get_command_output('pwd')
        self.assertEqual(exp, actual)
