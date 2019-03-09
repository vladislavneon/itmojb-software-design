import os
from unittest import TestCase

from src.interpreter import Interpreter


class TestCommandParser(TestCase):

    def testUpDir(self):
        os.mkdir("tmp")
        os.mkdir("tmp/dir")
        f = open("tmp/file.txt", "w+")
        f.close()

        interpreter = Interpreter()
        files_set = set(str(interpreter.execute("ls tmp")).strip().split('\n'))
        print(files_set)
        true_files_set = {"dir", "file.txt"}
        self.assertEqual(true_files_set, files_set)
        os.remove("tmp/file.txt")
        os.rmdir("tmp/dir")
        os.rmdir("tmp")
