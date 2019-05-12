from unittest import TestCase
from src.io.stream import Stream


class TestStream(TestCase):
    def test_fill(self):
        stream = Stream()
        content = ['ab', 'cd', 'ef', '', 'end']
        stream.write_lines(content)
        stream.write_line('gh')
        self.assertEqual(len(content) + 1, len(stream))
        self.assertEqual('\n'.join(content) + '\ngh\n', str(stream))

    def test_clear(self):
        stream = Stream()
        stream.write_line('line')
        stream.clear()
        self.assertEqual(0, len(stream))
        self.assertEqual('', str(stream))

    def test_iteration(self):
        stream = Stream()
        content = ['ab', 'cd', 'ef', '', 'end']
        stream.write_lines(content)

        self.assertEqual(len(content), len(stream))

        j = 0
        for line in stream:
            self.assertEqual(content[j], line)
            j += 1
        self.assertEqual(len(content), j)
