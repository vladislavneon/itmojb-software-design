import os
import fileinput
from src.io.stream import Stream


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
        for line in fileinput.input(file_name):
            stream.write_line(line.strip('\n'))
        return stream

    @staticmethod
    def write_file(file_name, stream):
        with open(file_name, 'w') as ouf:
            for line in stream:
                ouf.write(line)
                ouf.write('\n')