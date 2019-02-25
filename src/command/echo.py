from src.command.command_interface import ShellCommand
from src.io.stream import Stream


class CEcho(ShellCommand):
    def execute(self, in_stream):
        ous = Stream()
        ous.write_line(' '.join(self.args))
        return ous