from abc import ABC, abstractmethod
from src.io.stream import Stream


class CommandInvalidArgumentsError(ValueError):
    def __init__(self, message):
        super().__init__(f'command invalid arguments: {message}')


class CommandError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ShellCommand(ABC):
    """
    Abstract class for all CLI commands.
    It has a constructor taking list of command arguments and method `execute` used to execute a command.
    """
    def __init__(self, *args):
        self.args = args

    @abstractmethod
    def execute(self, in_stream):
        """
        Executes the command using `in_stream` as input data and returns output data as Stream object.
        :param in_stream: Stream, input stream
        :return: Stream, output stream
        """
        return Stream()
