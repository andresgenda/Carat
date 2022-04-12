from rply import ParserGenerator
from ast import Success

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['PROGRAM', 'PRINT', 'COMMA', 'COLON', 'SEMI_COLON', 'OPEN_PARENTH', 'CLOSE_PARENTH',
            'OPEN_BRACK', 'CLOSE_BRACK', 'EQUAL', 'IF', 'MORE_THAN', 'LESS_THAN', 'NOT_EQUAL', 
            'ELSE', 'ADD', 'SUBSTR', 'MULT', 'DIVIS', 'VAR','CTE_STRING', 'ID', 'INT', 'FLOAT', 
            'CTE_INT', 'CTE_FLOAT'],

            precedence=[
                ('left', ['ADD', 'SUBSTR']),
                ('left', ['MULT', 'DIVIS'])
            ]
        )

    def parse(self):
        @self.pg.production('programa : PROGRAM ID SEMI_COLON programa2')
        def programa(p):
            return Success()

        @self.pg.production('programa2 : vars bloque')
        @self.pg.production('programa2 : bloque')
        def programa2(p):
            return Success()
        
        @self.pg.production('vars : VAR vars2')
        def vars(p):
            return Success()
        
        @self.pg.production('vars2 : ID COMMA vars2')
        @self.pg.production('vars2 : ID COLON tipo SEMI_COLON')
        def vars2(p):
            return Success()

        @self.pg.production('tipo : INT')
        @self.pg.production('tipo : FLOAT')
        def tipo(p):
            return Success()
        
        @self.pg.production('bloque : OPEN_BRACK bloque2')
        def bloque(p):
            return Success()
        
        @self.pg.production('bloque2 : estatuto bloque2')
        @self.pg.production('bloque2 : estatuto CLOSE_BRACK')
        def bloque2(p):
            return Success()
        
        @self.pg.production('estatuto : asignacion')
        @self.pg.production('estatuto : condicion')
        @self.pg.production('estatuto : escritura')
        def estatuto(p):
            return Success()
        
        @self.pg.production('asignacion : ID EQUAL expresion SEMI_COLON')
        def asignacion(p):
            return Success()
        
        @self.pg.production('condicion : IF OPEN_PARENTH expresion CLOSE_PARENTH bloque condicion2')
        def condicion(p):
            return Success()

        @self.pg.production('condicion2 : ELSE bloque condicion3')
        @self.pg.production('condicion2 : condicion3')
        def condicion2(p):
            return Success()
        
        @self.pg.production('condicion3 : SEMI_COLON')
        def condicion3(p):
            return Success()
        
        @self.pg.production('escritura : PRINT OPEN_PARENTH escritura2')
        def escritura(p):
            return Success()
        
        @self.pg.production('escritura2 : expresion escritura3')
        @self.pg.production('escritura2 : CTE_STRING escritura3')
        def escritura2(p):
            return Success()
        
        @self.pg.production('escritura3 : COMMA escritura2')
        @self.pg.production('escritura3 : CLOSE_PARENTH SEMI_COLON')
        def escritura3(p):
            return Success()
        
        @self.pg.production('expresion : exp expresion2')
        @self.pg.production('expresion : expresion3')
        def expresion(p):
            return Success()
        
        @self.pg.production('expresion2 : MORE_THAN expresion3')
        @self.pg.production('expresion2 : LESS_THAN expresion3')
        @self.pg.production('expresion2 : NOT_EQUAL expresion3')
        def expresion2(p):
            return Success()
        
        @self.pg.production('expresion3 : exp')
        def expresion3(p):
            return Success()
        
        @self.pg.production('exp : termino ADD exp')
        @self.pg.production('exp : termino SUBSTR exp')
        @self.pg.production('exp : termino')
        def exp(p):
            return Success()
        
        @self.pg.production('termino : factor MULT termino')
        @self.pg.production('termino : factor DIVIS termino')
        @self.pg.production('termino : factor')
        def termino(p):
            return Success()
        
        @self.pg.production('factor : OPEN_PARENTH expresion CLOSE_PARENTH')
        @self.pg.production('factor : factor2')
        @self.pg.production('factor : factor3')
        def factor(p):
            return Success()
        
        @self.pg.production('factor2 : ADD factor3')
        @self.pg.production('factor2 : SUBSTR factor3')
        def factor2(p):
            return Success()
        
        @self.pg.production('factor3 : varcte')
        def factor3(p):
            return Success()
        
        @self.pg.production('varcte : ID')
        @self.pg.production('varcte : CTE_INT')
        @self.pg.production('varcte : CTE_FLOAT')
        def varcte(p):
            return Success()
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()