import subprocess as sbpr
from src.command.command_interface import ShellCommand
from src.io.stream import Stream


class ExternalCommand(ShellCommand):
    def execute(self, in_stream):
        result = sbpr.run(
            self.args,
            input=str(in_stream),
            text=True,
            capture_output=True
        )
        result = result.stdout.strip('\n').split('\n')
        ous = Stream()
        ous.write_lines(result)
        return ous