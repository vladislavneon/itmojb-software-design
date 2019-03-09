from src.command.command_interface import ShellCommand, CommandInvalidArgumentsError
from src.io.filesystem import FileSystem


class CCd(ShellCommand):
    """
    ShellCommand implementation for 'cd' command
    """
    def execute(self, in_stream):
        path = self.args[0] if len(self.args) > 0 else None
        FileSystem.cd(path)
