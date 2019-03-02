from src.command.command_interface import ShellCommand
import src.interpreter


class CExit(ShellCommand):
    """
    ShellCommand implementation for 'exit' command
    """
    def execute(self, in_stream):
        src.interpreter.Interpreter().state.should_exit = True
