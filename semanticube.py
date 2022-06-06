# ------------- Clase SemanticCube -------------
# Clase encargada de regresar la consideración semántica en cuanto a combinación de tipos

from helpers import Helpers

class SemanticCube:

    #Diccionario de aritméticas -.- +, -, *, /
    diccArit = {
        "INT" : {
            "INT" : "INT",
            "FLOAT" : "FLOAT",
            "BOOL" : "ERROR"
        },
        "FLOAT" : {
            "INT" : "FLOAT",
            "FLOAT" : "FLOAT",
            "BOOL" : "ERROR"
        },
        "BOOL" : {
            "INT" : "ERROR",
            "FLOAT" : "ERROR",
            "BOOL" : "ERROR"
        }
    }
    
    #Diccionario de asignación -.- =
    diccAsig = {
        "INT" : {
            "INT" : "INT",
            "FLOAT" : "FLOAT",
            "BOOL" : "ERROR"
        },
        "FLOAT" : {
            "INT" : "ERROR",
            "FLOAT" : "FLOAT",
            "BOOL" : "ERROR"
        },
        "BOOL" : {
            "INT" : "ERROR",
            "FLOAT" : "ERROR",
            "BOOL" : "ERROR"
        }
    }

    #Diccionario de comparaciones -.- <, >, !=, ==
    diccComp = {
        "INT" : {
            "INT" : "BOOL",
            "FLOAT" : "BOOL",
            "BOOL" : "ERROR"
        },
        "FLOAT" : {
            "INT" : "BOOL",
            "FLOAT" : "BOOL",
            "BOOL" : "ERROR"
        },
        "BOOL" : {
            "INT" : "ERROR",
            "FLOAT" : "ERROR",
            "BOOL" : "ERROR"
        }
    }

    #Diccionario de condicionales -.- &, |
    diccCond = {
        "INT" : {
            "INT" : "ERROR",
            "FLOAT" : "ERROR",
            "BOOL" : "ERROR"
        },
        "FLOAT" : {
            "INT" : "ERROR",
            "FLOAT" : "ERROR",
            "BOOL" : "ERROR"
        },
        "BOOL" : {
            "INT" : "ERROR",
            "FLOAT" : "ERROR",
            "BOOL" : "BOOL"
        }
    }


    def __init__(self):
        self.help = Helpers()

    #Regresa el tipo segun el tipo del primer y segundo operando
    def assignType(self, op1, op2, oprt_type):
        #Checa si la operación es arimética
        if(oprt_type == 1 or oprt_type == 2):
            return self.diccArit[op1][op2]
        #Checa si la operación es de asignación
        elif(oprt_type == 3):
            return self.diccAsig[op1][op2]
        #Checa si la operación es de comparación
        elif(oprt_type == 4):
            return self.diccComp[op1][op2]
        #Checa si la operación es condicional
        elif(oprt_type == 6):
            return self.diccCond[op1][op2]

    #Valida que la operación sea válida, y busca los tipos de cada operando
    def matchTypes(self, op1_type, op2_type, operation):
        oprType = self.help.getOperationType(operation)
        
        if(oprType == -1):
            print("ERROR: Operacion no valida")
            return "ERROR"
        
        op1_type = self.help.getOperatorType(op1_type)
        op2_type = self.help.getOperatorType(op2_type)
        return_type = self.assignType(op1_type, op2_type, oprType)
        
        return return_type