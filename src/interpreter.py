from src.io.stream import Stream
from src.parser.command_parser import CommandParser
import src.command as commands
from src.command.external import ExternalCommandError


class InterpreterState:
    def __init__(self):
        self.should_exit = False

    def get_should_exit(self):
        return self.should_exit

    def set_should_exit(self, val):
        self.should_exit = val

class Interpreter:
    def __init__(self):
        self.state = InterpreterState()
        self.parser = CommandParser()
        self.parser.add_command('echo', commands.echo.CEcho)
        self.parser.add_command('cat', commands.cat.CCat)
        self.parser.add_command('pwd', commands.pwd.CPwd)
        self.parser.add_command('exit', commands.exit.CExit)
        self.parser.add_command('wc', commands.wc.CWc)
        self.parser.add_command('grep', commands.grep.CGrep)

    def execute(self, command_text):
        """
        Execute one line of commands
        :param command_text: str, string of commands
        :return: Stream, output stream
        """
        self.state.set_should_exit(False)
        commands = self.parser.parse(command_text)
        stream = Stream()
        try:
            for com in commands:
                stream = com.execute(stream, self.state)
            if self.state.get_should_exit():
                print('bye')
                return
            print(stream, end='')
        except ExternalCommandError:
            print('Invalid command')
        except FileNotFoundError as e:
            print(e)


    def run(self):
        """
        Runs interpreter.
        """
        self.state.set_should_exit(False)
        while True:
            command_text = input().strip()
            self.execute(command_text)
            if self.state.get_should_exit():
                break
