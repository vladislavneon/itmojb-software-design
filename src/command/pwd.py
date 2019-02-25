from src.command.command_interface import ShellCommand
from src.io.stream import Stream
from src.io.filesystem import FileSystem


class CPwd(ShellCommand):
    def execute(self, in_stream):
        ous = Stream()
        ous.write_line(FileSystem.cwd())
        return ous