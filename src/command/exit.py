from src.command.command_interface import ShellCommand


class CExit(ShellCommand):
    """
    ShellCommand implementation for 'exit' command
    """
    def execute(self, in_stream, interpreter_state):
        interpreter_state.set_should_exit(True)
        return in_stream
