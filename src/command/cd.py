from src.command.command_interface import ShellCommand, CommandInvalidArgumentsError
from src.io.filesystem import FileSystem


class CCd(ShellCommand):
    """
    ShellCommand implementation for 'cd' command
    """
    def execute(self, in_stream):
        if len(self.args) == 0:
            raise CommandInvalidArgumentsError(f'"cd" takes 1 argument, given 0')
        path = self.args[0]
        FileSystem.cd(path)
