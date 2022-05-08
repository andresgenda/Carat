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
            4 : ["MORE_THAN", "LESS_THAN", "IS_EQUAL", "NOT_EQUAL"]
        }
        for key in listaTipos:
            if currTok in listaTipos[key]:
                return key
        return -1
    
    def getOperatorType(self, currTok):
        listaTipos = {
            "INT" : ["INT", "CTE_INT"],
            "FLOAT" : ["FLOAT", "CTE_FLOAT"]
        }

        for key in listaTipos:
            if currTok in listaTipos[key]:
                return key
            return -1
