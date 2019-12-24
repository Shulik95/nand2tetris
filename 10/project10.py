import os
import sys


class Tokenizer:
    def __init__(self, input_file):
        self.input_file = open(input_file)
        self.lines = []
        for line in self.input_file.readlines():
            space_count = 0
            for letter in line:
                if letter == ' ':
                    space_count += 1
                else:
                    line = line[space_count:]
                    break
            if '/' == line[0] or '\n' == line[0] or '*' == line.split(' ')[0] \
                    or '/**' in line:
                continue
            self.lines.append(line.split('//')[0])
        self.all_tokens = []
        self.curr_token = None
        self.token_count = -1
        self.types = \
            {' ': None, '{': 'SYMBOL', '}': 'SYMBOL', '(': 'SYMBOL',
             ')': 'SYMBOL',
             '[': 'SYMBOL', ']': 'SYMBOL', '.': 'SYMBOL', ',': 'SYMBOL',
             ';': 'SYMBOL',
             '+': 'SYMBOL', '-': 'SYMBOL', '*': 'SYMBOL', '/': 'SYMBOL',
             '&': 'SYMBOL',
             '|': 'SYMBOL', '<': 'SYMBOL', '>': 'SYMBOL', '=': 'SYMBOL',
             '~': 'SYMBOL',

             'class': 'KEYWORD', 'constructor': 'KEYWORD',
             'function': 'KEYWORD',
             'method': 'KEYWORD', 'field': 'KEYWORD', 'static': 'KEYWORD',
             'var': 'KEYWORD',
             'int': 'KEYWORD', 'char': 'KEYWORD', 'boolean': 'KEYWORD',
             'void': 'KEYWORD',
             'true': 'KEYWORD', 'false': 'KEYWORD', 'null': 'KEYWORD',
             'this': 'KEYWORD',
             'let': 'KEYWORD', 'do': 'KEYWORD', 'if': 'KEYWORD',
             'else': 'KEYWORD',
             'while': 'KEYWORD', 'return': 'KEYWORD',

             }

    def get_all_tokens(self):
        for line in self.lines:
            l = 0
            r = 0
            for letter in line:
                if letter not in self.types:
                    r += 1
                else:
                    if r != l:
                        self.all_tokens.append(line[l:r])
                    sign = line[r:r + 1]
                    if sign != ' ':
                        self.all_tokens.append(sign)
                    l = r + 1
                    r = r + 1
                continue

    def has_more_tokens(self):
        if self.token_count == len(self.all_tokens) - 1:
            return False
        return True

    def advance(self):
        self.token_count += 1
        self.curr_token = self.all_tokens[self.token_count]

    def token_type(self):
        if self.curr_token.isdigit():
            return 'INT_CONST'
        elif " \" " in self.curr_token:
            return 'STRING_CONST'
        elif self.curr_token in self.types:
            return self.types[self.curr_token]
        else:
            return 'IDENTIFIER'

    def keyword(self):
        return self.curr_token.upper()

    def symbol(self):
        return self.curr_token

    def identifier(self):
        return self.curr_token

    def int_val(self):
        return int(self.curr_token)

    def string_val(self):
        return self.curr_token


class CompilationEngine:

    def __init__(self, outputfile, tknz):
        edited_name = outputfile.replace('.jack', '.xml')
        self.file = open(edited_name, 'w')
        self.tknz = tknz

    def cmp_class(self):
        while self.tknz.has_more_tokens():
            self.tknz.advance()
            mytype = self.tknz.token_type()
            if mytype == 'KEYWORD':
                keytype = self.tknz.keyword()
                if keytype == 'CLASS':
                    pass
                






    def cmp_class_var_dec(self):
        pass

    def cmp_subroutine_dec(self):
        pass

    def cmp_param_lst(self):
        pass

    def cmp_subroutine_body(self):
        pass

    def cmp_var_dec(self):
        pass

    def cmp_statement(self):
        pass

    def cmp_let(self):
        pass

    def cmp_if(self):
        pass

    def cmp_while(self):
        pass

    def cmp_do(self):
        pass

    def cmp_return(self):
        pass

    def cmp_expression(self):
        pass

    def cmp_term(self):
        pass

    def cmp_expression_lst(self):
        pass







class JackAnalyzer:
    pass


if __name__ == "__main__":
    file = sys.argv[1]
    tokenz = Tokenizer(file)
    tokenz.get_all_tokens()
    # while tokenz.has_more_tokens():
    #     tokenz.advance()
    #     print(tokenz.token_type())
