class Stream:
    def __init__(self):
        self.stream = []
        self.pos = -1

    def __len__(self):
        return len(self.stream)

    def __str__(self):
        if self.stream:
            return '\n'.join(self.stream) + '\n'
        else:
            return ''

    def __iter__(self):
        return self

    def __next__(self):
        self.pos += 1
        if self.pos >= len(self.stream):
            self.pos = -1
            raise StopIteration
        return self.stream[self.pos]

    def write_line(self, line):
        self.stream.append(line)

    def write_lines(self, lines):
        for line in lines:
            self.stream.append(line)

    def clear(self):
        self.__init__()
