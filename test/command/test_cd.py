from unittest import TestCase

from src.interpreter import Interpreter


class TestCommandParser(TestCase):

    def testNotChangeDir(self):
        interpreter = Interpreter()
        current_dir = str(interpreter.execute("pwd"))
        interpreter.execute("cd .")
        not_changed_current_dir = str(interpreter.execute("pwd"))
        self.assertEqual(current_dir, not_changed_current_dir)

    def testUpDir(self):
        interpreter = Interpreter()
        current_dir = str(interpreter.execute("pwd"))
        true_upper_dir = current_dir[:current_dir.rfind('/')]
        interpreter.execute("cd ..")
        changed_upper_dir = str(interpreter.execute("pwd")).strip()
        self.assertEqual(true_upper_dir, changed_upper_dir)
