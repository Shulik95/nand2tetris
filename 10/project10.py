import os
import sys


class Tokenizer:
    def __init__(self, input_file):
        self.input_file = open(input_file)
        self.lines = []
        self.clean_lines()
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
        self.get_all_tokens()
        print(self.all_tokens)
        self.op = {"+", "-", "*", "/", "&", "|", "<", ">", "="}

    def clean_lines(self):
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

    def get_all_tokens(self):
        for line in self.lines:
            left = 0
            right = 0
            for letter in line:

                if letter not in self.types:
                    right += 1
                else:
                    if right != left:
                        self.all_tokens.append(line[left:right])
                    sign = line[right:right + 1]
                    if sign != ' ':
                        self.all_tokens.append(sign)
                    left = right + 1
                    right = right + 1
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
            return 'integerConstant'
        elif self.curr_token.startswith("\""):
            return 'stringConstant'
        elif self.curr_token in self.types:
            return self.types[self.curr_token]
        else:
            return 'IDENTIFIER'

    def keyword(self):
        return '<keyword> ' + self.curr_token + ' </keyword>\n'

    def symbol(self):
        return '<symbol> ' + self.curr_token + ' </symbol>\n'

    def identifier(self):
        return '<identifier> ' + self.curr_token + ' </identifier>\n'

    def int_val(self):
        return '<integerConstant> ' + self.curr_token + ' </integerConstant>\n'

    def string_val(self):
        return '<stringConstant> ' + self.curr_token[1:-1] + ' </stringConstant>\n'


class CompilationEngine:

    def __init__(self, outputfile, tknz):
        edited_name = outputfile.replace('.jack', '.xml')
        self.file = open(edited_name, 'w')
        self.tknz = tknz

    def cmp_class(self):
        self.file.write('<class>\n')
        self.tknz.advance()
        while self.tknz.has_more_tokens():
            current = self.tknz.curr_token

            if current == 'field' or \
                    current == 'static':
                self.cmp_class_var_dec()

            elif current == 'method' or current == 'function' or \
                    current == 'constructor':
                self.cmp_subroutine_dec()

            elif current == 'var':
                self.cmp_var_dec()

            elif current == 'let':
                self.cmp_let()

            if self.tknz.token_count < len(self.tknz.all_tokens) - 1:
                self.tknz.advance()

        self.file.write('</class>\n')

    def cmp_class_var_dec(self):
        self.file.write('<classVarDec>\n')
        while self.tknz.curr_token != ';':
            suffix = ' </' + self.tknz.token_type().lower() + '> '
            prefix = ' <' + self.tknz.token_type().lower() + '> '
            self.file.write(prefix + self.tknz.curr_token + suffix + '\n')
            self.tknz.advance()
        self.file.write(self.tknz.symbol())
        self.file.write('</classVarDec>\n')

    def peek(self):
        return self.tknz.all_tokens[self.tknz.token_count + 1]

    def cmp_subroutine_dec(self):
        self.file.write('<subroutineDec>\n')
        self.file.write(self.tknz.keyword())
        self.tknz.advance()
        if self.tknz.token_type() == 'IDENTIFIER':
            self.file.write(self.tknz.identifier())
        else:
            self.file.write(self.tknz.keyword())
        self.tknz.advance()
        self.file.write(self.tknz.identifier())
        self.tknz.advance()
        self.file.write(self.tknz.symbol())  # (
        self.cmp_param_lst()
        self.tknz.advance()
        self.file.write(self.tknz.symbol())  # )
        self.tknz.advance()
        self.file.write(self.tknz.symbol())  # {
        self.file.write('</subroutineDec>\n')

    def cmp_param_lst(self):
        self.file.write('<parameterList>\n')
        if self.peek() == ')':
            self.file.write('</parameterList>\n')
            return
        while True:
            self.tknz.advance()
            self.file.write(self.tknz.keyword())
            self.tknz.advance()
            self.file.write(self.tknz.identifier())
            if self.peek() != ')':
                self.tknz.advance()
                self.file.write(self.tknz.symbol())
            else:
                self.file.write('</parameterList>\n')
                break

    def cmp_subroutine_body(self):
        pass

    def cmp_var_dec(self):
        self.file.write('<varDec>\n')
        self.file.write(self.tknz.keyword())
        self.tknz.advance()
        if self.tknz.token_type() == 'IDENTIFIER':
            self.file.write(self.tknz.identifier())
        else:
            self.file.write(self.tknz.keyword())
        self.tknz.advance()
        self.file.write(self.tknz.identifier())
        self.tknz.advance()
        while self.tknz.curr_token == ',':
            self.file.write(self.tknz.symbol())
            self.tknz.advance()
            self.file.write(self.tknz.identifier())
            self.tknz.advance()
        self.file.write(self.tknz.symbol())
        self.file.write('</varDec>\n')

    def cmp_statement(self):
        pass

    def cmp_let(self):
        self.file.write('<letStatement>\n')
        self.file.write(self.tknz.keyword())
        self.tknz.advance()
        self.file.write(self.tknz.identifier())
        if self.peek() == '[':
            self.tknz.advance()
            self.file.write(self.tknz.symbol())  # [
            self.cmp_expression()
            self.tknz.advance()
            self.file.write(self.tknz.symbol())  # ]
        self.tknz.advance()
        self.file.write(self.tknz.symbol())  # =
        self.cmp_expression()
        self.tknz.advance()
        self.file.write(self.tknz.symbol())  # ;
        self.file.write('</letStatement>\n')

    def cmp_if(self):
        pass

    def cmp_while(self):
        pass

    def cmp_do(self):
        pass

    def cmp_return(self):
        pass

    def cmp_expression(self):
        self.file.write("<expression>\n")
        while self.tknz.curr_token in self.tknz.op:
            self.tknz.advance()
            self.cmp_term()

        self.file.write("</expression>\n")

    def cmp_term(self):
        tType = self.tknz.token_type()
        nextT = self.peek()
        self.file.write("<term>\n")
        if tType == "integerConstant":
            self.file.write(self.tknz.int_val())
            if self.tknz.curr_token in self.tknz.op:
                self.file.write(self.tknz.symbol())

        elif tType == "stringConstant":
            if not self.tknz.curr_token.endswith("\""):
                temp = self.__get_whole_str(self.tknz.curr_token)
                self.tknz.curr_token = temp
            self.file.write(self.tknz.string_val())

            if self.tknz.curr_token in self.tknz.op:
                self.file.write(self.tknz.symbol())

        elif tType == "KEYWORD":
            self.tknz.keyword()
        elif tType == "IDENTIFIER":
            self.file.write(self.tknz.identifier())
            self.tknz.advance()
            if self.tknz.curr_token in self.tknz.op:
                self.file.write(self.tknz.symbol())
            if nextT == "[":
                self.term_helper(self.cmp_expression())
            elif nextT == "(":
                self.term_helper(self.cmp_expression_lst())
            elif nextT == ".":
                self.file.write(self.tknz.symbol())  # .
                self.tknz.advance()
                self.file.write(self.tknz.symbol())  # (
                self.cmp_expression_lst()
                self.tknz.advance()
                self.file.write(self.tknz.symbol())  # )
        elif tType == "SYMBOL":
            self.term_helper(self.cmp_expression())
        else:
            self.file.write(self.tknz.symbol())
            self.cmp_term()
        self.file.write("</term>\n")

    def term_helper(self, func):
        self.file.write(self.tknz.symbol())  # [
        self.tknz.advance()
        func()
        self.tknz.advance()
        self.file.write(self.tknz.symbol())  # ]

    def cmp_expression_lst(self):
        pass

    def __get_whole_str(self, temp_str):
        """

        :param temp_str:
        :return:
        """
        while not self.tknz.curr_token.endswith("\""):
            self.tknz.advance()
            temp_str += " " + self.tknz.curr_token
        return temp_str

class JackAnalyzer:
    def __init__(self, jack_file):
        self.file_path = jack_file
        self.engine = None
        self.tknz = None

    def main(self):
        if os.path.isdir(self.file_path):
            path = self.file_path
            name = os.path.basename(path) + '.xml'
            file_list = [file for file in os.listdir(self.file_path)
                         if ".jack" in file]
            for item in file_list:
                self.tknz = Tokenizer(item)
                self.engine = CompilationEngine(name, self.tknz)
                self.engine.cmp_class()
        else:
            self.tknz = Tokenizer(self.file_path)
            self.engine = CompilationEngine(self.file_path, self.tknz)
            self.engine.cmp_class()


if __name__ == "__main__":
    file_or_path = sys.argv[1]
    JA = JackAnalyzer(file_or_path)
    JA.main()
