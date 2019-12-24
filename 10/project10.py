import os
import sys
import re

class Tokenizer:
    def __init__(self,input_file):
        self.input_file = open(input_file)
        self.lines = [self.clean_line(line) for line in self.input_file.readlines()]
        print(self.lines)
    def clean_line(self,line):
        if '/' == line[0]:
            return
        else:
            return line


    def has_more_tokens(self):
        pass

    def advance(self):
        pass

    def token_type(self):
        pass

    def keyword(self):
        pass

    def symbol(self):
        pass

    def identifier(self):
        pass

    def int_val(self):
        pass

    def string_val(self):
        pass


if __name__ == "__main__":
    file = sys.argv[1]
    mytokenizer = Tokenizer(file)

