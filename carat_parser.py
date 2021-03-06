# ------------- Clase Parser -------------
# Clase encargada de implementar la gramática del lenguaje de programación
# En este módulo se genera el código intermedio

import rply
import numpy as np
from rply import ParserGenerator
from helpers import Helpers
from quadruples import Quadruples
from stack import Stack
from dirFunc import DirFunc
from semanticube import SemanticCube
from MemVirtual import MemVirtual

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
        self.newDirFunc = DirFunc()
        self.globalFunc = ""
        self.currVarT = {}
        self.currFunc = ""
        self.currType = ""
        self.quads = Quadruples()
        self.stackOperandos = Stack()
        self.stackTipos = Stack()
        self.stackOperaciones = Stack()
        self.misQuads = []
        self.stackJumps = Stack()
        self.counter = 0
        self.sc = SemanticCube()
        self.memVirt = MemVirtual()
        self.paramTable = []
        self.paramCounter = 0
        self.accessFunc = ""
        self.isReturning = False
        self.isVoid = False

    def parse(self):

        #Se exportan las constantes, las funciones y los cuádruplos
        #Se agrega el cuádruplo de fin de programa
        @self.pg.production('programa : PROGRAM mainStart createDF SEMI_COLON programa2')
        @self.pg.production('programa : PROGRAM mainStart createDF SEMI_COLON programa4')
        def programa(p):
            self.newDirFunc.deleteKey(self.currFunc, "vars")
            newQuad = ["END", "", "", ""]
            self.misQuads.append(newQuad)
            self.help.getOperationNumber(self.misQuads)
            quadsExport = np.array(self.misQuads)
            np.savetxt('ExportedFiles/exportedQuads.csv', quadsExport, delimiter=',', fmt="%s")
            self.memVirt.exportCtes()
            self.newDirFunc.exportFuncs()
            return p

        @self.pg.production('programa2 : vars addVars programa3')
        @self.pg.production('programa2 : programa3')
        def programa2(p):
            return p
        
        @self.pg.production('programa3 : funcion programa3')
        @self.pg.production('programa3 : programa4')
        def programa3(p):
            return p
        
        @self.pg.production('programa4 : MAIN fillMain OPEN_PARENTH CLOSE_PARENTH OPEN_CURLY bloque CLOSE_CURLY')
        def programa4(p):
            return p
        
        #Punto neurálgico para iniciar el arreglo de cuádruplos con el GOTO al MAIN
        @self.pg.production('mainStart : ')
        def mainStart(p):
            self.stackJumps.push(0)
            newQuad = ["GOTO", "", "", ""]
            self.misQuads.append(newQuad)
            return p
        
        #Rellena el cuádruplo de GOTO al MAIN
        @self.pg.production('fillMain : ')
        def fillMain(p):
            self.newDirFunc.setNumVars(self.currFunc)
            currJump = len(self.misQuads)+1
            self.newDirFunc.setVarsTotal(self.currFunc)
            self.newDirFunc.setStart(self.globalFunc, currJump)
            self.stackJumps.push(currJump)
            self.quads.fillGoto(self.stackJumps, self.misQuads)
            return p

        #Crea el directorio de funciones con la función global
        @self.pg.production('createDF : ID')
        def createDF(p):
            self.currFunc = p[0].value
            self.globalFunc = self.currFunc
            self.newDirFunc.addFunc(self.currFunc, "VOID")
            return p
        
        @self.pg.production('vars : VAR tipo vars2')
        def vars(p):
            return p
        
        @self.pg.production('vars2 : idAux arreglo vars3')
        @self.pg.production('vars2 : idAux vars3')
        def vars2(p):
            return p
        
        #Verifica que la variable no haya sido declarada
        #Agrega una nueva variable a la tabla de variables
        @self.pg.production('idAux : ID')
        def idAux(p):
            if p[0].value in self.currVarT:
                raise ValueError("Declaracion multiple de variables")
            if self.currFunc == self.globalFunc:
                currDir = self.memVirt.getNextDir(self.currType, 0)
            else:
                currDir = self.memVirt.getNextDir(self.currType, 1)
            self.currVarT[p[0].value] = [self.currType, currDir]
            return p
        
        @self.pg.production('vars3 : COMMA vars2')
        @self.pg.production('vars3 : SEMI_COLON vars')
        @self.pg.production('vars3 : SEMI_COLON')
        def vars3(p):
            return p

        #Se agrega la tabla de variables al directorio de funciones
        #Se reinicia la tabla de varibales y la tabla de parámetros
        @self.pg.production('addVars : ')
        def addVars(p):
            self.newDirFunc.addVar(self.currFunc, self.currVarT)
            self.currVarT = {}
            self.paramTable = []
            return p

        #Se actualiza el tipo actual al tipo que viene llegando
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
        
        @self.pg.production('def_arr : OPEN_BRACK CTE_INT CLOSE_BRACK')
        def def_arr(p):
            return p
        
        #Se determina el número de variables utilizadas y se reinician las direcciones
        @self.pg.production('funcion : f_void')
        @self.pg.production('funcion : f_ret')
        def funcion(p):
            self.newDirFunc.setNumVars(self.currFunc)
            self.newDirFunc.setVarsTotal(self.currFunc)
            self.newDirFunc.deleteKey(self.currFunc, "vars")
            self.memVirt.resetVars()
            newQuad = ["ENDFUNC", "", "", ""]
            self.misQuads.append(newQuad)
            #Al terminar la funcion actual, la funcion actual vuelve a ser la global
            self.currFunc = self.globalFunc
            return p

        @self.pg.production('f_void : bpVoid init OPEN_CURLY f_void2')
        def f_void(p):
            return p
        
        #Se valida que el tipo de la función es VOID
        @self.pg.production('bpVoid : VOID')
        def bpVoid(p):
            self.currType = p[0].gettokentype()
            self.isVoid = True
            return p

        #Se indica que el tipo de la función NO es VOID
        @self.pg.production('isVoid : ')
        def isVoid(p):
            self.isVoid = False
            return p

        @self.pg.production('f_void2 : vars addVars f_void3')
        @self.pg.production('f_void2 : addVars f_void3')
        def f_void2(p):
            return p
        
        @self.pg.production('f_void3 : bloque CLOSE_CURLY')
        def f_void3(p):
            return p
        
        #Se valida que la función regrese algo
        @self.pg.production('f_ret : tipo isVoid init OPEN_CURLY f_ret2')
        def f_ret(p):
            if self.isReturning == False:
                raise ValueError("La funcion tiene que tener un retorno")
            self.isReturning = False
            return p
        
        @self.pg.production('f_ret2 : vars addVars f_ret3')
        @self.pg.production('f_ret2 : addVars f_ret3')
        def f_ret2(p):
            return p
        
        @self.pg.production('f_ret3 : bloque CLOSE_CURLY')
        @self.pg.production('f_ret3 : CLOSE_CURLY')
        def f_ret3(p):
            return p
        
        #Se válida que la función sea del tipo adecuado
        @self.pg.production('doReturn : ')
        def doReturn(p):
            self.quads.assignQuadCopy(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            retOp = self.stackOperandos.top()
            tipoActual = self.stackTipos.top()
            if self.isVoid == True:
                raise ValueError("Funcion de tipo VOID no puede tener retorno")
            funcType = self.newDirFunc.misFunciones[self.currFunc]["tipo"]
            if tipoActual != funcType:
                raise ValueError("Return - Function Type-mismatch")
            dirFunc = self.newDirFunc.getVarMem(self.globalFunc, self.currFunc)
            newQuad = ["RETURN", dirFunc, "", retOp]
            self.misQuads.append(newQuad)
            self.isReturning = True
            return p
        
        #Se coloca el número de cuádruplo en donde inicia la función
        @self.pg.production('init : FUNC bpCurrFunc OPEN_PARENTH init2')
        @self.pg.production('init : FUNC bpCurrFunc OPEN_PARENTH init3')
        def init(p):
            star_dir = len(self.misQuads)+1
            self.newDirFunc.addParams(self.currFunc, self.paramTable)
            self.newDirFunc.setStart(self.currFunc, star_dir)
            self.newDirFunc.setNumParams(self.currFunc)
            return p
        
        #Se cambia la funcion actual por la que viene llegando, y se agrega al directorio junto con su tipo
        @self.pg.production('bpCurrFunc : ID')
        def bpCurrFunc(p):
            if p[0].value in self.newDirFunc.misFunciones:
                raise ValueError("Nombre de funcion ya existe")
            self.currFunc = p[0].value
            self.newDirFunc.addFunc(self.currFunc, self.currType)
            if self.currType != "VOID":
                currDir = self.memVirt.getNextDir(self.currType, 0)
                infoToAdd = [self.currType, currDir]
                self.newDirFunc.misFunciones[self.globalFunc]["vars"][self.currFunc] = infoToAdd
            return p
        
        @self.pg.production('init2 : addParam COMMA init2')
        @self.pg.production('init2 : addParam init3')
        def init2(p):
            return p
        
        @self.pg.production('init3 : CLOSE_PARENTH')
        def init3(p):
            return p
        
        #Se agrega un parámetro a la lista de variables y tabla de parámetros
        @self.pg.production('addParam : tipo ID')
        def addParam(p):
            listaPlana = self.help.aplana(p)
            self.currType = listaPlana[0].gettokentype()
            if listaPlana[1].value in self.currVarT:
                raise ValueError("Declaracion multiple de variables")
            if self.currFunc == self.globalFunc:
                currDir = self.memVirt.getNextDir(self.currType, 0)
            else:
                currDir = self.memVirt.getNextDir(self.currType, 1)
            self.paramTable.append(self.currType)
            self.currVarT[listaPlana[1].value] = [self.currType, currDir]
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
        @self.pg.production('estatuto : ret')
        def estatuto(p):
            return p
        
        @self.pg.production('ret : RETURN OPEN_PARENTH expresion CLOSE_PARENTH doReturn SEMI_COLON')
        @self.pg.production('ret : RETURN OPEN_PARENTH llam_func CLOSE_PARENTH doReturn SEMI_COLON')
        def ret(p):
            return p
        
        #Se realiza la asignación
        @self.pg.production('asignacion : asigHelp asignacion2')
        def asignacion(p):
            self.quads.assignQuadCopy(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            return p
        
        #Se válida que la variable que se quiere asignar exista y se guarda su dirección en la pila de operandos
        @self.pg.production('asigHelp : ID EQUAL')
        def asigHelp(p):
            curr_id = p[0].value
            misFuncs = self.newDirFunc.misFunciones
            varFunction = self.help.getVarFunction(misFuncs, curr_id, self.currFunc, self.globalFunc)
            if varFunction == -1:
                raise ValueError("Variable no declarada")
            curr_idmem = self.newDirFunc.getVarMem(varFunction, curr_id)
            self.stackOperandos.push(curr_idmem)
            idType = self.newDirFunc.getIDType(varFunction, curr_id)
            self.stackTipos.push(idType)
            self.stackOperaciones.push(p[1].gettokentype())
            return p
        
        @self.pg.production('asignacion2 : llam_func')
        @self.pg.production('asignacion2 : asig_arr SEMI_COLON')
        @self.pg.production('asignacion2 : expresion SEMI_COLON')
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
        
        #Se busca la variable en caso de que sea ID, o bien se asigna dirección de constante
        @self.pg.production('var_cte : ID')
        @self.pg.production('var_cte : CTE_INT')
        @self.pg.production('var_cte : CTE_FLOAT')
        def var_cte(p):
            myToken = p[0].gettokentype()
            if myToken == 'CTE_INT' or myToken == 'CTE_FLOAT':
                self.memVirt.assignCte(myToken, p[0].value)
                dirCte = self.memVirt.getCteDir(p[0].value, myToken)
                curr_type = self.help.getOperatorType(p[0].gettokentype())
            else:
                curr_id = p[0].value
                misFuncs = self.newDirFunc.misFunciones
                varFunction = self.help.getVarFunction(misFuncs, curr_id, self.currFunc, self.globalFunc)
                if varFunction == -1:
                    raise ValueError("Variable no declarada")
                dirCte = self.newDirFunc.getVarMem(varFunction, curr_id)
                curr_type = self.newDirFunc.getIDType(varFunction, curr_id)
            self.stackOperandos.push(dirCte)
            self.stackTipos.push(curr_type)
            return p
        
        @self.pg.production('expresion : exp expresionComp expresion3')
        @self.pg.production('expresion : exp expresionCond expresion3')
        @self.pg.production('expresion : expresion3')
        def expresion(p):
            return p
        
        #Se guarda el tipo de operación
        @self.pg.production('expresionComp : MORE_THAN')
        @self.pg.production('expresionComp : LESS_THAN')
        @self.pg.production('expresionComp : IS_EQUAL')
        @self.pg.production('expresionComp : NOT_EQUAL')
        def expresionComp(p):
            self.quads.assignQuadCopy(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            currOp = p[0].gettokentype()
            self.stackOperaciones.push(currOp)
            return p

        #Se guarda el tipo de operación
        @self.pg.production('expresionCond : AND expresion')
        @self.pg.production('expresionCond : OR expresion')
        def expresionCond(p):
            self.quads.assignQuadCopy(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            currOp = p[0].gettokentype()
            self.stackOperaciones.push(currOp)
            return p
        
        @self.pg.production('expresion3 : exp')
        def expresion3(p):
            return p
        
        @self.pg.production('exp : termino expSumSub exp')
        @self.pg.production('exp : termino')
        def exp(p):
            return p
        
        #Checa que no haya otra operación aritmética antes que la nueva que llega
        #Genera el cuádruplo correspondiente
        #Si hay otra operación, genera su cuádruplo antes de empujar la nueva operación
        @self.pg.production('expSumSub : ADD')
        @self.pg.production('expSumSub : SUBSTR')
        def expSumSub(p):
            listaPlana = self.help.aplana(p)
            currTok = listaPlana[0].gettokentype()
            checkOp = self.stackOperaciones.top()
            tipoCheck = self.help.getOperationType(checkOp)
            while(tipoCheck == 1 or tipoCheck == 2):
                if self.stackOperaciones.top() == "ADD" or self.stackOperaciones.top() == "SUBSTR":
                    currOp = self.stackOperaciones.pop()
                    self.quads.executeQuadGenCopy(currOp, self.stackOperandos, self.stackTipos, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
                elif self.stackOperaciones.top() == "MULT" or self.stackOperaciones.top() == "DIVIS":
                    currOp = self.stackOperaciones.pop()
                    self.quads.executeQuadGenCopy(currOp, self.stackOperandos, self.stackTipos, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
                checkOp = self.stackOperaciones.top()
                tipoCheck = self.help.getOperationType(checkOp)
            self.stackOperaciones.push(currTok)
            return p
        
        @self.pg.production('termino : factor factorMultDiv termino')
        @self.pg.production('termino : factor')
        def termino(p):
            return p
        
        #Checa que no haya otra operación de la misma prioridad
        #Si es de menor prioridad, mete la operación actual a la pila
        #Si es de igual prioridad, realiza la operación anterior, y luego se mete a la pila
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
                self.quads.executeQuadGenCopy(currOp, self.stackOperandos, self.stackTipos, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            else:
                self.stackOperaciones.push(currTok)
            return p
        
        @self.pg.production('factor : op_parenth expresion cl_parenth')
        @self.pg.production('factor : factor3')
        def factor(p):
            return p
        
        #Empuja el paréntesis en las operaciones
        @self.pg.production('op_parenth : OPEN_PARENTH')
        def op_parenth(p):
            self.stackOperaciones.push(p[0].gettokentype())
            return p
        
        #Realiza todas las operaciones hasta llegar al paréntesis
        @self.pg.production('cl_parenth : CLOSE_PARENTH')
        def cl_parenth(p):
            self.quads.emptyParenth(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            return p
        
        @self.pg.production('factor3 : llam_func')
        @self.pg.production('factor3 : var_cte')
        def factor3(p):
            return p
        
        @self.pg.production('decision : decisionWOElse')
        @self.pg.production('decision : decisionWElse')
        def decision(p):
            return p
        
        #Llena el GOTO en caso de que la condición sea falsa
        @self.pg.production('decisionWOElse : IF OPEN_PARENTH expresion CLOSE_PARENTH if_bkpt OPEN_CURLY bloque CLOSE_CURLY')
        def decisionWOElse(p):
            currJump = len(self.misQuads) + 1
            self.stackJumps.push(currJump)
            self.quads.fillGoto(self.stackJumps, self.misQuads)
            return p
        
        #Llena el GOTO para que se brinque el else
        @self.pg.production('decisionWElse : IF OPEN_PARENTH expresion CLOSE_PARENTH if_bkpt OPEN_CURLY bloque CLOSE_CURLY decision2')
        def decisionWElse(p):
            currJump = len(self.misQuads) + 1
            self.stackJumps.push(currJump)
            self.quads.fillGoto(self.stackJumps, self.misQuads)
            return p
        
        #Crea el cuádruplo de GOTOF
        #Checa que el tipo sea BOOL
        @self.pg.production('if_bkpt : ')
        def if_bkpt(p):
            self.quads.assignQuadCopy(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            opEval = self.stackOperandos.pop()
            op_type = self.stackTipos.pop()
            if op_type != "BOOL":
                raise ValueError("Type Mismatch")
            else:
                newQuad = ["GOTOF", opEval, "", ""]
                currJump = len(self.misQuads)
                self.stackJumps.push(currJump)
                self.misQuads.append(newQuad)
            return p

        @self.pg.production('decision2 : ELSE else_chckpoint OPEN_CURLY bloque CLOSE_CURLY')
        def decision2(p):
            return p
        
        #Genera el GOTO que se brinca al else
        #Llena el GOTOF que se creó 
        @self.pg.production('else_chckpoint : ')
        def else_chckpoint(p):
            newQuad = ["GOTO", "", "", ""]
            self.misQuads.append(newQuad)
            cuadElse = len(self.misQuads) - 1
            currJump = len(self.misQuads) + 1
            self.stackJumps.push(currJump)
            self.quads.fillGoto(self.stackJumps, self.misQuads)
            self.stackJumps.push(cuadElse)
            return p
        
        @self.pg.production('lectura : INPUT OPEN_PARENTH lecturaAux lectura2')
        def lectura(p):
            return p
        
        @self.pg.production('lectura2 : COMMA lecturaAux lectura2')
        @self.pg.production('lectura2 : CLOSE_PARENTH SEMI_COLON')
        def lectura2(p):
            return p
        
        #Checa que la variable haya sido declarada
        @self.pg.production('lecturaAux : ID')
        def lecturaAux(p):
            curr_var = p[0].value
            if curr_var in self.newDirFunc.getVars(self.currFunc):
                curr_add = self.newDirFunc.getVarMem(self.currFunc, curr_var)
                self.quads.read_writeQuad("INPUT", curr_add, self.misQuads)
            else:
                raise ValueError("Variable no declarada")
            return p
        
        @self.pg.production('escritura : PRINT OPEN_PARENTH escritura2')
        def escritura(p):
            return p
        
        @self.pg.production('escritura2 : escritura_expAux escritura_exp escritura3')
        @self.pg.production('escritura2 : escritura_str escritura3')
        def escritura2(p):
            return p
        
        #Empuja la operación print
        @self.pg.production('escritura_expAux : ')
        def escritura_expAux(p):
            self.stackOperaciones.push("PRINT")
            return p
        
        #Realiza la exp hasta que ya no hayan operaciones restantes
        @self.pg.production('escritura_exp : exp')
        def escritura_exp(p):
            self.quads.assignQuadCopy(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            return p
        
        #Genera el cuádruplo del PRINT, y asigna una dirección constante al string
        @self.pg.production('escritura_str : CTE_STRING')
        def escritura_str(p):
            curr_val = p[0].value
            myToken = p[0].gettokentype()
            self.memVirt.assignCte(myToken, curr_val)
            dirCte = self.memVirt.getCteDir(curr_val, myToken)
            self.quads.read_writeQuad("PRINT", dirCte, self.misQuads)
            return p

        @self.pg.production('escritura3 : COMMA escritura2')
        @self.pg.production('escritura3 : CLOSE_PARENTH SEMI_COLON')
        def escritura3(p):
            return p
        
        #Crea el cuádruplo para regresar a donde comienza el while
        #Llena el cuádruplo de GOTOF
        @self.pg.production('ciclo_cc : WHILE while_bkpt OPEN_PARENTH expresion CLOSE_PARENTH DO while_cond OPEN_CURLY bloque CLOSE_CURLY')
        def ciclo_cc(p):
            newQuad = ["GOTO", "", "", ""]
            self.misQuads.append(newQuad)
            returnWhile = len(self.misQuads) - 1
            currJump = len(self.misQuads) + 1
            self.stackJumps.push(currJump)
            self.quads.fillGoto(self.stackJumps, self.misQuads)
            self.stackJumps.push(returnWhile)
            self.quads.fillGotoWhile(self.stackJumps, self.misQuads)
            return p
        
        #Agrega el número del cuádruplo donde empieza el while a la pila de saltos
        @self.pg.production('while_bkpt : ')
        def while_bkpt(p):
            currJump = len(self.misQuads) + 1
            self.stackJumps.push(currJump)
            return p
        
        #Genera el cuádruplo GOTOF
        @self.pg.production('while_cond : ')
        def while_cond(p):
            self.quads.assignQuadCopy(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            opEval = self.stackOperandos.pop()
            op_type = self.stackTipos.pop()
            if op_type != "BOOL":
                raise ValueError("Type Mismatch")
            else:
                newQuad = ["GOTOF", opEval, "", ""]
                currJump = len(self.misQuads)
                self.stackJumps.push(currJump)
                self.misQuads.append(newQuad)
            return p
        
        #Realiza la suma de 1 al vector del control
        #Genera el GOTO para regresar a la comparación
        #Llena el GOTOF en caso de ser falsa
        @self.pg.production('ciclo_sc : FOR for_idbkpt EQUAL expFor exp for_expbkptone TO expFor exp for_expbkpttwo DO OPEN_CURLY bloque CLOSE_CURLY')
        def ciclo_sc(p):
            vcontrol = self.stackOperandos.pop()
            self.stackTipos.pop()
            result = self.memVirt.getNextDir("INT", 2)
            self.newDirFunc.setNumTemps(self.currFunc, "INT")
            self.memVirt.assignCte("INT", '1')
            addOne = self.memVirt.getCteDir('1', "INT")
            newQuad = ["ADD", vcontrol, addOne, result]
            self.misQuads.append(newQuad)
            newQuad = ["EQUAL", result, "", vcontrol]
            self.misQuads.append(newQuad)
            newQuad = ["GOTO", "", "", ""]
            self.misQuads.append(newQuad)
            jumpToPush = len(self.misQuads) + 1
            self.stackJumps.push(jumpToPush)
            self.quads.fillGoto(self.stackJumps, self.misQuads)
            returnWhile = len(self.misQuads) - 1
            self.stackJumps.push(returnWhile)
            self.quads.fillGotoWhile(self.stackJumps, self.misQuads)
            return p
        
        #Crea un fondo falso
        @self.pg.production('expFor : ')
        def expFor(p):
            self.stackOperaciones.push('OPEN_PARENTH')
            return p
        
        #Checa que exista la variable
        @self.pg.production('for_idbkpt : ID')
        def for_idbkpt(p):
            curr_id = p[0].value
            #VALIDAR QUE EL ID SI EXISTA Y QUE SEA DE TIPO NUMERICO
            if curr_id in self.newDirFunc.getVars(self.currFunc):
                if self.newDirFunc.getIDType(self.currFunc, curr_id) == "INT":
                    curr_id = p[0].value
                    dirCte = self.newDirFunc.getVarMem(self.currFunc, curr_id)
                    curr_type = self.newDirFunc.getIDType(self.currFunc, curr_id)
                    self.stackOperandos.push(dirCte)
                    self.stackTipos.push(curr_type)
                else:
                    raise ValueError("Type-mismatch")
            else:
                if curr_id in self.newDirFunc.getVars(self.globalFunc):
                    if self.newDirFunc.getIDType(self.globalFunc, curr_id) == "INT":
                        curr_id = p[0].value
                        dirCte = self.newDirFunc.getVarMem(self.globalFunc, curr_id)
                        curr_type = self.newDirFunc.getIDType(self.globalFunc, curr_id)
                        self.stackOperandos.push(dirCte)
                        self.stackTipos.push(curr_type)
                    else:
                        raise ValueError("Type-mismatch")
                else:
                    raise ValueError("Variable de FOR no declarada")
            return p
        
        #Checa el tip de la expresion y se crea el cuádruplo del vector control
        @self.pg.production('for_expbkptone : ')
        def for_expbkptone(p):
            self.quads.emptyParenth(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            exp_type = self.stackTipos.pop()
            if exp_type != "INT":
                raise ValueError("Type-mismatch")
            else:
                curr_exp = self.stackOperandos.pop()
                vcontrol = self.stackOperandos.top()
                control_type = self.stackTipos.top()
                tipo_res = self.sc.matchTypes(control_type, exp_type, "EQUAL")
                if tipo_res == "ERROR":
                    raise ValueError("Type-mismatch")
                else:
                    newQuad = ["EQUAL", curr_exp, "", vcontrol]
                    self.misQuads.append(newQuad)
            return p
        
        #Se gener el cuádruplo de comparación
        @self.pg.production('for_expbkpttwo : ')
        def for_expbkpttwo(p):
            self.quads.emptyParenth(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            exp_type = self.stackTipos.pop()
            if exp_type != "INT":
                raise ValueError("Type-mismatch")
            else:
                curr_exp = self.stackOperandos.pop()
                vfinal = self.stackOperandos.top()
                control_type = self.stackTipos.top()
                tipo_res = self.sc.matchTypes(control_type, exp_type, "LESS_THAN")
                if tipo_res == "ERROR":
                    raise ValueError("Type-mismatch")
                else:
                    result = self.memVirt.getNextDir(tipo_res, 2)
                    self.newDirFunc.setNumTemps(self.currFunc, tipo_res)
                    newQuad = ["LESS_THAN", vfinal, curr_exp, result]
                    self.misQuads.append(newQuad)
                    currJump = len(self.misQuads)
                    self.stackJumps.push(currJump)
                    newQuad = ["GOTOF", result, "", ""]
                    self.misQuads.append(newQuad)
                    currJump = len(self.misQuads) - 1
                    self.stackJumps.push(currJump)
            return p
        
        #Revisa que la cantidad de parámetros sea correcta
        #Genera el cuádruplo GOSUB
        #Si la función no es VOID, genera un cuádruplo para igualar el resultado a una temporal
        @self.pg.production('llam_func : OPEN_PARENTH verifyFuncID OPEN_PARENTH llam_func2')
        def llam_func(p):
            if self.newDirFunc.getParam(self.accessFunc, self.paramCounter) != -1:
                raise ValueError("Faltan variables por declarar")
            startAddress = self.newDirFunc.getStart(self.accessFunc)
            newQuad = ["GOSUB", self.accessFunc, "", startAddress]
            self.misQuads.append(newQuad)
            accessFuncType = self.newDirFunc.getFuncType(self.accessFunc)
            if accessFuncType != "VOID":
                dirFunc = self.newDirFunc.getVarMem(self.globalFunc, self.accessFunc)
                result = self.memVirt.getNextDir(accessFuncType, 2)
                self.newDirFunc.setNumTemps(self.currFunc, accessFuncType)
                newQuad = ["EQUAL", dirFunc, "", result]
                self.misQuads.append(newQuad)
                self.stackOperandos.push(result)
                currType = self.help.getTypeDir(dirFunc)
                self.stackTipos.push(currType)
            self.accessFunc = ""
            return p
        
        #Verifica que la función exista
        #Crea el cuádruplo de ERA
        @self.pg.production('verifyFuncID : ID')
        def verifyFuncID(p):
            curr_id = p[0].value
            if curr_id not in self.newDirFunc.misFunciones:
                raise ValueError("Funcion no declarada")
            self.accessFunc = curr_id
            newQuad = ["ERA", "", "", curr_id]
            self.misQuads.append(newQuad)
            self.paramCounter = 0
            self.stackOperaciones.push('OPEN_PARENTH')
            return p
        
        @self.pg.production('llam_func2 : exp checkParam llam_func3')
        @self.pg.production('llam_func2 : CLOSE_PARENTH SEMI_COLON CLOSE_PARENTH')
        def llam_func2(p):
            return p
        
        @self.pg.production('llam_func3 : COMMA addFkBtm exp checkParam llam_func3')
        @self.pg.production('llam_func3 : CLOSE_PARENTH SEMI_COLON CLOSE_PARENTH')
        def llam_func3(p):
            return p
        
        #Agrega un fondo falso
        @self.pg.production('addFkBtm : ')
        def addFkBtm(p):
            self.stackOperaciones.push('OPEN_PARENTH')
            return p
        
        #Checa que el tipo de parámetro coincida con la tabla de parámetros
        @self.pg.production('checkParam : ')
        def checkParam(p):
            self.quads.emptyParenth(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            arg = self.stackOperandos.pop()
            curr_type = self.stackTipos.pop()
            if curr_type != self.newDirFunc.getParam(self.accessFunc, self.paramCounter):
                raise ValueError("Type-mismatch in function")
            if curr_type == "INT":
                offset = 0
            elif curr_type == "FLOAT":
                offset = 250
            elif curr_type == "STRING":
                offset = 500
            elif curr_type == "BOOL":
                offset = 750
            newQuad = ["PARAM", arg, "", self.paramCounter + offset]
            self.misQuads.append(newQuad)
            self.paramCounter += 1
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
        
        #Genera el cuádruplo que cambia el ángulo de la vuelta a la derecha
        @self.pg.production('commaFkBtmRt : COMMA')
        def commaFkBtmRt(p):
            self.quads.emptyParenth(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            result = self.stackOperandos.pop()
            resultType = self.stackTipos.pop()
            if resultType != "INT" and resultType != "FLOAT":
                raise ValueError("Error de tipo - LINEUP (Solo INT o Float)") 
            newQuad = ["RIGHT", "", "", result]
            self.misQuads.append(newQuad)
            self.stackOperaciones.push('OPEN_PARENTH')
            return p
        
        #Genera el cuádruplo que cambia el ángulo de la vuelta a la izquierda
        @self.pg.production('commaFkBtmLft : COMMA')
        def commaFkBtmLft(p):
            self.quads.emptyParenth(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            result = self.stackOperandos.pop()
            resultType = self.stackTipos.pop()
            if resultType != "INT" and resultType != "FLOAT":
                raise ValueError("Error de tipo - LINEUP (Solo INT o Float)") 
            newQuad = ["LEFT", "", "", result]
            self.misQuads.append(newQuad)
            self.stackOperaciones.push('OPEN_PARENTH')
            return p
        
        @self.pg.production('linea : arriba')
        @self.pg.production('linea : abajo')
        @self.pg.production('linea : derecha')
        @self.pg.production('linea : izq')
        def linea(p):
            return p
        
        #Genera el cuádruplo de pintar hacia arriba
        @self.pg.production('arriba : LINEUP op_parenth exp cl_parenth SEMI_COLON')
        def arriba(p):
            result = self.stackOperandos.pop()
            resultType = self.stackTipos.pop()
            if resultType != "INT" and resultType != "FLOAT":
                raise ValueError("Error de tipo - LINEUP (Solo INT o Float)") 
            newQuad = ["LINEUP", "", "", result]
            self.misQuads.append(newQuad)
            return p
        
        #Genera el cuádruplo de pintar hacia abajo
        @self.pg.production('abajo : LINEDOWN op_parenth exp cl_parenth SEMI_COLON')
        def abajo(p):
            result = self.stackOperandos.pop()
            resultType = self.stackTipos.pop()
            if resultType != "INT" and resultType != "FLOAT":
                raise ValueError("Error de tipo - LINEUP (Solo INT o Float)") 
            newQuad = ["LINEDOWN", "", "", result]
            self.misQuads.append(newQuad)
            return p
        
        #Genera el cuádruplo de pintar hacia arriba, habiendo dado vuelta a la derecha
        @self.pg.production('derecha : LINERT op_parenth exp commaFkBtmRt exp cl_parenth SEMI_COLON')
        def derecha(p):
            result = self.stackOperandos.pop()
            resultType = self.stackTipos.pop()
            if resultType != "INT" and resultType != "FLOAT":
                raise ValueError("Error de tipo - LINEUP (Solo INT o Float)")
            newQuad = ["LINEUP", "", "", result]
            self.misQuads.append(newQuad)
            return p
        
        #Genera el cuádruplo de pintar hacia arriba, habiendo dado vuelta a la izquierda
        @self.pg.production('izq : LINELF op_parenth exp commaFkBtmLft exp cl_parenth SEMI_COLON')
        def izq(p):
            result = self.stackOperandos.pop()
            resultType = self.stackTipos.pop()
            if resultType != "INT" and resultType != "FLOAT":
                raise ValueError("Error de tipo - LINEUP (Solo INT o Float)")
            newQuad = ["LINEUP", "", "", result]
            self.misQuads.append(newQuad)
            return p
        
        #Genera el cuádruplo de moverse a un punto
        @self.pg.production('punto : POINT op_parenth exp commaBkpt exp cl_parenth SEMI_COLON')
        def punto(p):
            coordenadaY = self.stackOperandos.pop()
            YType = self.stackTipos.pop()
            coordenadaX = self.stackOperandos.pop()
            XType = self.stackTipos.pop()
            if XType != "INT" and XType != "FLOAT":
                raise ValueError("Error de tipo - Point X (Solo INT o Float)") 
            if YType != "INT" and YType != "FLOAT":
                raise ValueError("Error de tipo - Point Y (Solo INT o Float)")
            newQuad = ["POINT", coordenadaX, coordenadaY, ""]
            self.misQuads.append(newQuad)
            return p
        
        #Genera el cuádruplo de pintar un circulo
        @self.pg.production('circulo : CIRCLE op_parenth exp cl_parenth SEMI_COLON')
        def circulo(p):
            result = self.stackOperandos.pop()
            resultType = self.stackTipos.pop()
            if resultType != "INT" and resultType != "FLOAT":
                raise ValueError("Error de tipo - LINEUP (Solo INT o Float)") 
            newQuad = ["CIRCLE", "", "", result]
            self.misQuads.append(newQuad)
            return p
        
        #Genera el cuádruplo de pintar un arco
        @self.pg.production('arco : ARC op_parenth exp commaBkpt exp cl_parenth SEMI_COLON')
        def arco(p):
            angulo = self.stackOperandos.pop()
            anguloType = self.stackTipos.pop()
            radio = self.stackOperandos.pop()
            radioType = self.stackTipos.pop()
            if anguloType != "INT" and anguloType != "FLOAT":
                raise ValueError("Error de tipo - ARC Param2 (Solo INT o Float)") 
            if radioType != "INT" and radioType != "FLOAT":
                raise ValueError("Error de tipo - ARC Param1 (Solo INT o Float)")
            newQuad = ["ARCO", angulo, "", radio]
            self.misQuads.append(newQuad)
            return p
        
        #Vacía el fondo falso y agrega un nuevo fondo falso
        @self.pg.production('commaBkpt : COMMA')
        def commaBkpt(p):
            self.quads.emptyParenth(self.stackOperandos, self.stackTipos, self.stackOperaciones, self.misQuads, self.memVirt, self.newDirFunc, self.currFunc)
            self.stackOperaciones.push('OPEN_PARENTH')
            return p
        
        #Genera el cuádruplo de pintar
        @self.pg.production('pintar : PENDOWN OPEN_PARENTH CLOSE_PARENTH SEMI_COLON')
        def pintar(p):
            newQuad = ["PINTAR", "", "", ""]
            self.misQuads.append(newQuad)
            return p
        
        #Genera el cuádruplo de no pintar
        @self.pg.production('no_pintar : PENUP OPEN_PARENTH CLOSE_PARENTH SEMI_COLON')
        def no_pintar(p):
            newQuad = ["NOPINTAR", "", "", ""]
            self.misQuads.append(newQuad)
            return p
        
        #Genera el cuádruplo de cambiar de color de pluma
        @self.pg.production('col : PENCOLOR op_parenth exp commaBkpt exp commaBkpt exp cl_parenth SEMI_COLON')
        def col(p):
            rgbB = self.stackOperandos.pop()
            BType = self.stackTipos.pop()
            rgbG = self.stackOperandos.pop()
            GType = self.stackTipos.pop()
            rgbR = self.stackOperandos.pop()
            RType = self.stackTipos.pop()
            if BType != "INT" and BType != "FLOAT":
                raise ValueError("Error de tipo - ARC Param2 (Solo INT o Float)") 
            if GType != "INT" and GType != "FLOAT":
                raise ValueError("Error de tipo - ARC Param1 (Solo INT o Float)")
            if RType != "INT" and RType != "FLOAT":
                raise ValueError("Error de tipo - ARC Param1 (Solo INT o Float)")
            newQuad = ["COLOR", rgbR, rgbG, rgbB]
            self.misQuads.append(newQuad)
            return p
        
        #Genera el cuádruplo de cambiar de tamaño de pluma
        @self.pg.production('tam : PENSIZE op_parenth exp cl_parenth SEMI_COLON')
        def tam(p):
            result = self.stackOperandos.pop()
            resultType = self.stackTipos.pop()
            if resultType != "INT" and resultType != "FLOAT":
                raise ValueError("Error de tipo - LINEUP (Solo INT o Float)") 
            newQuad = ["SIZE", "", "", result]
            self.misQuads.append(newQuad)
            return p
        
        #Genera el cuádruplo de borrar
        @self.pg.production('borrar : CLEAR OPEN_PARENTH CLOSE_PARENTH SEMI_COLON')
        def borrar(p):
            newQuad = ["CLEAR", "", "", ""]
            self.misQuads.append(newQuad)
            return p
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()