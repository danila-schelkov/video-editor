# Methods source: https://stackoverflow.com/questions/23113494/double-progress-bar-in-python

import sys


def move_cursor_up(repeat_times: int = 1):
    # My terminal breaks if we don't flush after the escape-code
    sys.stdout.write("\x1b[1A" * repeat_times)
    sys.stdout.flush()


def move_cursor_down(repeat_times: int = 1):
    # I could use '\x1b[1B' here, but newline is faster and easier
    sys.stdout.write("\n" * repeat_times)
    sys.stdout.flush()
