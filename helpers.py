class Helpers:

    def aplana(self, miLista):
        if miLista == []:
            return miLista
        if isinstance(miLista[0], list):
            return self.aplana(miLista[0]) + self.aplana(miLista[1:])
        return miLista[:1] + self.aplana(miLista[1:])
    
    def operator_operation(self, currTok):
        token_Types = {
            1 : ["ADD", "SUBSTR", "MULT", "DIVIS", "EQUAL", "MORE_THAN", "LESS_THAN", "IS_EQUAL", "NOT_EQUAL"],
            2 : ["INT", "CTE_INT", "FLOAT", "CTE_FLOAT"],
            3 : ["ID"],
            4 : ["EQUAL"]
        }
        for key in token_Types:
            if currTok in token_Types[key]:
                return key
        return -1
    
    def getOperationType(self, currTok):
        listaTipos = {
            1 : ["ADD", "SUBSTR"],
            2 : ["MULT", "DIVIS"],
            3 : ["EQUAL"],
            4 : ["MORE_THAN", "LESS_THAN", "IS_EQUAL", "NOT_EQUAL"],
            5 : ["PRINT"],
            6 : ["AND", "OR"]
        }
        for key in listaTipos:
            if currTok in listaTipos[key]:
                return key
        return -1
    
    def getOperatorType(self, currTok):
        listaTipos = {
            "INT" : ["INT", "CTE_INT"],
            "FLOAT" : ["FLOAT", "CTE_FLOAT"],
            "STRING" : ["STRING", "CTE_STRING"],
            "BOOL" : ["BOOL"]
        }

        for key in listaTipos:
            if currTok in listaTipos[key]:
                return key
        return -1
    
    def getVarFunction(self, myFunctions, myVar, currFunc, globalFunc):
        if myVar in myFunctions[currFunc]["vars"]:
            return currFunc
        elif myVar in myFunctions[globalFunc]["vars"]:
            return globalFunc
        return -1
    
    def getTypeDir(self, currDir):
        if currDir < 2000:
            return self.getOffset(currDir - 1000)
        elif currDir < 3000:
            return self.getOffset(currDir - 2000)
        elif currDir < 4000:
            return self.getOffset(currDir - 3000)
        elif currDir < 5000:
            return self.getOffset(currDir - 4000)
    
    def getOffset(self, off):
        if off < 250:
            return "INT"
        elif off < 500:
            return "FLOAT"
    
    def getOperationNumber(self, quads):
        for row in quads:
            op = row[0]
            if op == "ADD":
                row[0] = 1
            elif op == "SUBSTR":
                row[0] = 2
            elif op == "MULT":
                row[0] = 3
            elif op == "DIVIS":
                row[0] = 4
            elif op == "EQUAL":
                row[0] = 5
            elif op == "MORE_THAN":
                row[0] = 6
            elif op == "LESS_THAN":
                row[0] = 7
            elif op == "IS_EQUAL":
                row[0] = 8
            elif op == "NOT_EQUAL":
                row[0] = 9
            elif op == "PRINT":
                row[0] = 10
            elif op == "INPUT":
                row[0] = 11
            elif op == "GOTO":
                row[0] = 12
            elif op == "GOTOF":
                row[0] = 13
            elif op == "GOSUB":
                row[0] = 14
            elif op == "ERA":
                row[0] = 15
            elif op == "PARAM":
                row[0] = 16
            elif op == "END":
                row[0] = 17
            elif op == "ENDFUNC":
                row[0] = 18
            elif op == "RETURN":
                row[0] = 19
            elif op == "LINEUP":
                row[0] = 20
            elif op == "LINEDOWN":
                row[0] = 21
            elif op == "RIGHT":
                row[0] = 22
            elif op == "LEFT":
                row[0] = 23
            elif op == "CLEAR":
                row[0] = 24
            elif op == "PINTAR":
                row[0] = 25
            elif op == "NOPINTAR":
                row[0] = 26
            elif op == "SIZE":
                row[0] = 27
            elif op == "CIRCLE":
                row[0] = 28
            elif op == "ARCO":
                row[0] = 29
            elif op == "POINT":
                row[0] = 30
            elif op == "COLOR":
                row[0] = 31