from src.io.stream import Stream
from src.parser.command_parser import CommandParser
import src.command as commands


class InterpreterState:
    def __init__(self):
        self.should_exit = False


class Interpreter:
    def __new__(cls):
        if not getattr(cls, 'instance', None):
            obj = super().__new__(cls)
            obj.state = InterpreterState()
            obj.parser = CommandParser()
            obj.parser.add_command('echo', commands.echo.CEcho)
            obj.parser.add_command('cat', commands.cat.CCat)
            obj.parser.add_command('pwd', commands.pwd.CPwd)
            obj.parser.add_command('exit', commands.exit.CExit)
            obj.parser.add_command('wc', commands.wc.CWc)
            obj.parser.add_command('grep', commands.grep.CGrep)
            obj.parser.add_command('cd', commands.cd.CCd)
            obj.parser.add_command('ls', commands.ls.CLs)
            cls.instance = obj
        return cls.instance

    def __init__(self):
        pass

    def execute(self, command_text):
        """
        Execute commands of one line
        :param command_text: str, string of commands
        :return: Stream, output stream
        """
        self.state.should_exit = False
        commands = self.parser.parse(command_text)
        stream = Stream()
        for com in commands:
            stream = com.execute(stream)
            if Interpreter().state.should_exit:
                break
        return stream
