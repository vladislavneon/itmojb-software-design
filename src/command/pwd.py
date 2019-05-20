from src.command.command_interface import ShellCommand
from src.io.stream import Stream
from src.io.filesystem import FileSystem


class CPwd(ShellCommand):
    """
    ShellCommand implementation for 'pwd' command
    """
    def execute(self, in_stream, interpreter_state=None):
        ous = Stream()
        ous.write_line(FileSystem.cwd())
        return ous