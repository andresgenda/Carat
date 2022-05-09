import rply
from rply import ParserGenerator
from helpers import Helpers
from quadruples import Quadruples
from stack import Stack

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['PROGRAM', 'PRINT', 'COMMA', 'SEMI_COLON', 'OPEN_PARENTH', 'CLOSE_PARENTH',
            'OPEN_BRACK', 'CLOSE_BRACK', 'EQUAL', 'IF', 'MORE_THAN', 'LESS_THAN', 'NOT_EQUAL', 
            'ELSE', 'ADD', 'SUBSTR', 'MULT', 'DIVIS', 'VAR','CTE_STRING', 'ID', 'INT', 'FLOAT', 
            'CTE_INT', 'CTE_FLOAT', 'CHAR', 'VOID', 'RETURN', 'INPUT', 'FUNC', 'WHILE', 'DO', 'FOR',
            'TO', 'IS_EQUAL', 'AND', 'OR', 'OPEN_CURLY', 'CLOSE_CURLY', 'MAIN', 'LINEUP', 'LINEDOWN',
            'LINERT', 'LINELF', 'POINT', 'CIRCLE', 'ARC', 'PENUP', 'PENDOWN', 'PENCOLOR', 'PENSIZE',
            'CLEAR'],

            precedence=[
                ('left', ['ADD', 'SUBSTR']),
                ('left', ['MULT', 'DIVIS'])
            ]
        )

        self.help = Helpers()
        self.tabFunc = {}
        self.globalFunc = ""
        self.currVarT = {}
        self.currFunc = ""
        self.currType = ""
        self.quads = Quadruples()
        self.stackOperandos = Stack()
        self.stackTipos = Stack()
        self.stackOperaciones = Stack()
        self.misQuads = []

    def parse(self):
        @self.pg.production('programa : PROGRAM createDF SEMI_COLON programa2')
        @self.pg.production('programa : PROGRAM createDF SEMI_COLON programa4')
        def programa(p):
            return p

        @self.pg.production('programa2 : vars programa3')
        @self.pg.production('programa2 : programa3')
        def programa2(p):
            return p
        
        @self.pg.production('programa3 : funcion programa3')
        @self.pg.production('programa3 : programa4')
        def programa3(p):
            return p
        
        @self.pg.production('programa4 : varglobales MAIN OPEN_PARENTH CLOSE_PARENTH OPEN_CURLY bloque CLOSE_CURLY')
        def programa4(p):
            return p
        
        @self.pg.production('varglobales : ')
        def varglobales(p):
            self.tabFunc[self.currFunc].append(self.currVarT)
            self.currFunc = self.globalFunc
            print(self.tabFunc)
            return p

        @self.pg.production('createDF : ID')
        def createDF(p):
            self.currFunc = p[0].value
            self.globalFunc = self.currFunc
            self.tabFunc[self.currFunc] = ["void"]
            return p
        
        @self.pg.production('vars : VAR tipo vars2')
        def vars(p):
            return p
        
        @self.pg.production('vars2 : idAux arreglo vars3')
        @self.pg.production('vars2 : idAux vars3')
        def vars2(p):
            return p
        
        @self.pg.production('idAux : ID')
        def idAux(p):
            if p[0].value in self.currVarT:
                raise ValueError("Declaracion multiple de variables")
            self.currVarT[p[0].value] = self.currType
            return p
        
        @self.pg.production('vars3 : COMMA vars2')
        @self.pg.production('vars3 : SEMI_COLON vars')
        @self.pg.production('vars3 : SEMI_COLON')
        def vars3(p):
            return p

        @self.pg.production('tipo : INT')
        @self.pg.production('tipo : FLOAT')
        @self.pg.production('tipo : CHAR')
        def tipo(p):
            self.currType = p[0].gettokentype()
            return p
        
        @self.pg.production('arreglo : def_arr')
        @self.pg.production('arreglo : def_arr def_arr')
        def arreglo(p):
            return p
        
        @self.pg.production('def_arr : OPEN_BRACK def_arr2')
        def def_arr(p):
            return p
        
        @self.pg.production('def_arr2 : CTE_INT CLOSE_BRACK')
        @self.pg.production('def_arr2 : ID CLOSE_BRACK')
        def def_arr2(p):
            return p
        
        @self.pg.production('funcion : f_void')
        @self.pg.production('funcion : f_ret')
        def funcion(p):
            return p
        
        @self.pg.production('f_void : bpVoid init OPEN_CURLY f_void2')
        def f_void(p):
            return p
        
        @self.pg.production('bpVoid : VOID')
        def bpVoid(p):
            self.currType = p[0].gettokentype
            return p


        @self.pg.production('f_void2 : vars f_void3')
        @self.pg.production('f_void2 : f_void3')
        def f_void2(p):
            return p
        
        @self.pg.production('f_void3 : bloque CLOSE_CURLY')
        def f_void3(p):
            return p
        
        @self.pg.production('f_ret : tipo init OPEN_CURLY f_ret2')
        def f_ret(p):
            return p
        
        @self.pg.production('f_ret2 : vars f_ret3')
        @self.pg.production('f_ret2 : f_ret3')
        def f_ret2(p):
            return p
        
        @self.pg.production('f_ret3 : bloque RETURN OPEN_PARENTH exp CLOSE_PARENTH SEMI_COLON CLOSE_CURLY')
        def f_ret3(p):
            return p
        
        @self.pg.production('init : FUNC bpCurrFunc OPEN_PARENTH init2')
        @self.pg.production('init : FUNC bpCurrFunc OPEN_PARENTH init3')
        def init(p):
            return p
        
        #Funcion que recibe el nombre de una funcion
        # - Funcion agrega las variables a la funcion actual y cambia la
        #   funcion actual por la nueva funcion, vacia el arreglo de variables y
        #   le asigna el tipo actual a la funcion
        @self.pg.production('bpCurrFunc : ID')
        def bpCurrFunc(p):
            if p[0].value in self.tabFunc:
                raise ValueError("Nombre de funcion ya existe")
            self.tabFunc[self.currFunc].append(self.currVarT)
            self.currVarT = {}
            self.currFunc = p[0].value
            self.tabFunc[self.currFunc] = [self.currType]
            return p
        
        @self.pg.production('init2 : tipo ID COMMA init2')
        @self.pg.production('init2 : tipo ID init3')
        def init2(p):
            return p
        
        @self.pg.production('init3 : CLOSE_PARENTH')
        def init3(p):
            return p
        
        @self.pg.production('bloque : estatuto')
        @self.pg.production('bloque : estatuto bloque')
        def bloque(p):
            return p
        
        @self.pg.production('estatuto : asignacion')
        @self.pg.production('estatuto : decision')
        @self.pg.production('estatuto : lectura')
        @self.pg.production('estatuto : escritura')
        @self.pg.production('estatuto : ciclo_cc')
        @self.pg.production('estatuto : ciclo_sc')
        @self.pg.production('estatuto : llam_func')
        @self.pg.production('estatuto : llam_esp')
        def estatuto(p):
            return p
        
        @self.pg.production('asignacion : asigHelp asignacion2')
        def asignacion(p):
            #listaPlana = self.help.aplana(p)
            #varsAct = self.tabFunc[self.currFunc][1]
            #self.quads.assignQuad(self.stackOperandos, self.stackTipos, self.misQuads)
            self.quads.assignQuadCopy(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads)
            print(self.misQuads)
            #self.quads.createQuads(listaPlana, varsAct)
            return p
        
        @self.pg.production('asigHelp : ID EQUAL')
        def asigHelp(p):
            self.stackOperandos.push(p[0].value)
            idType = self.tabFunc[self.currFunc][1][p[0].value]
            self.stackTipos.push(idType)
            self.stackOperaciones.push(p[1].gettokentype())
            return p
        
        @self.pg.production('asignacion2 : asig_arr SEMI_COLON')
        @self.pg.production('asignacion2 : expresion SEMI_COLON')
        @self.pg.production('asignacion2 : llam_func')
        def asignacion2(p):
            return p
        
        @self.pg.production('asig_arr : elems')
        @self.pg.production('asig_arr : OPEN_CURLY elems asig_arr2')
        def asig_arr(p):
            return p
        
        @self.pg.production('asig_arr2 : COMMA elems asig_arr2')
        @self.pg.production('asig_arr2 : CLOSE_CURLY')
        def asig_arr2(p):
            return p
        
        @self.pg.production('elems : OPEN_CURLY var_cte elems2')
        def elems(p):
            return p
        
        @self.pg.production('elems2 : COMMA var_cte elems2')
        @self.pg.production('elems2 : CLOSE_CURLY')
        def elems2(p):
            return p
        
        @self.pg.production('var_cte : ID')
        @self.pg.production('var_cte : CTE_INT')
        @self.pg.production('var_cte : CTE_FLOAT')
        def var_cte(p):
            #listaPlana = self.help.aplana(p)
            self.stackOperandos.push(p[0].value)
            curr_type = self.help.getOperatorType(p[0].gettokentype())
            self.stackTipos.push(curr_type)
            return p
        
        @self.pg.production('expresion : exp expresion2')
        @self.pg.production('expresion : expresion3')
        def expresion(p):
            return p
        
        @self.pg.production('expresion2 : MORE_THAN expresion3')
        @self.pg.production('expresion2 : LESS_THAN expresion3')
        @self.pg.production('expresion2 : IS_EQUAL expresion3')
        @self.pg.production('expresion2 : NOT_EQUAL expresion3')
        @self.pg.production('expresion2 : AND expresion3')
        @self.pg.production('expresion2 : OR expresion3')
        def expresion2(p):
            return p
        
        @self.pg.production('expresion3 : exp')
        def expresion3(p):
            #self.quads.createQuads(listaPlana, varsAct)
            return p
        
        @self.pg.production('exp : termino expSumSub exp')
        @self.pg.production('exp : termino')
        def exp(p):
            return p
        
        @self.pg.production('expSumSub : ADD')
        @self.pg.production('expSumSub : SUBSTR')
        def expSumSub(p):
            listaPlana = self.help.aplana(p)
            currTok = listaPlana[0].gettokentype()
            listaPlana = self.help.aplana(p)
            currTok = listaPlana[0].gettokentype()
            checkOp = self.stackOperaciones.top()
            tipoCheck = self.help.getOperationType(checkOp)
            while(tipoCheck == 1 or tipoCheck == 2):
                if self.stackOperaciones.top() == "ADD" or self.stackOperaciones.top() == "SUBSTR":
                    currOp = self.stackOperaciones.pop()
                    self.quads.executeQuadGenCopy(currOp, self.stackOperandos, self.stackTipos, self.misQuads)
                elif self.stackOperaciones.top() == "MULT" or self.stackOperaciones.top() == "DIVIS":
                    currOp = self.stackOperaciones.pop()
                    self.quads.executeQuadGenCopy(currOp, self.stackOperandos, self.stackTipos, self.misQuads)
                checkOp = self.stackOperaciones.top()
                tipoCheck = self.help.getOperationType(checkOp)
            self.stackOperaciones.push(currTok)
            return p
        
        @self.pg.production('termino : factor factorMultDiv termino')
        @self.pg.production('termino : factor')
        def termino(p):
            return p
        
        @self.pg.production('factorMultDiv : MULT')
        @self.pg.production('factorMultDiv : DIVIS')
        def factorMultDiv(p):
            listaPlana = self.help.aplana(p)
            currTok = listaPlana[0].gettokentype()
            if self.stackOperaciones.top() == "ADD" or self.stackOperaciones.top() == "SUBSTR":
                self.stackOperaciones.push(currTok)
            elif self.stackOperaciones.top() == "MULT" or self.stackOperaciones.top() == "DIVIS":
                currOp = self.stackOperaciones.pop()
                self.stackOperaciones.push(currTok)
                self.quads.executeQuadGenCopy(currOp, self.stackOperandos, self.stackTipos, self.misQuads)
            else:
                self.stackOperaciones.push(currTok)
            return p
        
        @self.pg.production('factor : OPEN_PARENTH expresion CLOSE_PARENTH')
        @self.pg.production('factor : factor2')
        @self.pg.production('factor : factor3')
        def factor(p):
            return p
        
        @self.pg.production('factor2 : ADD factor3')
        @self.pg.production('factor2 : SUBSTR factor3')
        def factor2(p):
            return p
        
        @self.pg.production('factor3 : var_cte')
        @self.pg.production('factor3 : llam_func')
        def factor3(p):
            return p
        
        @self.pg.production('decision : IF OPEN_PARENTH expresion CLOSE_PARENTH OPEN_CURLY bloque CLOSE_CURLY')
        @self.pg.production('decision : IF OPEN_PARENTH expresion CLOSE_PARENTH OPEN_CURLY bloque CLOSE_CURLY decision2')
        def decision(p):
            return p

        @self.pg.production('decision2 : ELSE OPEN_CURLY bloque CLOSE_CURLY')
        def decision2(p):
            return p
        
        @self.pg.production('lectura : INPUT OPEN_PARENTH ID lectura2')
        def lectura(p):
            return p
        
        @self.pg.production('lectura2 : COMMA ID lectura2')
        @self.pg.production('lectura2 : CLOSE_PARENTH SEMI_COLON')
        def lectura2(p):
            return p
        
        @self.pg.production('escritura : PRINT OPEN_PARENTH escritura2')
        def escritura(p):
            return p
        
        @self.pg.production('escritura2 : expresion escritura3')
        @self.pg.production('escritura2 : CTE_STRING escritura3')
        def escritura2(p):
            return p
        
        @self.pg.production('escritura3 : COMMA escritura2')
        @self.pg.production('escritura3 : CLOSE_PARENTH SEMI_COLON')
        def escritura3(p):
            return p
        
        @self.pg.production('ciclo_cc : WHILE OPEN_PARENTH expresion CLOSE_PARENTH DO OPEN_CURLY bloque CLOSE_CURLY')
        def ciclo_cc(p):
            return p
        
        @self.pg.production('ciclo_sc : FOR ID EQUAL exp TO exp DO OPEN_CURLY bloque CLOSE_CURLY')
        def ciclo_sc(p):
            return p
        
        @self.pg.production('llam_func : ID OPEN_PARENTH llam_func2')
        def llam_func(p):
            return p
        
        @self.pg.production('llam_func2 : exp llam_func3')
        @self.pg.production('llam_func2 : CLOSE_PARENTH SEMI_COLON')
        def llam_func2(p):
            return p
        
        @self.pg.production('llam_func3 : COMMA exp llam_func3')
        @self.pg.production('llam_func3 : CLOSE_PARENTH SEMI_COLON')
        def llam_func3(p):
            return p
        
        @self.pg.production('llam_esp : linea')
        @self.pg.production('llam_esp : punto')
        @self.pg.production('llam_esp : circulo')
        @self.pg.production('llam_esp : arco')
        @self.pg.production('llam_esp : pintar')
        @self.pg.production('llam_esp : no_pintar')
        @self.pg.production('llam_esp : col')
        @self.pg.production('llam_esp : tam')
        @self.pg.production('llam_esp : borrar')
        def llam_esp(p):
            return p
        
        @self.pg.production('linea : arriba')
        @self.pg.production('linea : abajo')
        @self.pg.production('linea : derecha')
        @self.pg.production('linea : izq')
        def linea(p):
            return p
        
        @self.pg.production('arriba : LINEUP OPEN_PARENTH exp CLOSE_PARENTH SEMI_COLON')
        def arriba(p):
            return p
        
        @self.pg.production('abajo : LINEDOWN OPEN_PARENTH exp CLOSE_PARENTH SEMI_COLON')
        def abajo(p):
            return p
        
        @self.pg.production('derecha : LINERT OPEN_PARENTH exp CLOSE_PARENTH SEMI_COLON')
        def derecha(p):
            return p
        
        @self.pg.production('izq : LINELF OPEN_PARENTH exp CLOSE_PARENTH SEMI_COLON')
        def izq(p):
            return p
        
        @self.pg.production('punto : POINT OPEN_PARENTH exp COMMA exp CLOSE_PARENTH SEMI_COLON')
        def punto(p):
            return p
        
        @self.pg.production('circulo : CIRCLE OPEN_PARENTH exp CLOSE_PARENTH SEMI_COLON')
        def circulo(p):
            return p
        
        @self.pg.production('arco : ARC OPEN_PARENTH exp COMMA exp CLOSE_PARENTH SEMI_COLON')
        def arco(p):
            return p
        
        @self.pg.production('pintar : PENDOWN OPEN_PARENTH CLOSE_PARENTH SEMI_COLON')
        def pintar(p):
            return p
        
        @self.pg.production('no_pintar : PENUP OPEN_PARENTH CLOSE_PARENTH SEMI_COLON')
        def no_pintar(p):
            return p
        
        @self.pg.production('col : PENCOLOR OPEN_PARENTH exp COMMA exp COMMA exp CLOSE_PARENTH SEMI_COLON')
        def col(p):
            return p
        
        @self.pg.production('tam : PENSIZE OPEN_PARENTH exp CLOSE_PARENTH SEMI_COLON')
        def tam(p):
            return p
        
        @self.pg.production('borrar : CLEAR OPEN_PARENTH CLOSE_PARENTH SEMI_COLON')
        def borrar(p):
            return p
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()