from src.io.stream import Stream
from src.parser.command_parser import CommandParser
import src.command as commands
from src.command.external import ExternalCommandError
from src.io.filesystem import FileSystemFileNotExistError


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
            cls.instance = obj
        return cls.instance

    def __init__(self):
        pass

    def run(self):
        """
        Runs interpreter.
        """
        self.state.should_exit = False
        while True:
            command_text = input().strip()
            commands = self.parser.parse(command_text)
            stream = Stream()
            for com in commands:
                try:
                    stream = com.execute(stream)
                except ExternalCommandError:
                    print('Invalid command')
                except FileSystemFileNotExistError as e:
                    print(e)
            if Interpreter().state.should_exit:
                print('bye')
                break
            print(stream, end='')
