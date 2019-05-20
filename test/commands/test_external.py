from unittest import TestCase
from src.interpreter import Interpreter


class TestExternal(TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def get_command_output(self, command_text):
        return self.interpreter.execute(command_text).stream

    def test_ls(self):
        exp = ['resources',
               'test_cat.py',
               'test_echo.py',
               'test_exit.py',
               'test_external.py',
               'test_pwd.py',
               'test_wc.py']
        actual = self.get_command_output('ls')
        self.assertEqual(exp, actual)

    def test_git_log(self):
        exp = ['commit 8645aad08bf1062b93f6aa9b7b88cac797a0ce2d',
               'Author: Vladislav Korablinov <vladislavneon1@mail.ru>',
               'Date:   Mon Feb 25 07:52:13 2019 +0300',
               '',
               '    Initial commit']
        actual = self.get_command_output('git log 8645aad08bf1062b93f6aa9b7b88cac797a0ce2d')
        self.assertEqual(exp, actual)

    def test_not_existing(self):
        exp = ['Invalid command']
        actual = self.get_command_output('existing')
        self.assertEqual(exp, actual)