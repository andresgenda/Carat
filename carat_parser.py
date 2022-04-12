from rply import ParserGenerator
from ast import Success

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['PROGRAM', 'PRINT', 'COMMA', 'SEMI_COLON', 'OPEN_PARENTH', 'CLOSE_PARENTH',
            'OPEN_BRACK', 'CLOSE_BRACK', 'EQUAL', 'IF', 'MORE_THAN', 'LESS_THAN', 'NOT_EQUAL', 
            'ELSE', 'ADD', 'SUBSTR', 'MULT', 'DIVIS', 'VAR','CTE_STRING', 'ID', 'INT', 'FLOAT', 
            'CTE_INT', 'CTE_FLOAT', 'CHAR', 'VOID', 'RETURN', 'INPUT', 'FUNC', 'WHILE', 'DO', 'FOR',
            'TO', 'IS_EQUAL', 'AND', 'OR', 'OPEN_CURLY', 'CLOSE_CURLY', 'MAIN'],

            precedence=[
                ('left', ['ADD', 'SUBSTR']),
                ('left', ['MULT', 'DIVIS'])
            ]
        )

    def parse(self):
        @self.pg.production('programa : PROGRAM ID SEMI_COLON programa2')
        @self.pg.production('programa : PROGRAM ID SEMI_COLON programa4')
        def programa(p):
            return Success()

        @self.pg.production('programa2 : vars programa3')
        @self.pg.production('programa2 : programa3')
        def programa2(p):
            return Success()
        
        @self.pg.production('programa3 : funcion programa3')
        @self.pg.production('programa3 : programa4')
        def programa3(p):
            return Success()
        
        @self.pg.production('programa4 : MAIN OPEN_PARENTH CLOSE_PARENTH OPEN_CURLY bloque CLOSE_CURLY')
        def programa4(p):
            return Success()
        
        @self.pg.production('vars : VAR tipo vars2')
        def vars(p):
            return Success()
        
        @self.pg.production('vars2 : ID arreglo vars3')
        @self.pg.production('vars2 : ID vars3')
        def vars2(p):
            return Success()
        
        @self.pg.production('vars3 : COMMA vars2')
        @self.pg.production('vars3 : SEMI_COLON vars')
        @self.pg.production('vars3 : SEMI_COLON')

        @self.pg.production('tipo : INT')
        @self.pg.production('tipo : FLOAT')
        @self.pg.production('tipo : CHAR')
        def tipo(p):
            return Success()
        
        @self.pg.production('arreglo : def_arr')
        @self.pg.production('arreglo : def_arr def_arr')
        def arreglo(p):
            return Success()
        
        @self.pg.production('def_arr : OPEN_BRACK def_arr2')
        def def_arr(p):
            return Success()
        
        @self.pg.production('def_arr2 : CTE_INT CLOSE_BRACK')
        @self.pg.production('def_arr2 : ID CLOSE_BRACK')
        def def_arr2(p):
            return Success()
        
        @self.pg.production('funcion : f_void')
        @self.pg.production('funcion : f_ret')
        def funcion(p):
            return Success()
        
        @self.pg.production('f_void : VOID init OPEN_CURLY f_void2')
        def f_void(p):
            return Success()

        @self.pg.production('f_void2 : vars f_void3')
        @self.pg.production('f_void2 : f_void3')
        def f_void2(p):
            return Success()
        
        @self.pg.production('f_void3 : bloque CLOSE_CURLY')
        def f_void3(p):
            return Success()
        
        @self.pg.production('f_ret : tipo init OPEN_CURLY f_ret2')
        def f_ret(p):
            return Success()
        
        @self.pg.production('f_ret2 : vars f_ret3')
        @self.pg.production('f_ret2 : f_ret3')
        def f_ret2(p):
            return Success()
        
        @self.pg.production('f_ret3 : bloque RETURN OPEN_PARENTH exp CLOSE_PARENTH SEMI_COLON CLOSE_CURLY')
        def f_ret3(p):
            return Success()
        
        @self.pg.production('init : FUNC ID OPEN_PARENTH init2')
        @self.pg.production('init : FUNC ID OPEN_PARENTH init3')
        def init(p):
            return Success()
        
        @self.pg.production('init2 : tipo ID COMMA init2')
        @self.pg.production('init2 : tipo ID init3')
        def init2(p):
            return Success()
        
        @self.pg.production('init3 : CLOSE_PARENTH')
        def init3(p):
            return Success()
        
        @self.pg.production('bloque : estatuto')
        @self.pg.production('bloque : estatuto bloque')
        def bloque(p):
            return Success()
        
        @self.pg.production('estatuto : asignacion')
        @self.pg.production('estatuto : decision')
        @self.pg.production('estatuto : lectura')
        @self.pg.production('estatuto : escritura')
        @self.pg.production('estatuto : ciclo_cc')
        @self.pg.production('estatuto : ciclo_sc')
        @self.pg.production('estatuto : llam_func')
        def estatuto(p):
            return Success()
        
        @self.pg.production('asignacion : ID EQUAL asignacion2')
        def asignacion(p):
            return Success()
        
        @self.pg.production('asignacion2 : asig_arr SEMI_COLON')
        @self.pg.production('asignacion2 : expresion SEMI_COLON')
        @self.pg.production('asignacion2 : llam_func')
        def asignacion2(p):
            return Success()
        
        @self.pg.production('asig_arr : elems')
        @self.pg.production('asig_arr : OPEN_CURLY elems asig_arr2')
        def asig_arr(p):
            return Success()
        
        @self.pg.production('asig_arr2 : COMMA elems asig_arr2')
        @self.pg.production('asig_arr2 : CLOSE_CURLY')
        def asig_arr2(p):
            return Success()
        
        @self.pg.production('elems : OPEN_CURLY var_cte elems2')
        def elems(p):
            return Success()
        
        @self.pg.production('elems2 : COMMA var_cte elems2')
        @self.pg.production('elems2 : CLOSE_CURLY')
        def elems2(p):
            return Success()
        
        @self.pg.production('var_cte : ID')
        @self.pg.production('var_cte : CTE_INT')
        @self.pg.production('var_cte : CTE_FLOAT')
        def var_cte(p):
            return Success()
        
        @self.pg.production('expresion : exp expresion2')
        @self.pg.production('expresion : expresion3')
        def expresion(p):
            return Success()
        
        @self.pg.production('expresion2 : MORE_THAN expresion3')
        @self.pg.production('expresion2 : LESS_THAN expresion3')
        @self.pg.production('expresion2 : IS_EQUAL expresion3')
        @self.pg.production('expresion2 : NOT_EQUAL expresion3')
        @self.pg.production('expresion2 : AND expresion3')
        @self.pg.production('expresion2 : OR expresion3')
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
        
        @self.pg.production('factor3 : var_cte')
        @self.pg.production('factor3 : llam_func')
        def factor3(p):
            return Success()
        
        @self.pg.production('decision : IF OPEN_PARENTH expresion CLOSE_PARENTH OPEN_CURLY bloque CLOSE_CURLY')
        @self.pg.production('decision : IF OPEN_PARENTH expresion CLOSE_PARENTH OPEN_CURLY bloque CLOSE_CURLY decision2')
        def decision(p):
            return Success()

        @self.pg.production('decision2 : ELSE OPEN_CURLY bloque CLOSE_CURLY')
        def decision2(p):
            return Success()
        
        @self.pg.production('lectura : INPUT OPEN_PARENTH ID lectura2')
        def lectura(p):
            return Success()
        
        @self.pg.production('lectura2 : COMMA ID lectura2')
        @self.pg.production('lectura2 : CLOSE_PARENTH SEMI_COLON')
        def lectura2(p):
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
        
        @self.pg.production('ciclo_cc : WHILE OPEN_PARENTH expresion CLOSE_PARENTH DO OPEN_CURLY bloque CLOSE_CURLY')
        def ciclo_cc(p):
            return Success()
        
        @self.pg.production('ciclo_sc : FOR ID EQUAL exp TO exp DO OPEN_CURLY bloque CLOSE_CURLY')
        def ciclo_sc(p):
            return Success()
        
        @self.pg.production('llam_func : ID OPEN_PARENTH llam_func2')
        def llam_func(p):
            return Success()
        
        @self.pg.production('llam_func2 : exp llam_func3')
        @self.pg.production('llam_func2 : CLOSE_PARENTH SEMI_COLON')
        def llam_func2(p):
            return Success()
        
        @self.pg.production('llam_func3 : COMMA exp llam_func3')
        @self.pg.production('llam_func3 : CLOSE_PARENTH SEMI_COLON')
        def llam_func3(p):
            return Success()
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()