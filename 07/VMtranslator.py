import sys, os


class Parser:
    """
    This class receives a file as input, moves it into a data structure which
    allows easy line manipulation.
    """

    def __init__(self, input_file):
        """
        creates a Parser object.
        :param input_file: the file to parse.
        """
        self.file = open(input_file)
        self.lines = []
        for line in self.file.readlines():
            if "/" in line or "\n" == line[0]:  # clear comments and empty lines
                continue
            self.lines.append(line)
        self.curr_line = None
        self.line_counter = 0
        self.__command_dict = {
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
        checks if there are more commands in the input/
        :return: boolean value.
        """
        if self.line_counter == len(self.lines):  # means were done reading.
            return False
        return True

    def advance(self):
        """
        Reads the next command from the input and makes it the next comment.
        Called only if if has_more_commands is True.
        """
        self.curr_line = self.lines[self.line_counter]
        self.line_counter += 1

    def command_type(self):
        """
        Returns the type of the current VM command. C_ARITHMETIC is returned
        for all the arithmetic commands.
        :return:command type.
        """
        temp_line = self.__clean_line()
        return self.__command_dict[temp_line[0]]

    def arg1(self):
        """
        returns the first argument of the current command. in the case of
        C_ARITHMETIC the command itself is returned.
        """
        if self.command_type() == "C_ARITHMETIC":
            return self.__clean_line()[0]  # returns arithmetic command itself
        return self.__clean_line()[1]  # returns segment for pop/push

    def arg2(self):
        """
        returns the second argument of the current command. only called for
        specific command types.
        """
        return self.__clean_line()[2]

    def __clean_line(self):
        """
        This function clears away all white space from the line. white space
        includes in line comments and comment lines.
        :return: an array which holds the cleaned values.
        """
        if len(self.curr_line.split()) > 1:
            if not self.has_more_commands():  # deals with last line
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
    """
    This class translates the VM commands into hack language.
    """

    def __init__(self, output_file):
        """
        creates a CodeWriter object.
        :param output_file: file to write into.
        """
        self.file = open(output_file + ".asm", "w")
        self.addr = {"local": "LCL",
                     "argument": "ARG",
                     "this": "THIS",
                     "that": "THAT",
                     "static": "STATIC",
                     "temp": 5,
                     "pointer": 3
                     }

        self.file_name = output_file.split("/")[-1]
        self.__counter = 0

    def write_arithmetic(self, command):
        """
        Writes the assembly code that is the translation of the given
        arithmetic command.
        :param command: str representing a command.
        """
        if command == "not" or command == "neg":
            self.__one_var(command)
        else:
            self.__two_var(command)

    def __one_var(self, command):
        """

        :param command:
        :return:
        """
        self.__pop_from_stack()
        if command == "not":
            self.write("D=!D")
        else:
            self.write("D=-D")
        self.__push_to_stack()

    def __two_var(self, command):
        """

        :param command:
        :return:
        """
        self.__pop_from_stack()
        self.write("@SP")
        self.write("M=M-1")
        self.write("A=M")

        if command in ["add", "sub"]:
            if command == "add":  # x+y
                self.write("M=M+D")

            else:  # command has to be "sub
                self.write("M=M-D")
            self.write("@SP")
            self.write("M=M+1")

        elif command in ["eq", "gt", "lt"]:
            # common lines of code:
            self.write("D=M-D")  # performs x-y
            self.write(("@JUMP" + self.__counter.__str__()))
            self.write("M=-1")
            #  cases:
            if command == "eq":  # check if x = y
                self.write("D;JEQ")

            elif command == "gt":  # check if x > y
                self.write("D;JGT")  # A will be 1

            else:  # check if x < y because command has to be "lt"
                self.write("D;JLT")
            # common lines
            self.write("@NJUMP" + self.__counter.__str__())
            self.write("M=0")
            self.write("D=M")
            self.write("0;JMP")
            # creates jump label in case command is true:
            self.write("(JUMP" + self.__counter.__str__() + ")")
            self.write("D=M")
            #  creates label for case the command is flase
            self.write("(NJUMP"+self.__counter.__str__()+")")
            self.write("D=M")
            #  D holds either 1 or o, push D to stack now.
            self.__push_to_stack()
            self.__counter += 1  # advance counter for further use.

        else:  # command is "and" or "or"
            if command == "or":
                self.write("D=D|M")
            else:
                self.write("D=D&M")
            self.__push_to_stack()

    def write_push_pop(self, command, segment, index):
        """
        Writes the assembly code that is the translation of the given command.
        the command is either C_PUSH or C_POP.
        :param command: command as str
        :param segment: segment to pop/push into/from.
        :param index: the index of the item in the segment.
        """
        if command == "C_PUSH":
            if segment == "constant":
                self.write("@" + str(index))
                self.write("D=A")
                self.__push_to_stack()
            elif segment in ["argument", "local", "this", "that"]:
                self.__get_address(index, segment)
                self.write("A=D+M")
                self.write("D=M")  # *addr
                self.__push_to_stack()  # *addr = *sp
            elif segment == "static":
                self.write("@" + self.file_name + "." + str(index))
                self.write("D=M")
                self.__push_to_stack()
            elif segment == "temp" or segment == "pointer":
                self.write("@R" + str(int(self.addr[segment]) + int(index)))
                self.write("D=M")
                self.__push_to_stack()

        elif command == "C_POP":
            if segment in ["argument", "local", "this", "that"]:
                self.__get_address(index, segment)
                self.write("D=D+M")
                self.write("@R13")
                self.write("M=D")
                self.__pop_from_stack()
                self.write("@R13")
                self.write("A=M")
                self.write("M=D")
            elif segment == 'static':
                self.__pop_from_stack()  # assigns value to D
                self.write('@' + self.file_name + "." + str(index))
                self.write('M=D')
            elif segment == "temp" or segment == "pointer":
                self.__pop_from_stack()
                self.write("@R" + str(int(self.addr[segment]) + int(index)))
                self.write("M=D")

    def __get_address(self, index, segment):
        """

        :param index:
        :param segment:
        :return:
        """
        self.write("@" + str(index))  # access address LCL+index
        self.write("D=A")
        self.write("@" + self.addr[segment])

        # self.__write("A=D")

    def __push_to_stack(self):
        """

        :return:
        """
        self.write("@SP")
        self.write("A=M")
        self.write("M=D")
        self.write("@SP")
        self.write("M=M+1")

    def __pop_from_stack(self):
        """

        :return:
        """
        self.write("@SP")
        self.write("M=M-1")
        self.write("A=M")
        self.write("D=M")

    def write(self, line):
        """
        writes file to text.
        :param line: string which contains an hack command.
        """
        self.file.write(line + "\n")

    def close(self):
        self.file.close()


class VMtranslator:
    """
    Main class for this program.
    """

    def __init__(self, path):
        self.CW = None
        self.file_path = path

    def parse_files(self):
        """

        :return:
        """
        if os.path.isdir(self.file_path):
            path = self.file_path
            # .asm file named after folder
            name = os.path.basename(path)
            self.CW = CodeWriter(path + "/" + name)
            file_list = [file for file in os.listdir(self.file_path)
                         if ".vm" in file]  # create list of vm files
            for item in file_list:
                self.__translate(self.file_path + "/" + item)
        else:
            self.CW = CodeWriter(self.file_path)  # asm file holds one file
            self.__translate(self.file_path)

    def __translate(self, item):
        """

        :return:
        """
        temp_parser = Parser(item)  # create parser
        while temp_parser.has_more_commands():
            temp_parser.advance()
            if temp_parser.command_type() == "C_PUSH" or \
                    temp_parser.command_type() == "C_POP":
                self.CW.write(
                    "// writing:" + temp_parser.command_type() + " " + temp_parser.arg1() + " " + temp_parser.arg2())
                self.CW.write_push_pop(temp_parser.command_type(),
                                       temp_parser.arg1(), temp_parser.arg2())
            else:
                self.CW.write("// writing arithmetic: " + temp_parser.arg1())
                self.CW.write_arithmetic(temp_parser.arg1())
        self.CW.close()


if __name__ == '__main__':
    file_path = sys.argv[1]
    trans = VMtranslator(file_path)
    trans.parse_files()
