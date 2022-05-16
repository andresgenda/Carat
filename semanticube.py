from helpers import Helpers

class SemanticCube:

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

    def assignType(self, op1, op2, oprt_type):
        if(oprt_type == 1 or oprt_type == 2):
            return self.diccArit[op1][op2]
        elif(oprt_type == 3):
            return self.diccAsig[op1][op2]
        elif(oprt_type == 4):
            return self.diccComp[op1][op2]
        elif(oprt_type == 6):
            return self.diccCond[op1][op2]

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