from src.command.command_interface import ShellCommand
from src.io.filesystem import FileSystem
from src.io.stream import Stream


class CLs(ShellCommand):
    """
    ShellCommand implementation for 'ls' command
    """
    def execute(self, in_stream):
        out_stream = Stream()
        path = self.args[0] if len(self.args) > 0 else "."
        try:
            listdir = FileSystem.ls(path)
            out_stream.write_lines(listdir)
        except FileNotFoundError:
            out_stream.write_line(f"No such file or directory: {path}")
        return out_stream
