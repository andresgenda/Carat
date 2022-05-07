from helpers import Helpers

class SemanticCube:

    diccArit = {
        "int" : {
            "int" : "int",
            "float" : "float"
        },
        "float" : {
            "int" : "float",
            "float" : "float"
        }
    }
    
    diccAsig = {
        "int" : {
            "int" : "int",
            "float" : "float"
        },
        "float" : {
            "int" : "error",
            "float" : "float"
        }
    }

    diccComp = {
        "int" : {
            "int" : "bool",
            "float" : "bool"
        },
        "float" : {
            "int" : "bool",
            "float" : "bool"
        }
    }

    def __init__(self):
        self.help = Helpers()

    def assignType(self, op1, op2, oprt_type):
        if(oprt_type == 1 or oprt_type == 2):
            print(self.diccArit[op1][op2])
        elif(oprt_type == 3):
            print(self.diccAsig[op1][op2])
        elif(oprt_type == 4):
            print(self.diccComp[op1][op2])

    def matchTypes(self, op1_type, op2_type, operation):

        oprType = self.help.getOperationType(operation)
        
        if(oprType == -1):
            print("ERROR: Operacion no valida")
        else:
            op1_type = self.help.getOperatorType(op1_type)
            op2_type = self.help.getOperatorType(op2_type)
            self.assignType(op1_type, op2_type, oprType)


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