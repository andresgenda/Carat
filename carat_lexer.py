# ------------- Clase Lexer -------------
# Clase encargada de agregar y registrar los tokens permitidos por el lenguaje

from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    #Agrega los tokens
    def _add_tokens(self):
        self.lexer.add('PROGRAM', r'program')
        self.lexer.add('LINEUP', r'lineUp')
        self.lexer.add('LINEDOWN', r'lineDown')
        self.lexer.add('LINERT', r'lineRt')
        self.lexer.add('LINELF', r'lineLf')
        self.lexer.add('POINT', r'point')
        self.lexer.add('CIRCLE', r'circle')
        self.lexer.add('ARC', r'arc')
        self.lexer.add('PENUP', r'penUp')
        self.lexer.add('PENDOWN', r'penDown')
        self.lexer.add('PENCOLOR', r'penColor')
        self.lexer.add('PENSIZE', r'penSize')
        self.lexer.add('CLEAR', r'clear')
        self.lexer.add('CTE_STRING', r"\"([^\"\\]|\\.)*\"")
        self.lexer.add('MAIN', r'main')
        self.lexer.add('INPUT', r'input')
        self.lexer.add('PRINT', r'print')
        self.lexer.add('FUNC', r'func')
        self.lexer.add('WHILE', r'while')
        self.lexer.add('DO', r'do')
        self.lexer.add('FOR', r'for')
        self.lexer.add('TO', r'to')
        self.lexer.add('INT', r'int')
        self.lexer.add('FLOAT', r'float')
        self.lexer.add('CHAR', r'char')
        self.lexer.add('VOID', r'void')
        self.lexer.add('RETURN', r'return')
        self.lexer.add('IF', r'if')
        self.lexer.add('ELSE', r'else')
        self.lexer.add('VAR', r'var')
        self.lexer.add('COMMA', r'\,')
        self.lexer.add('SEMI_COLON', r'\;')
        self.lexer.add('OPEN_PARENTH', r'\(')
        self.lexer.add('CLOSE_PARENTH', r'\)')
        self.lexer.add('OPEN_CURLY', r'\{')
        self.lexer.add('CLOSE_CURLY', r'\}')
        self.lexer.add('OPEN_BRACK', r'\[')
        self.lexer.add('CLOSE_BRACK', r'\]')
        self.lexer.add('IS_EQUAL', r'\==')
        self.lexer.add('EQUAL', r'\=')
        self.lexer.add('NOT_EQUAL', r'\!=')
        self.lexer.add('MORE_THAN', r'\>')
        self.lexer.add('LESS_THAN', r'\<')
        self.lexer.add('AND', r'\&')
        self.lexer.add('OR', r'\|')
        self.lexer.add('ADD', r'\+')
        self.lexer.add('SUBSTR', r'\-')
        self.lexer.add('MULT', r'\*')
        self.lexer.add('DIVIS', r'\/')
        self.lexer.add('CTE_FLOAT', r'(((0|[1-9][0-9]*)(\.[0-9]*)+)|(\.[0-9]+))([eE][\+\-]?[0-9]*)?')
        self.lexer.add('CTE_INT', r'\d+')
        self.lexer.add('ID', r'[a-zA-Z_$][a-zA-Z_0-9]*')
        self.lexer.ignore('\s+')


    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()