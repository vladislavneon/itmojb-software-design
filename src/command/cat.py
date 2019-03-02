from src.command.command_interface import ShellCommand
from src.io.filesystem import FileSystem
from src.command.command_interface import CommandInvalidArgumentsError


class CCat(ShellCommand):
    def execute(self, in_stream):
        if len(self.args) == 0:
            raise CommandInvalidArgumentsError(f'"cat" takes 1 argument, given 0')
        file_name = self.args[0]
        return FileSystem.read_file(file_name)