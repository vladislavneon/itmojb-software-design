from src.command.command_interface import ShellCommand
from src.io.filesystem import FileSystem
from src.io.stream import Stream


class CLs(ShellCommand):
    """
    ShellCommand implementation for 'ls' command
    """
    def execute(self, in_stream):
        ous = Stream()
        path = self.args[0] if len(self.args) > 0 else "."
        listdir = FileSystem.ls(path)
        ous.write_lines(listdir)
        return ous
