import sys, os


class Parser:
    """

    """

    def __init__(self, input_file):
        """

        :param input_file: pu
        """
        self.file = open(input_file)
        self.lines = self.file.readlines()
        self.curr_line = None
        self.line_counter = 0
        self.command_dict = {
            "add": "C_ARITHMETIC",
            "sub": "C_ARITHMETIC",
            "neg": "C_ARITHMETIC",
            "eq": "C_ARITHMETIC",
            "gt": "C_ARITHMETIC",
            "lt": "C_ARITHMETIC",
            "and": "C_ARITHMETIC",
            "or": "C_ARITHMETIC",
            "not": "C_ARITHMETIC",
            "push": "C_PUSH",
            "pop": "C_POP"
        }

    def has_more_commands(self):
        """

        :return:
        """
        if self.line_counter == len(self.lines):  # means were done reading.
            return False
        return True

    def advance(self):
        """

        :return:
        """
        self.curr_line = self.lines[self.line_counter]
        self.line_counter += 1

    def command_type(self):
        """

        :return:
        """
        temp_line = self.__clean_line()
        return self.command_dict[temp_line[0]]

    def arg1(self):
        return self.__clean_line()[0]

    def arg2(self):
        if self.command_dict[self.arg1()] == 'C_PUSH' or (self.command_dict[self.arg1()] == 'C_POP'):
            return self.__clean_line()[2]

    def __clean_line(self):
        """
        :return:
        """
        if len(self.curr_line.split()) > 1:
            if not self.has_more_commands():
                return self.curr_line.split(" ")
            return self.curr_line[:-1].split(" ")
        cleaned = ""
        for letter in self.curr_line:
            if letter == "/":
                cleaned += ""
                break
            elif letter == "\n" or letter == " ":
                cleaned += ""
            else:
                cleaned += letter
        return [cleaned]


class CodeWriter:

    def __init__(self, output_file):
        """

        :param output_file:
        """
        self.file = open(output_file, "w")

    def write_arithmetic(self, command):
        """

        :param command:
        :return:
        """
        pass

    def write_push_pop(self, command, segment, index):
        """

        :param command:
        :param segment:
        :param index:
        :return:
        """
        if command == "C_PUSH":
            pass
        pass


if __name__ == '__main__':
    temp_P = Parser(sys.argv[1])
    while temp_P.has_more_commands():
        temp_P.advance()
        print(temp_P.arg2())
