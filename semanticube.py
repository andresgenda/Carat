from helpers import Helpers

class SemanticCube:

    diccArit = {
        "INT" : {
            "INT" : "INT",
            "FLOAT" : "FLOAT"
        },
        "FLOAT" : {
            "INT" : "FLOAT",
            "FLOAT" : "FLOAT"
        }
    }
    
    diccAsig = {
        "INT" : {
            "INT" : "INT",
            "FLOAT" : "FLOAT"
        },
        "FLOAT" : {
            "INT" : "error",
            "FLOAT" : "FLOAT"
        }
    }

    diccComp = {
        "INT" : {
            "INT" : "BOOL",
            "FLOAT" : "BOOL"
        },
        "FLOAT" : {
            "INT" : "BOOL",
            "FLOAT" : "BOOL"
        }
    }

    def __init__(self):
        self.help = Helpers()

    def assignType(self, op1, op2, oprt_type):
        if(oprt_type == 1 or oprt_type == 2):
            return self.diccArit[op1][op2]
        elif(oprt_type == 3):
            return self.diccAsig[op1][op2]
        elif(oprt_type == 4):
            return self.diccComp[op1][op2]

    def matchTypes(self, op1_type, op2_type, operation):

        oprType = self.help.getOperationType(operation)
        
        if(oprType == -1):
            print("ERROR: Operacion no valida")
            return "ERROR"
        
        op1_type = self.help.getOperatorType(op1_type)
        op2_type = self.help.getOperatorType(op2_type)
        return_type = self.assignType(op1_type, op2_type, oprType)
        
        return return_type


#INT with INT combination
            #---ARITMETICOS---
            # + -> INT
            # - -> INT
            # * -> INT
            # / -> INT
            #---ASIGNACION---
            # = -> INT
            #---COMPARACION---
            # > -> BOOL
            # < -> BOOL
            # == -> BOOL
            # != -> BOOL
        

        #Si me llega INT, FLOAT:
        #---ARITMETICOS---
        # + -> FLOAT
        # - -> FLOAT
        # * -> FLOAT
        # / -> FLOAT
        #---ASIGNACION---
        # = -> FLOAT
        #---COMPARACION---
        # > -> BOOL
        # < -> BOOL
        # == -> BOOL
        # != -> BOOL
        

        #Si me llega FLOAT, INT:
        #---ARITMETICOS---
        # + -> FLOAT
        # - -> FLOAT
        # * -> FLOAT
        # / -> FLOAT
        #---ASIGNACION---
        # = -> ERROR
        #---COMPARACION---
        # > -> BOOL
        # < -> BOOL
        # == -> BOOL
        # != -> BOOL

        #Si me llega FLOAT, FLOAT:
        #---ARITMETICOS---
        # + -> FLOAT
        # - -> FLOAT
        # * -> FLOAT
        # / -> FLOAT
        #---ASIGNACION---
        # = -> FLOAT
        #---COMPARACION---
        # > -> BOOL
        # < -> BOOL
        # == -> BOOL
        # != -> BOOL