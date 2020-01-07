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
        if kind == 'STATIC':
            self.curr_scope[name] = [type, kind, self.static_counter]
            self.static_counter += 1
        elif kind == 'FIELD':
            self.curr_scope[name] = [type, kind, self.field_counter]
            self.field_counter += 1
        elif kind == 'ARG':
            self.curr_scope[name] = [type, kind, self.arg_counter]
            self.arg_counter += 1
        else:
            self.curr_scope[name] = [type, kind, self.var_counter]
            self.var_counter += 1

    def VarCount(self, kind):
        """
        Returns the number of variables of the given kind already defined in
        the current scope.
        :param kind: kind of the variable
        """
        if kind == 'STATIC':
            return self.static_counter
        elif kind == 'FIELD':
            return self.field_counter
        elif kind == 'ARG':
            return self.arg_counter
        else:
            return self.var_counter

    def KindOf(self, name):
        """
        Returns the kind of the named identifier in the current scope.
        if the identifier is unknown in the current scope, returns NONE
        """
        if name in self.curr_scope:  # checks global or local
            return self.curr_scope[name][1]
        elif name in self.class_level:
            return self.class_level[name][1]
        return None

    def TypeOf(self, name):
        """
        Returns the type of the named identifier in the current scope.
        """
        if name in self.curr_scope:
            return self.curr_scope[name][0]
        elif name in self.class_level:
            return self.class_level[name][0]

    def IndexOf(self, name):
        """
        Returns the index assigned to the named identifier.
        """
        if name in self.curr_scope:
            return self.curr_scope[name][2]
        elif name in self.class_level:
            return self.class_level[name][2]
