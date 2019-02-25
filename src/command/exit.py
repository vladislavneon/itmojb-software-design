from src.command.command_interface import ShellCommand


class CExit(ShellCommand):
    def execute(self, in_stream):
        from src.interpreter import Interpreter
        Interpreter().state.should_exit = True
