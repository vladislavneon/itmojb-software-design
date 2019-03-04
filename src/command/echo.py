from src.command.command_interface import ShellCommand
from src.io.stream import Stream


class CEcho(ShellCommand):
    """
    ShellCommand implementation for 'echo' command
    """
    def execute(self, in_stream):
        ous = Stream()
        ous.write_line(' '.join(self.args))
        return ous