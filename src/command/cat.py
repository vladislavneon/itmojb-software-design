from src.command.command_interface import ShellCommand
from src.io.filesystem import FileSystem


class CCat(ShellCommand):
    def execute(self, in_stream):
        file_name = self.args[0]
        return FileSystem.read_file(file_name)