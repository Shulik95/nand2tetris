import sys, os


class Parser:
    """

    """

    def __init__(self, input_file):
        """

        :param input_file: pu
        """
        self.file = input_file
        self.curr_line = None

    def has_more_commands(self):
        """

        :return:
        """
        next_line = self.file.readline()  # reads next line
        if not next_line:
            return False
        return True

    def advance(self):
        line = self.file.readline()


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename)
