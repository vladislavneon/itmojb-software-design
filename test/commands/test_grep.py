from unittest import TestCase
from src.interpreter import Interpreter


class TestGrep(TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def get_command_output(self, command_text):
        return self.interpreter.execute(command_text).stream

    def test_a(self):
        exp = ['abc',
               'abacaba',
               'long distance runner',
               'cocaine',
               '***say///hey',
               'abacababacaba']
        actual = self.get_command_output('grep a resources/test_grep.txt')
        self.assertEqual(exp, actual)

    def test_word(self):
        exp = ['run to the hills']
        actual = self.get_command_output('grep -w run resources/test_grep.txt')
        self.assertEqual(exp, actual)

    def test_word_ic(self):
        exp = ['run to the hills', 'RuN FoR YoUr LiFe']
        actual = self.get_command_output('grep -w -i run resources/test_grep.txt')
        self.assertEqual(exp, actual)

        exp = ['line 2', 'line 3']
        actual = self.get_command_output('grep -w -i line resources/test_grep.txt')
        self.assertEqual(exp, actual)

    def test_ic(self):
        exp = ['long distance runner', 'run to the hills', 'RuN FoR YoUr LiFe']
        actual = self.get_command_output('grep -i run resources/test_grep.txt')
        self.assertEqual(exp, actual)

    def test_append(self):
        exp = ['helb', 'run to the hills', 'RuN FoR YoUr LiFe', 'abacababacaba']
        actual = self.get_command_output('grep -A 3 he resources/test_grep.txt')
        self.assertEqual(exp, actual)

    def test_regex(self):
        exp = ['cocaine']
        actual = self.get_command_output("grep '..ine' resources/test_grep.txt")
        self.assertEqual(exp, actual)

        exp = ['сэмплтекст']
        actual = self.get_command_output("grep '[а-я]' resources/test_grep.txt")
        self.assertEqual(exp, actual)

        exp = ['line 2', 'line 3', '42 42 42']
        actual = self.get_command_output("grep '\d' resources/test_grep.txt")
        self.assertEqual(exp, actual)
