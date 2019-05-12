from src.command.command_interface import ShellCommand, CommandInvalidArgumentsError
from src.io.filesystem import FileSystem
from src.io.stream import Stream


class CCd(ShellCommand):
    """
    ShellCommand implementation for 'cd' command
    """
    def execute(self, in_stream):
        path = self.args[0] if len(self.args) > 0 else None
        out_stream = Stream()
        try:
            FileSystem.cd(path)
        except FileNotFoundError:
            out_stream.write_line(f"No such file or directory: {path}")
        return out_stream
