from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('PROGRAM', r'program')
        self.lexer.add('PRINT', r'print')
        self.lexer.add('INT', r'int')
        self.lexer.add('FLOAT', r'float')
        self.lexer.add('IF', r'if')
        self.lexer.add('ELSE', r'else')
        self.lexer.add('CTE_STRING', r"\"([^\"\\]|\\.)*\"")
        self.lexer.add('VAR', r'var')
        self.lexer.add('COMMA', r'\,')
        self.lexer.add('COLON', r'\:')
        self.lexer.add('SEMI_COLON', r'\;')
        self.lexer.add('OPEN_PARENTH', r'\(')
        self.lexer.add('CLOSE_PARENTH', r'\)')
        self.lexer.add('OPEN_BRACK', r'\{')
        self.lexer.add('CLOSE_BRACK', r'\}')
        self.lexer.add('EQUAL', r'\=')
        self.lexer.add('NOT_EQUAL', r'\<>')
        self.lexer.add('MORE_THAN', r'\>')
        self.lexer.add('LESS_THAN', r'\<')
        self.lexer.add('ADD', r'\+')
        self.lexer.add('SUBSTR', r'\-')
        self.lexer.add('MULT', r'\*')
        self.lexer.add('DIVIS', r'\/')
        self.lexer.add('CTE_INT', r'\d+')
        self.lexer.add('ID', r'[a-zA-Z_$][a-zA-Z_0-9]*')
        self.lexer.add('CTE_FLOAT', r'(((0|[1-9][0-9]*)(\.[0-9]*)+)|(\.[0-9]+))([eE][\+\-]?[0-9]*)?')
        self.lexer.ignore('\s+')


    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()