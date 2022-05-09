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
    
    def assignQuadCopy(self, miStackOpernds, miStackTps, miStackOps, misNuevosQuads):
        while miStackOps.isEmpty() == False:
            checkOp = miStackOps.pop()
            currOp = checkOp
            checkOp = self.help.getOperationType(checkOp)
            #SUMA O RESTA
            if checkOp != 3:
                self.executeQuadGenCopy(currOp, miStackOpernds, miStackTps, misNuevosQuads)
            #IGUAL
            else:
                op1 = miStackOpernds.pop()
                type1 = miStackTps.pop()
                result = miStackOpernds.pop()
                type_result = miStackTps.pop()
                result_type = self.scube.matchTypes(type_result, type1, currOp)
                if result_type != "ERROR":
                    new_quad = [currOp, op1, "", result]
                    misNuevosQuads.append(new_quad)
    
    def executeQuadGenCopy(self, currOp, miStackOpernds, miStackTps, misNuevosQuads):
        op2 = miStackOpernds.pop()
        op1 = miStackOpernds.pop()
        type2 = miStackTps.pop()
        type1 = miStackTps.pop()
        result_type = self.scube.matchTypes(type1, type2, currOp)
        if result_type != "ERROR":
            result = self.evalQuad(currOp, op1, op2)
            new_quad = [currOp, op1, op2, result]
            misNuevosQuads.append(new_quad)
            miStackOpernds.push(result)
            miStackTps.push(result_type)
    
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
    
    #------------------------------------------------------ A PARTIR DE AQUI CREO QUE YA NO LO VOY A USAR
    
    #FUNCION PARA CUANDO TENGO UNA OPERACION "="
    def assignQuad(self, miStackOpernds, miStackTps, misNuevosQuads):
        op1 = miStackOpernds.pop()
        type1 = miStackTps.pop()
        result = miStackOpernds.pop()
        type_result = miStackTps.pop()
        result_type = self.scube.matchTypes(type_result, type1, "EQUAL")
        if result_type != "ERROR":
            new_quad = ["EQUAL", op1, "", result]
            misNuevosQuads.append(new_quad)

    def executeQuadGen(self, currOp):
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
                        currOp = self.stackOperaciones.pop()
                        self.stackOperaciones.push(currTok)
                        self.executeQuadGen(currOp)
                    elif self.stackOperaciones.top() == "ADD" or self.stackOperaciones.top() == "SUBSTR":
                        currOp = self.stackOperaciones.pop()
                        self.stackOperaciones.push(currTok)
                        self.executeQuadGen(currOp)
                    elif self.stackOperaciones.top() == "EQUAL":
                        self.stackOperaciones.push(currTok)
                #AQUI ES POR SI ME LLEGA UNA MULT O DIV
                elif checkOp == 2:
                    if self.stackOperaciones.top() == "MULT" or self.stackOperaciones.top() == "DIVIS":
                        currOp = self.stackOperaciones.pop()
                        self.stackOperaciones.push(currTok)
                        self.executeQuadGen(currOp)
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
            if checkOp != 3:
                self.executeQuadGen(currOp)
            #IGUAL
            else:
                op1 = self.stackOperandos.pop()
                type1 = self.stackTipos.pop()
                result = self.stackOperandos.pop()
                type_result = self.stackTipos.pop()
                result_type = self.scube.matchTypes(type_result, type1, currOp)
                if result_type != "ERROR":
                    new_quad = [currOp, op1, "", result]
                    self.quads.append(new_quad)
        
        print(self.quads)
