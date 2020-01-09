import os
import sys


class SymbolTable:
    """
    This class creates objects which manage the symbols
    of methods and classes.
    """

    def __init__(self):
        """
        Creates SymbolTable object.
        """
        self.class_level = {}
        self.subroutine_level = {}
        self.curr_scope = self.class_level  # starts from global level
        self.var_counter = 0
        self.static_counter = 0
        self.field_counter = 0
        self.arg_counter = 0

    def startSubroutine(self):
        """
        Starts a new Subroutine scope (resets former one if it exists).
        """
        self.curr_scope = self.subroutine_level  # change to sub level
        self.subroutine_level = {}  # clears dictionary
        self.var_counter = 0
        self.arg_counter = 0

    def define(self, name, type, kind):
        """
        Define a new identifier of the given name, type and kind, and assigns
        it a running index. STATIC and FIELD identifiers have a class scope,
        while ARG and VAR have a subroutine scope.
        """
        if kind == 'static':
            self.class_level[name] = [type, kind, self.static_counter]
            self.static_counter += 1
        elif kind == 'field':
            self.class_level[name] = [type, kind, self.field_counter]
            self.field_counter += 1
        elif kind == 'argument':
            self.subroutine_level[name] = [type, kind, self.arg_counter]
            self.arg_counter += 1
        else:
            self.subroutine_level[name] = [type, kind, self.var_counter]
            self.var_counter += 1

    def varCount(self, kind):
        """
        Returns the number of variables of the given kind already defined in
        the current scope.
        :param kind: kind of the variable
        """
        if kind == 'static':
            return self.static_counter
        elif kind == 'field':
            return self.field_counter
        elif kind == 'arg':
            return self.arg_counter
        else:
            return self.var_counter

    def kindOf(self, name):
        """
        Returns the kind of the named identifier in the current scope.
        if the identifier is unknown in the current scope, returns NONE
        """
        if name in self.subroutine_level:  # checks global or local
            return self.subroutine_level[name][1]
        elif name in self.class_level:
            return self.class_level[name][1]
        return None

    def typeOf(self, name):
        """
        Returns the type of the named identifier in the current scope.
        """
        if name in self.subroutine_level:
            return self.subroutine_level[name][0]
        elif name in self.class_level:
            return self.class_level[name][0]

    def indexOf(self, name):
        """
        Returns the index assigned to the named identifier.
        """
        if name in self.subroutine_level:
            return self.subroutine_level[name][2]
        elif name in self.class_level:
            return self.class_level[name][2]


class VMWriter:
    """
    This class writes VM commands into a file. It encapsulates the VM
    command syntax.
    """

    def __init__(self, outputFile):
        """
        Creates a new file and prepares for writing VM commands.
        :param outputFile: name of output file
        """
        self.file = open(outputFile, 'w')

    def writePush(self, segment, index):
        """
        Writes a VM pop command.
        """
        self.file.write("push " + segment + " " + str(index) + "\n")

    def writePop(self, segment, index):
        """
        Write a VM pop command.
        """
        self.file.write("pop " + segment + " " + str(index) + "\n")

    def writeArithmetic(self, command):
        """
        Writes a VM arithmetic command.
        """
        self.file.write(command + "\n")

    def writeLabel(self, label):
        """
        Writes a VM label command.
        """
        self.file.write("label " + label + "\n")

    def writeGoto(self, label):
        """
        writes a VM goto command.
        """
        self.file.write("goto " + label + "\n")

    def writeIf(self, label):
        """
        Writes a VM if-goto command.
        """
        self.file.write("if-goto " + label + "\n")

    def writeCall(self, name, nArgs):
        """
        Writes a VM call command.
        """
        self.file.write("call " + name + " " + str(nArgs) + "\n")

    def writeFunction(self, name, nLocals):
        """
        Writes a VM function command.
        """
        self.file.write("function " + name + " " + str(nLocals) + "\n")

    def writeReturn(self):
        """
        Writes a VM return command.
        """

        self.file.write("return\n")

    def close(self):
        """
        Closes the output file.
        """
        self.file.close()


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
        self.un_op = {"-", "~"}
        self.bin_op = {"+", "*", "/", "&", "|", "<", ">", "="}
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
                    or '/**' in line or "*" == line[
                0]:  # lines doesnt contain code
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
        return '<stringConstant> ' + self.curr_token[
                                     1:-1] + ' </stringConstant>\n'


class CompilationEngine:
    """
    compiles code from jack to VM.
    """

    def __init__(self, outputfile, tknz):
        self.VMW = VMWriter(outputfile.replace("jack", "vm"))
        self.tknz = tknz
        self.symbol = SymbolTable()
        self.className = ""
        self.methodName = ""
        self.op_lst = []
        self.if_counter = 0
        self.while_counter = 0
        self.expression_count = 0

    def cmp_class(self):
        """
        compiles an entire class using pre-made methods.
        """
        self.tknz.advance()  # points to class keyword
        self.className = self.peek()  # saves class name
        self.tknz.advance()
        self.tknz.advance()  # points to "{"
        while self.peek() in ["field", "static"]:
            self.tknz.advance()
            self.cmp_class_var_dec()
        while self.peek() in ['method', 'function', 'constructor']:
            self.tknz.advance()
            self.cmp_subroutine_dec()
        self.tknz.advance()

    def cmp_class_var_dec(self):
        """
        compiles all class variables.
        """
        kind = self.tknz.curr_token  # saves kind
        self.tknz.advance()
        type = self.tknz.curr_token  # saves type
        self.tknz.advance()
        name = self.tknz.curr_token  # saves name
        self.symbol.define(name, type, kind)
        while self.peek() == ",":
            self.tknz.advance()  # moves to ','
            self.tknz.advance()
            name = self.tknz.curr_token  # save next name
            self.symbol.define(name, type, kind)
        self.tknz.advance()  # moves to ";"

    def peek(self):
        """
        peeks one token ahead. used for LL(1)
        """
        try:
            return self.tknz.all_tokens[self.tknz.token_count + 1]
        except IndexError:
            return -1  # no more values, end of token list

    def cmp_subroutine_dec(self):
        """
        compiles a subroutines declaration.
        """
        func_type = self.tknz.curr_token  # saves constructor/method/function
        self.tknz.advance()  # func/method return type
        self.tknz.advance()  # points to method name.
        self.methodName = self.tknz.curr_token  # saves method name
        self.symbol.startSubroutine()  # reset lower level table.
        self.tknz.advance()  # "("
        if func_type == "constructor":
            self.VMW.writeFunction(self.className + "." + self.methodName, 0)
            self.cmp_param_lst()  # adds arguments to table
            self.VMW.writePush("constant", self.symbol.varCount("field"))
            self.VMW.writeCall("Memory.alloc", 1)
            self.VMW.writePop("pointer", 0)  # assigns object to "this"
            self.tknz.advance()
        elif func_type == "method":
            self.symbol.define("this", self.className,
                               "argument")  # adds obj reference
            self.cmp_param_lst()  # adds arguments to table
            self.tknz.advance()  # {
            if self.peek() == "var":
                while self.peek() == "var":
                    self.cmp_var_dec()  # curr is ";"
            else:
                self.tknz.advance()
            self.VMW.writeFunction(self.className + "." + self.methodName,
                                   self.symbol.varCount("var"))
            self.VMW.writePush("argument", 0)  # pushes the object to stack
            self.VMW.writePop("pointer", 0)  # assigns object to "this"
        else:
            self.cmp_param_lst()  # returns curr == ")"
            self.tknz.advance()  # {
            if self.peek() == "var":
                while self.peek() == "var":
                    self.cmp_var_dec()  # curr is ";"
            else:
                self.tknz.advance()
            self.VMW.writeFunction(self.className + "." + self.methodName,
                                   self.symbol.varCount("var"))  # function
        self.cmp_subroutine_body()

    def cmp_param_lst(self):
        """
        compiles the parameter list for a given method, separated by commas.
        """
        if self.peek() == ')':  # no arguments are sent into this function
            self.tknz.advance()
            return
        kind = "argument"  # constant for param list
        while True:
            self.tknz.advance()  # points to type
            tempType = self.tknz.curr_token
            self.tknz.advance()  # points to VarName
            tempName = self.tknz.curr_token
            self.symbol.define(tempName, tempType, kind)  # add to table.
            if self.peek() != ')':
                self.tknz.advance()  # advances to ","
            else:
                self.tknz.advance()  # points to ")"
                break

    def cmp_subroutine_body(self):
        """
        compiles an entire subroutine body, including method variables and
        and inner statements.
        """
        self.tknz.advance()  # some statement
        self.cmp_statement()

    def cmp_var_dec(self):
        """
        compiles variable decelerations in methods.
        """
        kind = "local"  # constant for subroutine vars
        self.tknz.advance()  # var
        self.tknz.advance()  # type
        type = self.tknz.curr_token
        self.tknz.advance()
        name = self.tknz.curr_token
        self.symbol.define(name, type, kind)  # adds to table
        self.tknz.advance()  # either "," or ";"
        while self.tknz.curr_token == ',':
            self.tknz.advance()  # get another name
            name = self.tknz.curr_token
            self.symbol.define(name, type, kind)
            self.tknz.advance()  # next "," or ";"

    def cmp_statement(self):
        """
        compiles a given set of statements, handles all different kinds of
        statements according to the api.
        """

        while self.tknz.curr_token != "}":  # checks if more statements exist.
            self.__cmp_stat_helper()
            self.tknz.advance()

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
        self.tknz.advance()  # moves to var name
        kind = self.symbol.kindOf(self.tknz.curr_token)
        index = self.symbol.indexOf(self.tknz.curr_token)
        if self.peek() == '[':
            self.tknz.advance()
            self.file.write(self.tknz.symbol())  # [
            self.tknz.advance()
            self.cmp_expression()
            self.file.write(self.tknz.symbol())  # ]
        self.tknz.advance()  # =
        self.tknz.advance()  # enters expression
        self.cmp_expression()  # returns when curr = ";"
        self.VMW.writePop(kind, index)

    def cmp_if(self):
        """
        compiles an 'if' statement.
        """
        self.if_counter += 1
        self.tknz.advance()  # (
        if self.peek() in self.tknz.un_op:
            self.tknz.advance()
            self.cmp_expression()
        else:
            self.tknz.advance()  # enters expression
            self.cmp_expression()  # return when curr = ")"
        self.VMW.writeArithmetic("not")
        self.VMW.writeIf(
            'IF_FALSE' + str(self.if_counter))  # condition is upheld
        tlabel = self.if_counter
        self.__brack_and_statment()
        self.VMW.writeGoto("IF_TRUE" + str(tlabel))
        if self.peek() == "else":
            self.VMW.writeLabel(
                'IF_FALSE' + str(tlabel))  # creates 2nd label
            self.tknz.advance()
            self.__brack_and_statment()
        self.VMW.writeLabel('IF_TRUE' + str(self.if_counter))
        # self.VMW.writeGoto("IF_END" + str(self.if_counter))
        # self.VMW.writeLabel("IF_END" + str(self.if_counter))

    def __brack_and_statment(self):
        """
        helper method for repating lines of code during if statements
        """
        self.tknz.advance()  # {
        self.tknz.advance()  # inside statements
        self.cmp_statement()

    def cmp_while(self):
        """
        compiles a while statement.
        """
        self.while_counter += 1

        self.tknz.advance()  # (
        self.VMW.writeLabel("WHILE-TRUE" + str(self.while_counter))
        self.tknz.advance()  # into expression
        self.cmp_expression()
        self.VMW.writeArithmetic("not")
        # tLable = "WHILE-TRUE" + str(self.while_counter)
        # self.while_counter += 1
        self.VMW.writeIf("WHILE-FALSE" + str(self.while_counter))
        self.tknz.advance()  # {
        self.tknz.advance()  # inside statements
        self.cmp_statement()
        self.VMW.writeGoto(
            "WHILE-TRUE" + str(self.while_counter))  # goes back to loop
        # expression isn't upheld, skip statements
        self.VMW.writeLabel("WHILE-FALSE" + str(self.while_counter))

    def cmp_do(self):
        """
        compiles do statements.
        """
        self.tknz.advance()
        # print subroutine or class name
        nextT = self.peek()
        self.subRoutineCall(nextT)  # curr = ")"
        self.tknz.advance()
        self.VMW.writePop("temp", 0)

    def cmp_return(self):
        """
        compiles a return statement, handles both cases. with expressions or
        expressionless.
        """
        if self.peek() != ";":  # has expressions
            self.tknz.advance()
            self.cmp_expression()
        else:  # no expressions
            self.VMW.writePush("constant", 0)
            self.tknz.advance()
        self.VMW.writeReturn()

    def cmp_expression(self):
        """
        compiles an expression, supports complex expressions.
        """
        self.cmp_term()
        while self.tknz.curr_token in self.tknz.bin_op:
            op = self.tknz.curr_token
            if op == '+':
                self.op_lst.append('add')
            elif op == '-':
                self.op_lst.append('sub')
            elif op == '|':
                self.op_lst.append('or')
            elif op == '&':
                self.op_lst.append('and')
            elif op == '=':
                self.op_lst.append('eq')
            elif op == '<':
                self.op_lst.append('lt')
            elif op == '>':
                self.op_lst.append('gt')
            elif op == '*':
                self.op_lst.append(('Math.multiply', 2))
            elif op == '/':
                self.op_lst.append(('Math.divide', 2))
            self.tknz.advance()
            if self.tknz.curr_token != '(':
                self.cmp_term()
            else:  # curr token is "("
                self.tknz.advance()
                self.cmp_expression()
                if self.tknz.curr_token == ")" or not self.op_lst:
                    break
            while self.op_lst:
                command = self.op_lst.pop()
                if type(command) == tuple:
                    self.VMW.writeCall(command[0], command[1])
                else:
                    self.VMW.writeArithmetic(command)
                nextT = self.peek()
                if nextT != ";" and nextT == ")":  # deals with recursive cases
                    self.tknz.advance()

    def cmp_term(self):
        """
        breaks each expression down into term and compiles them accordingly.
        """
        tType = self.tknz.token_type()
        nextT = self.peek()
        if tType == "integerConstant":
            self.VMW.writePush("constant", self.tknz.curr_token)
            self.tknz.advance()  # advances to ')'
        elif tType == "stringConstant":
            if not self.tknz.curr_token.endswith("\""):  # checks for str const
                temp = self.__get_whole_str(self.tknz.curr_token)
                self.tknz.curr_token = temp  # whole string const with spaces
            self.tknz.advance()
        elif tType == "IDENTIFIER":
            if nextT == "[":
                self.tknz.advance()
                self.term_helper(self.cmp_expression)
            segment = self.symbol.kindOf(self.tknz.curr_token)
            index = self.symbol.indexOf(self.tknz.curr_token)
            if self.tknz.curr_token in self.symbol.class_level:
                if segment == "field":
                    self.VMW.writePush("this", index)
                else:  # static
                    self.VMW.writePush(segment, index)
            elif self.tknz.curr_token in self.symbol.subroutine_level:
                self.VMW.writePush(segment, index)  # local or arg
            elif nextT in ["(", "."]:
                self.subRoutineCall(nextT)
            self.tknz.advance()
        elif tType == "SYMBOL":
            self.term_helper(self.cmp_expression)
            if self.tknz.curr_token in ["-", "~"]:  # unary op ahead
                remember = self.tknz.curr_token
                if self.peek() == "(":
                    self.tknz.advance()
                self.tknz.advance()
                self.cmp_expression()
                if remember == '-':
                    self.VMW.writeArithmetic('neg')
                else:  # ~
                    self.VMW.writeArithmetic('not')
            else:
                self.tknz.advance()
        elif tType == "KEYWORD":
            if self.tknz.curr_token in self.tknz.key_const:
                if self.tknz.curr_token == 'this':
                    self.VMW.writePush('pointer', 0)
                elif self.tknz.curr_token == 'true':
                    self.VMW.writePush('constant', 1)
                    self.VMW.writeArithmetic('neg')
                else:  # false or null
                    self.VMW.writePush('constant', 0)
            self.tknz.advance()

    def subRoutineCall(self, nextT):
        """
        compiles a subroutine call
        :param nextT: the next token, helps determine which case were in.
        """
        prefix = self.tknz.curr_token  # class/method names
        if nextT == "(":
            self.tknz.advance()
            self.VMW.writePush("pointer", 0)
            self.VMW.writePop("arg", 0)  # first arg of method is "self"
            self.symbol.arg_counter += 1
            self.term_helper(self.cmp_expression_lst)
            nArgs = self.symbol.varCount("arg")
            self.VMW.writeCall(self.className + "." + prefix, nArgs)

        elif nextT == ".":
            self.tknz.advance()  # .
            self.tknz.advance()  # method name
            suffix = self.tknz.curr_token  # saves subroutine name
            fullName = prefix + "." + suffix
            self.tknz.advance()  # (
            self.tknz.advance()  # into expression
            self.cmp_expression_lst()  # returns when curr = ")"
            #self.tknz.advance()  # ";"
            self.VMW.writeCall(fullName, self.expression_count)

    def term_helper(self, func):
        """
        a helper method for term compiling
        :param func: a function which writes a specific part of code
        """
        if self.tknz.curr_token not in ["-", "~"]:  # unary op ahead
            self.tknz.advance()
            func()

    def cmp_expression_lst(self):
        """
        compiles a list of expressions, separated by commas.
        :return: amount of variables the function takes.
        """
        self.expression_count = 0
        if self.tknz.curr_token != ")":
            while True:
                self.cmp_expression()  # compiles expression
                self.expression_count += 1
                if self.tknz.curr_token == ")":  # done with exp list
                    break
                self.tknz.advance()

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


class JackCompiler:
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
    JA = JackCompiler(file_or_path)
    JA.main()
