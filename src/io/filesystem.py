import os
import fileinput
from src.io.stream import Stream


class FileSystem:
    @staticmethod
    def cd(path):
        """
        Calls OS-based command to change current working directory
        :param path: str, path
        """
        os.chdir(path)

    @staticmethod
    def cwd():
        """
        Returns current working directory
        :return: str, current working directory
        """
        return os.getcwd()

    @staticmethod
    def read_file(file_name='-'):
        """
        Reads specified file `file_name` and returns its content via Stream object
        If `file_name` is not given then reads from standart input
        :param file_name: str, path to file
        :return: Stream, Stream object containing file content
        """
        stream = Stream()
        with fileinput.input(file_name) as inf:
            for line in inf:
                stream.write_line(line.strip('\n'))
        return stream

    @staticmethod
    def write_file(file_name, stream):
        """
        Writes content of Stream object to the file
        :param file_name: str, path to the file
        :param stream: Stream
        """
        with open(file_name, 'w') as ouf:
            for line in stream:
                ouf.write(line)
                ouf.write('\n')