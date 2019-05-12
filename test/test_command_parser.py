from unittest import TestCase
from src.parser.command_parser import CommandParser
from src.command.command_interface import ShellCommand


class FakeCmd(ShellCommand):
    def execute(self, in_stream):
        pass

    def get_args(self):
        return self.args


class FooCmd(ShellCommand):
    def execute(self, in_stream):
        pass


class BarCmd(ShellCommand):
    def execute(self, in_stream):
        pass


class TestCommandParser(TestCase):
    def setUp(self):
        self.parser = CommandParser()
        self.parser.add_command('fake', FakeCmd)
        self.parser.add_command('foo', FooCmd)
        self.parser.add_command('bar', BarCmd)

    def testCommandDetection(self):
        cmd_list = self.parser.parse('fake a | foo b | bar c')
        self.assertEqual(len(cmd_list), 3)
        self.assertIsInstance(cmd_list[0], FakeCmd)
        self.assertIsInstance(cmd_list[1], FooCmd)
        self.assertIsInstance(cmd_list[2], BarCmd)

        cmd_list = self.parser.parse('fake foo | bar c')
        self.assertEqual(len(cmd_list), 2)
        self.assertIsInstance(cmd_list[0], FakeCmd)
        self.assertIsInstance(cmd_list[1], BarCmd)

    def testCommandAliasing(self):
        self.parser.parse('alias1=foo')
        self.parser.parse('alias2=bar')

        cmd_list = self.parser.parse('$alias1 a | $alias2 b')
        self.assertEqual(len(cmd_list), 2)
        self.assertIsInstance(cmd_list[0], FooCmd)
        self.assertIsInstance(cmd_list[1], BarCmd)

    def testAliasOverwrite(self):
        self.parser.parse('alias1=foo')
        cmd_list = self.parser.parse('$alias1 a')
        self.assertEqual(len(cmd_list), 1)
        self.assertIsInstance(cmd_list[0], FooCmd)

        self.parser.parse('alias1=bar')
        cmd_list = self.parser.parse('$alias1 a')
        self.assertEqual(len(cmd_list), 1)
        self.assertIsInstance(cmd_list[0], BarCmd)

    def testArgsPassing(self):
        self.parser.add_command('fake', FakeCmd)
        cmd_list = self.parser.parse('fake one   two    -h -f three')
        self.assertEqual(len(cmd_list), 1)
        self.assertIsInstance(cmd_list[0], FakeCmd)
        self.assertEqual(cmd_list[0].get_args(), ('one', 'two', '-h', '-f', 'three'))
