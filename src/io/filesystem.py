import os
import fileinput
from src.io.stream import Stream


class FileSystemFileNotExistError(ValueError):
    def __init__(self, message):
        super().__init__(f'File system error: file {message} doesn\'t exist')


class FileSystem:
    @staticmethod
    def cd(path=None):
        """
        Calls OS-based command to change current working directory
        :param path: str, path
        """
        if path is None:
            path = os.getenv("HOME")
        os.chdir(path)

    @staticmethod
    def cwd():
        """
        Returns current working directory
        :return: str, current working directory
        """
        return os.getcwd()

    @staticmethod
    def ls(path="."):
        """
        Returns list of files and directories in current directory or by provided path
        :param path: str, path
        :return: list, files and dirs in directory
        """
        return os.listdir(path)

    @staticmethod
    def read_file(file_name='-'):
        """
        Reads specified file `file_name` and returns its content via Stream object
        If `file_name` is not given then reads from standart input
        :param file_name: str, path to file
        :return: Stream, Stream object containing file content
        """
        stream = Stream()
        try:
            for line in fileinput.input(file_name):
                stream.write_line(line.strip('\n'))
        except FileNotFoundError:
            raise FileSystemFileNotExistError(file_name)
        return stream

    @staticmethod
    def write_file(file_name, stream):
        """
        Writes content of Stream object to the file
        :param file_name: str, path to the file
        :param stream: Stream
        """
        try:
            with open(file_name, 'w') as ouf:
                for line in stream:
                    ouf.write(line)
                    ouf.write('\n')
        except FileNotFoundError:
            raise FileSystemFileNotExistError(file_name)