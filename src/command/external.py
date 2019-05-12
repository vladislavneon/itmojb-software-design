import subprocess as sbpr
from src.command.command_interface import ShellCommand
from src.command.command_interface import CommandError
from src.io.stream import Stream


class ExternalCommandError(CommandError):
    def __init__(self, message):
        super().__init__(f'external command error: {message}')


class ExternalCommand(ShellCommand):
    """
    ShellCommand implementation for any unknown (external) command
    """
    def execute(self, in_stream):
        try:
            result = sbpr.run(
                self.args,
                input=str(in_stream),
                text=True,
                capture_output=True
            )
            result = result.stdout.strip('\n').split('\n')
        except Exception as e:
            raise ExternalCommandError(e)
        ous = Stream()
        ous.write_lines(result)
        return ous