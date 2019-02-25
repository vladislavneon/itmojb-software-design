from src.command.command_interface import ShellCommand
from src.io.stream import Stream
from src.io.filesystem import FileSystem


class CWc(ShellCommand):
    def execute(self, in_stream):
        if self.args:
            file_name = self.args[0]
            in_stream = FileSystem.read_file(file_name)
        lines_number = len(in_stream)
        words_number = 0
        symbols_number = 0
        for line in in_stream:
            symbols_number += len(line)
            words_number += len(line.split())
        ous = Stream()
        ous.write_line(f'{lines_number} {words_number} {symbols_number}')
        return ous