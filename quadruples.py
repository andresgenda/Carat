from semanticube import SemanticCube
from helpers import Helpers
from stack import Stack

class Quadruples:

    quads = []
    stackOperandos = Stack()
    stackTipos = Stack()
    stackOperaciones = Stack()

    def __init__(self):
        self.scube = SemanticCube()
        self.help = Helpers()
    
    #def assignQuad(self, )
    
    def evalQuad(self, exOp, op1, op2):
        if exOp == "ADD":
            result = int(op1) + int(op2)
            return str(result)
        elif exOp == "SUBSTR":
            result = int(op1) - int(op2)
            return str(result)
        elif exOp == "MULT":
            result = int(op1) * int(op2)
            return str(result)
        elif exOp == "DIVIS":
            result = int(op1) / int(op2)
            return str(result)

    
    def executeQuadGen(self, exOp, currTok):
        currOp = self.stackOperaciones.pop()
        self.stackOperaciones.push(currTok)
        op2 = self.stackOperandos.pop()
        op1 = self.stackOperandos.pop()
        type2 = self.stackTipos.pop()
        type1 = self.stackTipos.pop()
        result_type = self.scube.matchTypes(type1, type2, currOp)
        if result_type != "ERROR":
            result = self.evalQuad(currOp, op1, op2)
            new_quad = [currOp, op1, op2, result]
            self.quads.append(new_quad)
            self.stackOperandos.push(result)
            self.stackTipos.push(result_type)


    def createQuads(self, tokenList, varList):

        for key in tokenList:
            currVal = key.value
            currTok = key.gettokentype()
            #Check if my current token is an operation or an operator
            checkToken = self.help.operator_operation(currTok)
            # 1 ---- OPERATION
            if checkToken == 1:
                checkOp = self.help.getOperationType(currTok)
                if checkOp == 1:
                    if self.stackOperaciones.top() == "MULT" or self.stackOperaciones.top() == "DIVIS":
                        self.executeQuadGen(self.stackOperaciones.top(), currTok)
                    elif self.stackOperaciones.top() == "ADD" or self.stackOperaciones.top() == "SUBSTR":
                        self.executeQuadGen(self.stackOperaciones.top(), currTok)
                    elif self.stackOperaciones.top() == "EQUAL":
                        self.stackOperaciones.push(currTok)
                #AQUI ES POR SI ME LLEGA UNA MULT O DIV
                elif checkOp == 2:
                    if self.stackOperaciones.top() == "MULT" or self.stackOperaciones.top() == "DIVIS":
                        self.executeQuadGen(self.stackOperaciones.top(), currTok)
                    elif self.stackOperaciones.top() == "ADD" or self.stackOperaciones.top() == "SUBSTR":
                        self.stackOperaciones.push(currTok)
                    elif self.stackOperaciones.top() == "EQUAL":
                        self.stackOperaciones.push(currTok)
                elif checkOp == 3:
                    self.stackOperaciones.push(currTok)
            # 2 ---- OPERATOR / CONSTANT
            elif checkToken == 2:
                self.stackOperandos.push(currVal)
                self.stackTipos.push(currTok)
            # 3 ---- OPERATOR / ID
            elif checkToken == 3:
                self.stackOperandos.push(currVal)
                self.stackTipos.push(varList[currVal])
        
        
        while self.stackOperaciones.isEmpty() == False:
            
            checkOp = self.stackOperaciones.pop()
            currOp = checkOp
            checkOp = self.help.getOperationType(checkOp)
            #SUMA O RESTA
            if checkOp == 1:
                op2 = self.stackOperandos.pop()
                op1 = self.stackOperandos.pop()
                type2 = self.stackTipos.pop()
                type1 = self.stackTipos.pop()
                result_type = self.scube.matchTypes(type1, type2, currOp)
                if result_type != "ERROR":
                    result = op1 + op2
                    new_quad = [currOp, op1, op2, result]
                    self.quads.append(new_quad)
                    self.stackOperandos.push(result)
                    self.stackTipos.push(result_type)
            #IGUAL
            if checkOp == 3:
                op1 = self.stackOperandos.pop()
                type1 = self.stackTipos.pop()
                result = self.stackOperandos.pop()
                type_result = self.stackTipos.pop()
                result_type = self.scube.matchTypes(type_result, type1, currOp)
                if result_type != "ERROR":
                    new_quad = [currOp, op1, "", result]
                    self.quads.append(new_quad)
        
        print(self.quads)
