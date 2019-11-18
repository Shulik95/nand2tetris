import sys, os, copy

# A dictionary holding all computation values.
comp = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
}

# A dictionary holding all destination values
dest = {
    "null": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}

jump = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JNP": "111"
}

symbols = {
    "SP": "0",
    "LCL": "1",
    "ARG": "2",
    "THIS": "3",
    "THAT": "4",
    "R0": "0",
    "R1": "1",
    "R2": "2",
    "R3": "3",
    "R4": "4",
    "R5": "5",
    "R6": "6",
    "R7": "7",
    "R8": "8",
    "R9": "9",
    "R10": "10",
    "R11": "11",
    "R12": "12",
    "R13": "13",
    "R14": "14",
    "R15": "15",
    "SCREEN": "16384",
    "KBD": "24576"
}


# filename = sys.argv[1]  # get the name of the file to translate


def clean_line(line):
    """
    This function clears away all white space from the line. white space
    includes in line comments and comment lines.
    :param line: The line to clear.
    :return: A string which is the clear version of its input.
    """

    cleaned = ""  # an empty string for adding chars
    for char in line:
        if char == "/":
            cleaned += ""
            break  # no need to keep iterating, only line comments left.
        elif char == "\n" or char == " ":
            cleaned += ""
        else:
            cleaned += char
    return cleaned


def get_instruction_type(line):
    """
    Receives a cleaned line and determines the type of the instruction,
    calls the appropriate function to deal with the instruction.
    :param line: a line with no white-spaces.
    :return: the binary representation of the command.
    """
    if line[0] == "@":
        return a_instruction(line[1:])  # remove the "@".
    else:
        return c_instruction(line)


def a_instruction(line: str) -> str:
    """
    This function translates a line into a legal A-instruction. starts with
    checking if we got a number or a variable. than handles each of the cases
    accordingly. we assume all symbols have been already added in the first
    run over
    :param line: a line containing an A-instruction. where @ is removed.
    :return: returns the binary representation of the instruction.
    """
    if line.isdigit():
        # returns the binary value in 16 bits.
        final_val = line
    else:
        final_val = symbols.get(line)  # get symbol val from table.
    return bin(int(final_val))[2:].zfill(16)


def c_instruction(line):
    """
    Receives a line which describes a C-instruction. translates into the
    needed format.
    :param line: a line containing a C-instruction, no white-spaces.
    :return: returns a 16 bit bus representing the instruction.
    """

    formated = c_helper(line)
    temp1 = formated.split("=")  # get dest from string.
    destination = temp1[0]
    compute, jmp = temp1[1].split(";")  # get comp and jmp
    binfinal = "111" + dest[destination] + comp[compute] + jump[jmp]
    return binfinal  # returns binary rep of C-instruction


def c_helper(line):
    """
    this function is an helper for the C-instruction translator, it puts a
    line into the "dest=comp;jump" formation, which makes it easy to deal with
    different instruction.
    :param line: a line cleaned from white-space.
    :return: returns a C-instruction in "dest=comp;jump" format.
    """
    if "=" not in line:
        line = "null=" + line
    elif ";" not in line:
        line += ";null"
    return line


def read_asm(filename):
    """

    :param filename:
    :return:
    """
    f = open(filename)
    all_lines = f.readlines()
    lines = [line for line in all_lines]  # create a list of all text lines.
    return lines

def write_hack(filename):
    """

    :param filename:
    :return:
    """
    pass


if __name__ == "__main__":
    print(clean_line("shulik //asdafsag"))
