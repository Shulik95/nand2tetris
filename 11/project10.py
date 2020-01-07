import os
import sys
from JackCompiler import SymbolTable as st


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
        self.op = {"+", "-", "*", "/", "&", "|", "<", ">", "="}
        self.key_const = {"true", "false", "null", "this"}

    def clean_lines(self):
        """
        cleans each line, removing spaces and in line comments.
        """
        for line in self.input_file.readlines():
            if "\t" in line:
                line = line.replace("\t", '')
            space_count = 0
            for letter in line:
                if letter == ' ':
                    space_count += 1
                else:
                    line = line[space_count:]
                    break
            if '/' == line[0] or '\n' == line[0] or '*' == line.split(' ')[0] \
                    or '/**' in line or "*" == line[0]:  # lines doesnt contain code
                continue
            self.lines.append(line.split('//')[0])

    def get_all_tokens(self):
        """
        breaks all lines into tokens for further use.
        """
        for line in self.lines:
            left = 0
            right = 0
            for letter in line:
                if letter == "\n" and left != right:
                    self.all_tokens.append(line[left:right])
                elif letter not in self.types:
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
        """
        checks if all tokens have been checked and compiled.
        :return: false if we are done, true otherwise.
        """
        if self.token_count == len(self.all_tokens) - 1:
            return False
        return True

    def advance(self):
        """
        moves on to the next token.
        """
        self.token_count += 1
        self.curr_token = self.all_tokens[self.token_count]

    def token_type(self):
        """
        gets the token type.
        """
        if self.curr_token.isdigit():
            return 'integerConstant'
        elif self.curr_token.startswith("\""):
            return 'stringConstant'
        elif self.curr_token in self.types:
            return self.types[self.curr_token]
        else:
            return 'IDENTIFIER'

    def keyword(self):
        """
        :return: an in format xml line.
        """
        return '<keyword> ' + self.curr_token + ' </keyword>\n'

    def symbol(self):
        """
        :return: an in format xml line.
        """
        if self.curr_token == ">":
            self.curr_token = "&gt;"
        elif self.curr_token == "<":
            self.curr_token = "&lt;"
        elif self.curr_token == "&":
            self.curr_token = "&amp;"
        elif self.curr_token == "\'":
            self.curr_token = "&quot;"
        return '<symbol> ' + self.curr_token + ' </symbol>\n'

    def identifier(self):
        """
        :return: an in format xml line.
        """
        return '<identifier> ' + self.curr_token + ' </identifier>\n'

    def int_val(self):
        """
        :return: an in format xml line.
        """
        return '<integerConstant> ' + self.curr_token + ' </integerConstant>\n'

    def string_val(self):
        """
        :return: an in format xml line.
        """
        return '<stringConstant> ' + self.curr_token[1:-1] + ' </stringConstant>\n'


class CompilationEngine:

    def __init__(self, outputfile, tknz):
        edited_name = outputfile.replace('.jack', '.xml')
        self.file = open(edited_name, 'w')
        self.tknz = tknz

    def cmp_class(self):
        """
        compiles an entire class using pre-made methods.
        """
        self.file.write('<class>\n')
        self.tknz.advance()
        self.file.write(self.tknz.keyword())  # writes 'class'
        self.tknz.advance()
        self.file.write(self.tknz.identifier())  # writes class name
        self.tknz.advance()
        self.file.write(self.tknz.symbol())  # "{"
        while self.peek() in ['static', 'field']:  # checks for class variables
            self.tknz.advance()
            self.cmp_class_var_dec()
        while self.peek() in ['method', 'function', 'constructor']:
            self.tknz.advance()
            self.cmp_subroutine_dec()
        self.tknz.advance()
        self.file.write(self.tknz.symbol())  # "}"
        self.file.write('</class>\n')

    def cmp_class_var_dec(self):
        """
        compiles all class variables.
        """
        self.file.write('<classVarDec>\n')
        self.file.write(self.tknz.keyword())
        self.tknz.advance()
        if self.tknz.curr_token in ['int', 'char', 'boolean']:
            self.file.write(self.tknz.keyword())
        else:
            self.file.write(self.tknz.identifier())
        self.tknz.advance()
        self.file.write(self.tknz.identifier())
        while self.peek() == ",":
            self.tknz.advance()  # moves to ','
            self.file.write(self.tknz.symbol())
            self.tknz.advance()
            self.file.write(self.tknz.identifier())
        self.tknz.advance()  # moves to ';'
        self.file.write(self.tknz.symbol())
        self.file.write('</classVarDec>\n')

    def peek(self):
        """
        peeks one token ahead. used for LL(1)
        """
        try:
            return self.tknz.all_tokens[self.tknz.token_count + 1]
        except IndexError:
            return -1  # no more values, end of token list

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
        self.cmp_subroutine_body()
        self.file.write('</subroutineDec>\n')

    def cmp_param_lst(self):
        """
        compiles the parameter list for a given method, separated by commas.
        """
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
        """
        compiles an entire subroutine body, including method variables and
        and inner statements.
        """
        self.file.write("<subroutineBody>\n")
        self.file.write(self.tknz.symbol())  # "{"
        while self.peek() == "var":  # has more method variables
            self.tknz.advance()
            self.cmp_var_dec()
        self.tknz.advance()
        self.cmp_statement()
        self.file.write(self.tknz.symbol())  # "}"
        self.file.write("</subroutineBody>\n")

    def cmp_var_dec(self):
        """
        compiles variable decelerations in methods.
        """
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
        """
        compiles a given set of statements, handles all different kinds of
        statements according to the api.
        """
        self.file.write("<statements>\n")
        while self.tknz.curr_token != "}":  # checks if more statements exist.
            self.__cmp_stat_helper()
            self.tknz.advance()
        self.file.write("</statements>\n")

    def __cmp_stat_helper(self):
        """
        an helper method which filters the current statement and calles fitting
        method.
        """
        curr_statement = self.tknz.curr_token
        if curr_statement == "do":
            self.cmp_do()
        elif curr_statement == "let":
            self.cmp_let()
        elif curr_statement == "while":
            self.cmp_while()
        elif curr_statement == "return":
            self.cmp_return()
        else:
            self.cmp_if()

    def cmp_let(self):
        """
        compiles a let statement.
        """
        self.file.write('<letStatement>\n')
        self.file.write(self.tknz.keyword())
        self.tknz.advance()
        self.file.write(self.tknz.identifier())
        if self.peek() == '[':
            self.tknz.advance()
            self.file.write(self.tknz.symbol())  # [
            self.tknz.advance()
            self.cmp_expression()
            self.file.write(self.tknz.symbol())  # ]
        self.tknz.advance()
        self.file.write(self.tknz.symbol())  # =
        self.tknz.advance()
        self.cmp_expression()
        self.file.write(self.tknz.symbol())  # ;
        self.file.write('</letStatement>\n')

    def cmp_if(self):
        """
        compiles an 'if' statement.
        """
        self.file.write("<ifStatement>\n")
        self.file.write(self.tknz.keyword())  # writes 'if'
        self.tknz.advance()
        self.file.write(self.tknz.symbol())  # (
        self.tknz.advance()
        self.cmp_expression()
        self.file.write(self.tknz.symbol())  # )
        self.__brack_and_statment()

        if self.peek() == "else":
            self.tknz.advance()
            self.file.write(self.tknz.keyword())  # writes else
            self.__brack_and_statment()

        self.file.write("</ifStatement>\n")

    def __brack_and_statment(self):
        """
        helper method for repating lines of code during if statements
        """
        self.tknz.advance()
        self.file.write(self.tknz.symbol())  # {
        self.tknz.advance()
        self.cmp_statement()
        self.file.write(self.tknz.symbol())  # }

    def cmp_while(self):
        """
        compiles a while statement.
        """
        self.file.write("<whileStatement>\n")
        self.file.write(self.tknz.keyword())  # writes 'while'
        self.tknz.advance()
        self.file.write(self.tknz.symbol())  # (
        self.tknz.advance()
        self.cmp_expression()
        self.file.write(self.tknz.symbol())  # )
        self.__brack_and_statment()
        self.file.write("</whileStatement>\n")

    def cmp_do(self):
        """
        compiles do statements.
        """
        self.file.write("<doStatement>\n")
        self.file.write(self.tknz.keyword())
        self.tknz.advance()
        self.file.write(self.tknz.identifier())  # print subroutine or class name
        nextT = self.peek()
        self.subRoutineCall(nextT)
        self.tknz.advance()
        self.file.write(self.tknz.symbol())  # compiles ;
        self.file.write("</doStatement>\n")

    def cmp_return(self):
        """
        compiles a return statement, handles both cases. with expressions or
        expressionless.
        """
        self.file.write("<returnStatement>\n")
        self.file.write(self.tknz.keyword())  # writes 'return'
        if self.peek() != ";":  # has expressions
            self.tknz.advance()
            self.cmp_expression()
        else:  # no expressions
            self.tknz.advance()
        self.file.write(self.tknz.symbol())
        self.file.write("</returnStatement>\n")

    def cmp_expression(self):
        """
        compiles an expression, supports complex expressions.
        """
        self.file.write("<expression>\n")  #
        self.cmp_term()
        while self.tknz.curr_token in self.tknz.op:
            self.file.write(self.tknz.symbol())
            self.tknz.advance()
            self.cmp_term()
        self.file.write("</expression>\n")

    def cmp_term(self):
        """
        breaks each expression down into term and compiles them accordingly.
        """
        tType = self.tknz.token_type()
        nextT = self.peek()
        self.file.write("<term>\n")
        if tType == "integerConstant":
            self.file.write(self.tknz.int_val())  # writes integer
            self.tknz.advance()  # advances to ';'

        elif tType == "stringConstant":
            if not self.tknz.curr_token.endswith("\""):  # checks for str const
                temp = self.__get_whole_str(self.tknz.curr_token)
                self.tknz.curr_token = temp  # whole string const with spaces
            self.file.write(self.tknz.string_val())
            self.tknz.advance()
        elif tType == "IDENTIFIER":
            self.file.write(self.tknz.identifier())
            if nextT == "[":
                self.tknz.advance()
                self.term_helper(self.cmp_expression)
            self.subRoutineCall(nextT)
            self.tknz.advance()
        elif tType == "SYMBOL":
            self.term_helper(self.cmp_expression)
            if self.tknz.curr_token in ["-", "~"]:  # unary op ahead
                self.tknz.advance()
                self.cmp_term()
            else:
                self.tknz.advance()
        elif tType == "KEYWORD":
            self.file.write(self.tknz.keyword())
            self.tknz.advance()
        self.file.write("</term>\n")

    def subRoutineCall(self, nextT):
        """
        compiles a subroutine call
        :param nextT: the next token, helps determine which case were in.
        """
        if nextT == "(":
            self.tknz.advance()
            self.term_helper(self.cmp_expression_lst)

        elif nextT == ".":
            self.tknz.advance()
            self.file.write(self.tknz.symbol())  # .
            self.tknz.advance()
            self.file.write(self.tknz.identifier())  # writes subroutine name
            self.tknz.advance()
            self.file.write(self.tknz.symbol())  # (
            self.tknz.advance()
            self.cmp_expression_lst()
            self.file.write(self.tknz.symbol())  # )

    def term_helper(self, func):
        """
        a helper method for term compiling
        :param func: a function which writes a specific part of code
        """
        self.file.write(self.tknz.symbol())  # [ / (
        if self.tknz.curr_token not in ["-", "~"]:  # unary op ahead
            self.tknz.advance()
            func()
            self.file.write(self.tknz.symbol())  # ] / )

    def cmp_expression_lst(self):
        """
        compiles a list of expressions, separated by commas.
        """
        self.file.write("<expressionList>\n")
        if self.tknz.curr_token != ")":
            while True:
                self.cmp_expression()  # compiles expression
                if self.tknz.curr_token == ")":  # done with exp list
                    break
                self.file.write(self.tknz.symbol())  # compiles either ',' or ')' if done
                self.tknz.advance()
        self.file.write("</expressionList>\n")

    def __get_whole_str(self, temp_str):
        """
        a helper method for cases which contain string constants with spaces
        :param temp_str: the current part of the string.
        :return: the full string const, with spaces.
        """
        while not self.tknz.curr_token.endswith("\""):
            self.tknz.advance()
            temp_str += " " + self.tknz.curr_token
        return temp_str


class JackAnalyzer:
    """
    The main class of the program. for each .jack file we create a tokenizer
    and CompileEngine and compile the file. a XML file with the compiled
    file name will be outputted.
    """
    def __init__(self, jack_file):
        self.file_path = jack_file
        self.engine = None
        self.tknz = None

    def main(self):
        if os.path.isdir(self.file_path):
            path = self.file_path

            file_list = [file for file in os.listdir(self.file_path)
                         if ".jack" in file]
            for item in file_list:
                self.tknz = Tokenizer(path + '/' + item)
                self.engine = CompilationEngine(path + '/' + item, self.tknz)
                self.engine.cmp_class()
        else:
            self.tknz = Tokenizer(self.file_path)
            self.engine = CompilationEngine(self.file_path, self.tknz)
            self.engine.cmp_class()


if __name__ == "__main__":
    file_or_path = sys.argv[1]
    JA = JackAnalyzer(file_or_path)
    JA.main()
