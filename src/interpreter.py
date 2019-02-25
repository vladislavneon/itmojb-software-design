from src.io.stream import Stream
from src.parser.command_parser import CommandParser
from src.command.cat import CCat
from src.command.echo import CEcho
from src.command.pwd import CPwd
from src.command.exit import CExit
from src.command.wc import CWc


class InterpreterState:
    def __init__(self):
        self.should_exit = False

class Interpreter:
    def __new__(cls):
        if not getattr(cls, 'instance', None):
            obj = super().__new__(cls)
            obj.state = InterpreterState()
            obj.input_stream = Stream()
            obj.output_stream = Stream()
            obj.parser = CommandParser()
            obj.parser.add_command('echo', CEcho)
            obj.parser.add_command('cat', CCat)
            obj.parser.add_command('pwd', CPwd)
            obj.parser.add_command('exit', CExit)
            obj.parser.add_command('wc', CWc)
            cls.instance = obj
        return cls.instance

    def __init__(self):
        pass

    def run(self):
        self.state.should_exit = False
        while True:
            command_text = input().strip()
            commands = self.parser.parse(command_text)
            stream = Stream()
            for com in commands:
                stream = com.execute(stream)
            if Interpreter().state.should_exit:
                print('bye')
                break
            print(stream.stream)
            print(stream, end='')
