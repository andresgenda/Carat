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

    def printQuads(self, misNuevosQuads):
        for (i, item) in enumerate(misNuevosQuads, start=1):
            print(i, item)
    
    def fillGotoWhile(self, miStackJmps, misNuevosQuads):
        quadToFill = miStackJmps.pop()
        myGoto = miStackJmps.pop()
        misNuevosQuads[quadToFill][3] = myGoto
    
    def fillGoto(self, miStackJmps, misNuevosQuads):
        myGoto = miStackJmps.pop()
        quadToFill = miStackJmps.pop()
        misNuevosQuads[quadToFill][3] = myGoto
    
    def emptyParenth(self, miStackOpernds, miStackTps, miStackOps, misNuevosQuads):
        while miStackOps.top() != "OPEN_PARENTH":
            checkOp = miStackOps.pop()
            self.executeQuadGenCopy(checkOp, miStackOpernds, miStackTps, misNuevosQuads)
        miStackOps.pop()
    
    def read_writeQuad(self, op, var, misNuevosQuads):
        new_quad = [op, "", "", var]
        misNuevosQuads.append(new_quad)
    
    def assignQuadCopy(self, miStackOpernds, miStackTps, miStackOps, misNuevosQuads):
        while miStackOps.isEmpty() == False:
            checkOp = miStackOps.pop()
            currOp = checkOp
            checkOp = self.help.getOperationType(checkOp)
            #ARIT O COMP
            if checkOp == 1 or checkOp == 2 or checkOp == 4:
                self.executeQuadGenCopy(currOp, miStackOpernds, miStackTps, misNuevosQuads)
            #PRINT
            elif checkOp == 5:
                result = miStackOpernds.pop()
                type_result = miStackTps.pop()
                new_quad = [currOp, "", "", result]
                misNuevosQuads.append(new_quad)
            #IGUAL
            elif checkOp == 3:
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
            return str(op1)