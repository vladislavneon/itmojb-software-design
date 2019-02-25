from abc import ABC, abstractmethod


class ShellCommand(ABC):
    def __init__(self, *args):
        self.args = args

    @abstractmethod
    def execute(self, in_stream):
        pass
