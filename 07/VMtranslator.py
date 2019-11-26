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
        self.addr = {"local": "LCL",
                     "argument": "ARG",
                     "this": "THIS",
                     "that": "THAT",
                     "static": "STATIC",
                     "temp": 5,
                     "pointer": 3
                     }

        self.file_name = output_file[:-2]

    def write_arithmetic(self, command):
        """

        :param command:
        :return:
        """
        if command == "not" or command == "neg":
            self.__one_var(command)

    def __one_var(self, command):
        """

        :param command:
        :return:
        """
        self.__pop_from_stack()
        if command == "not":
            self.__write("D=!D")
        else:
            self.__write("D=-D")
        self.__push_to_stack()

    def __two_var(self, command):

            


    def write_push_pop(self, command, segment, index):
        """

        :param command:
        :param segment:
        :param index:
        :return:
        """
        if command == "C_PUSH":
            if segment == "constant":
                self.__write("@" + str(index))
                self.__write("D=A")
                self.__push_to_stack()
            elif segment in ["argument", "local", "this", "that"]:
                self.__get_address(index, segment)
                self.__write("D=M")  # *addr
                self.__push_to_stack()  # *addr = *sp
            elif segment == "static":
                self.__write("@" + self.file_name + str(index))
                self.__write("D=M")
                self.__push_to_stack()
            elif segment == "temp" or segment == "pointer":
                self.__write("@R" + str(self.addr[segment] + index))
                self.__write("D=M")
                self.__push_to_stack()

        elif command == "C_POP":
            if segment in ["argument", "local", "this", "that"]:
                self.__get_address(index, segment)
                self.__write("@R13")
                self.__write("M=D")
                self.__pop_from_stack()
                self.__write("@R13")
                self.__write("A=M")
                self.__write("M=D")
            elif segment == 'static':
                self.__pop_from_stack()  # assigns value to D
                self.__write('@' + self.file_name + str(index))
                self.__write('M=D')
            elif segment == "temp" or segment == "pointer":
                self.__pop_from_stack()
                self.__write("@R" + str(self.addr[segment] + index))
                self.__write("M=D")

    def __get_address(self, index, segment):
        """

        :param index:
        :param segment:
        :return:
        """
        self.__write("@" + str(index))  # access address LCL+index
        self.__write("D=A")
        self.__write("@" + self.addr[segment])
        self.__write("D=D+M")
        self.__write("A=D")

    def __push_to_stack(self):
        """

        :return:
        """
        self.__write("@SP")
        self.__write("A=M")
        self.__write("M=D")
        self.__write("@SP")
        self.__write("M=M+1")

    def __pop_from_stack(self):
        """

        :return:
        """
        self.__write("@SP")
        self.__write("M=M-1")
        self.__write("A=M")
        self.__write("D=M")

    def __write(self, line):
        """
        writes file to text.
        :param line: string which contains an hack command.
        """
        self.file.write(line + "\n")


if __name__ == '__main__':
    temp_P = Parser(sys.argv[1])
    while temp_P.has_more_commands():
        temp_P.advance()
        print(temp_P.arg2())
