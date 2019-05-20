import re
from argparse import ArgumentParser
from src.command.command_interface import ShellCommand
from src.io.stream import Stream
from src.io.filesystem import FileSystem


class GrepArgumentParserExit(SystemExit):
    pass


class GrepArgumentParser(ArgumentParser):
    def exit(self, *_):
        raise GrepArgumentParserExit


class CGrep(ShellCommand):
    def __init__(self, *args):
        super().__init__(*args)
        self.parser = GrepArgumentParser(description='show lines containing certain PATTERN in FILES',
                                         prog='grep')
        self.parser.add_argument('PATTERN', nargs=1)
        self.parser.add_argument('FILES', nargs='*', )
        self.parser.add_argument('-i', help='ignore case',
                                 action='store_true', default=False)
        self.parser.add_argument('-w', help='match whole words only',
                                 action='store_true', default=False)
        self.parser.add_argument('-A', help='print N lines after match',
                                 type=int, action='store', default=0,
                                 metavar='N')

    def execute(self, in_stream, interpreter_state=None):
        try:
            self.arguments = self.parser.parse_args(list(self.args))
            if self.arguments.FILES:
                res = []
                for file in self.arguments.FILES:
                    in_stream = FileSystem.read_file(file)
                    cur_res = self.grep_stream(in_stream)
                    res.extend(cur_res)
            else:
                res = self.grep_stream(in_stream)
            ous = Stream()
            ous.write_lines(res)
            return ous
        except GrepArgumentParserExit:
            return Stream()

    def grep_stream(self, stream):
        if self.arguments.w:
            pattern = r'(^|\W){}($|\W)'.format(self.arguments.PATTERN[0])
        else:
            pattern = r'{}'.format(self.arguments.PATTERN[0])

        if self.arguments.i:
            compiled_pattern = re.compile(pattern, flags=re.IGNORECASE)
        else:
            compiled_pattern = re.compile(pattern)

        lines = [line for line in stream]
        res = []

        ptr = 0
        while ptr < len(lines):
            if compiled_pattern.search(lines[ptr]):
                for i in range(ptr, min(len(lines), ptr + self.arguments.A + 1)):
                    res.append(lines[i])
                ptr = min(len(lines), ptr + self.arguments.A + 1)
            else:
                ptr += 1

        return res