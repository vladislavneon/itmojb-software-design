from src.command.command_interface import ShellCommand


class CGrep(ShellCommand):
    def execute(self, in_stream):
        print(self.args)