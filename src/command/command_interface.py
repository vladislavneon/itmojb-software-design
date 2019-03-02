from abc import ABC, abstractmethod


class CommandInvalidArgumentsError(ValueError):
    def __init__(self, message):
        super().__init__(f'command invalid arguments: {message}')


class CommandError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ShellCommand(ABC):
    def __init__(self, *args):
        self.args = args

    @abstractmethod
    def execute(self, in_stream):
        pass
