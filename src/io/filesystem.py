import os
import fileinput
from src.io.stream import Stream


class FileSystemFileNotExistError(ValueError):
    def __init__(self, message):
        super().__init__(f'File system error: file {message} doesn\'t exist')


class FileSystem:
    @staticmethod
    def cd(path):
        os.chdir(path)

    @staticmethod
    def cwd():
        return os.getcwd()

    @staticmethod
    def read_file(file_name='-'):
        stream = Stream()
        try:
            for line in fileinput.input(file_name):
                stream.write_line(line.strip('\n'))
        except FileNotFoundError:
            raise FileSystemFileNotExistError(file_name)
        return stream

    @staticmethod
    def write_file(file_name, stream):
        try:
            with open(file_name, 'w') as ouf:
                for line in stream:
                    ouf.write(line)
                    ouf.write('\n')
        except FileNotFoundError:
            raise FileSystemFileNotExistError(file_name)