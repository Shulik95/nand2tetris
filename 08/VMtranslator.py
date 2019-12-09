import os
import sys


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
            if "/" == line[0] or "\n" == line[
                0]:  # clear comments & empty lines
                continue
            line = line.split('//')[0]

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
            "pop": "C_POP",

            "label": 'C_LABEL',
            "goto": 'C_GOTO',
            'if-goto': 'C_IF',
            "function": 'C_FUNCTION',
            "return": 'C_RETURN',
            "call": 'C_CALL'
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
        Returns the type of the current VM command.
        :return:command type.
        """
        temp_line = self.clean_line()
        return self.__command_dict[temp_line[0]]

    def arg1(self):
        """
        returns the first argument of the current command. in the case of
        C_ARITHMETIC the command itself is returned.
        """
        if self.command_type() in ["C_ARITHMETIC",
                                   'C_RETURN']:  # RETURN MIGHT NOT BELONG HERE~!!!@# HAVE TO CHECK FURTHER
            return self.clean_line()[0]  # arithmetic or return command
        else:  # either push, pop, label, goto, if-goto, function or call
            return self.clean_line()[1]

    def arg2(self):
        """
        returns the second argument of the current command. only called for
        specific command types.
        """
        return self.clean_line()[2]

    def clean_line(self):
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
        edited_name = output_file.replace(".vm", ".asm")
        self.file = open(edited_name, "w")
        self.addr = {"local": "LCL",
                     "argument": "ARG",
                     "this": "THIS",
                     "that": "THAT",
                     "static": "STATIC",
                     "temp": 5,
                     "pointer": 3
                     }

        self.file_name = output_file.split("/")[-1]
        self.__acounter = 0
        self.__ccounter = 0
        self.isfunc = False

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
        Handles all arithmetic action which are unary, performed on one
        variable only.
        :param command: the arithmetic operator.
        """
        self.__pop_from_stack()
        if command == "not":
            self.write("D=!D")
        else:  # action has to be neg
            self.write("D=-D")
        self.__push_to_stack()

    def __two_var(self, command):
        """
        Handles all arithmetic binary operators.
        :param command: the arithmetic operator.
        :return:
        """
        self.__pop_from_stack()  # store y in D
        self.write("@SP")
        self.write("M=M-1")
        self.write("A=M")  # point to RAM holding x.

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
            self.write(("@JUMP" + self.__acounter.__str__()))
            self.write("M=-1")
            #  cases:
            if command == "eq":  # check if x = y
                self.write("D;JEQ")

            elif command == "gt":  # check if x > y
                self.write("D;JGT")  # A will be 1

            else:  # check if x < y because command has to be "lt"
                self.write("D;JLT")
            # common lines
            self.write("@NJUMP" + self.__acounter.__str__())
            self.write("M=0")
            self.write("0;JMP")
            # creates jump label in case command is true:
            self.write("(JUMP" + self.__acounter.__str__() + ")")
            # creates label for case the command is false
            self.write("(NJUMP" + self.__acounter.__str__() + ")")
            self.write("D=M")
            #  D holds either 1 or 0, push D to stack now.
            self.__push_to_stack()
            self.__acounter += 1  # advance counter for further use.

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

    def write_label(self, label):
        if not self.isfunc:
            if label[-1] == '\n':
                my_str = '(' + label[:-1] + ')'
            else:
                my_str = '(' + label + ')'
            self.write(my_str)
        else:
            pass

    def write_goto(self, goto):
        self.write('@' + goto)
        self.write('0;JMP')

    def write_ifgoto(self, ifgoto):
        """
        """
        self.write('@SP')
        self.write('A=M-1')
        self.write('D=M')
        self.write('@SP')
        self.write('M=M-1')
        self.write('@' + ifgoto)
        self.write('D;JNE')

    def write_function(self, fname, nargs):
        self.write_label(fname)
        for i in range(nargs):
            self.write('@R0')
            self.write('D=A')
            self.__push_to_stack()

    def write_call(self, fname, nargs):
        self.write('@RETURN' + str(self.__ccounter))  # push return address
        self.write('D=A')
        self.__push_to_stack()
        for item in ['@LCL', '@ARG', '@THIS', '@THAT']:
            self.write(item)
            self.write("D=M")
            self.__push_to_stack()

        self.write('@5')  # arg=sp-5-nargs
        self.write('D=A')
        self.write('@' + str(nargs))
        self.write('D=D+A')
        self.write('@SP')
        self.write('D=M-D')
        self.write('@ARGS')
        self.write('M=D')

        self.write('@SP')  # LCL=SP
        self.write('D=M')
        self.write('@LCL')
        self.write('M=D')

        self.write_goto(fname)  # goto fname

        self.write_label('@RETURN' + str(self.__ccounter))  # declare label
        self.__ccounter += 1

    def write_return(self):
        pass

    def __get_address(self, index, segment):
        """
        creates an address according to format.
        :param index: the index in the segment.
        :param segment: the specific segment.
        """
        self.write("@" + str(index))  # access address LCL+index
        self.write("D=A")
        self.write("@" + self.addr[segment])

    def __push_to_stack(self):
        """
        Pushes value into the stack, method assumes the value is already
        stored in the D register. increments SP pointer.
        """
        self.write("@SP")
        self.write("A=M")
        self.write("M=D")
        self.write("@SP")
        self.write("M=M+1")

    def __pop_from_stack(self):
        """
        Pops value from stack into D register.
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
        Parses each file in given folder and translates it into hack code.
        Each files is translated by a different parser but all files are
        translated into the same .asm file.
        """
        if os.path.isdir(self.file_path):
            path = self.file_path
            name = os.path.basename(path) + '.asm'
            # .asm file named after folder
            self.CW = CodeWriter(path + "/" + name)
            file_list = [file for file in os.listdir(self.file_path)
                         if ".vm" in file]  # create list of vm files
            for item in file_list:
                self.__translate(self.file_path + "/" + item)
        else:
            self.CW = CodeWriter(self.file_path)  # path holds one file
            self.__translate(self.file_path)
        self.CW.close()

    def __translate(self, item):
        """
        translates a given file from vm to hack code.
        """
        temp_parser = Parser(item)  # create parser
        while temp_parser.has_more_commands():
            temp_parser.advance()  # get next command
            if temp_parser.command_type() == "C_PUSH" or \
                    temp_parser.command_type() == "C_POP":
                self.CW.write(
                    "// writing:" + temp_parser.command_type() +
                    " " + temp_parser.arg1() + " " + temp_parser.arg2())
                self.CW.write_push_pop(temp_parser.command_type(),
                                       temp_parser.arg1(), temp_parser.arg2())
            elif temp_parser.command_type() == "C_ARITHMETIC":
                self.CW.write("// writing arithmetic: " + temp_parser.arg1())
                self.CW.write_arithmetic(temp_parser.arg1())
            elif temp_parser.command_type() == "C_LABEL":
                self.CW.write("// writing label: " + temp_parser.arg1())
                self.CW.write_label(temp_parser.arg1())
            elif temp_parser.command_type() == "C_GOTO":
                self.CW.write("// writing goto: " + temp_parser.arg1())
                self.CW.write_goto(temp_parser.arg1())
            elif temp_parser.command_type() == "C_IF":
                self.CW.write("// writing if-goto: " + temp_parser.arg1())
                self.CW.write_ifgoto(temp_parser.arg1())


if __name__ == '__main__':
    file_path = sys.argv[1]
    translator = VMtranslator(file_path)
    translator.parse_files()
