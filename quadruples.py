from semanticube import SemanticCube

class Quadruples:

    def evalQuads(self, tokenList):
        stackOperandos = []
        #stackTipos = []
        stackOperaciones = []

        for currOp in tokenList:
            currVal = currOp.value
            currTok = currOp.gettokentype()
            if currTok == "ID":
                stackOperandos.append(currVal)
            elif currTok == "EQUAL":
                stackOperaciones.append(currVal)
            elif currTok == "ADD":
                stackOperaciones.append(currVal)
            elif currTok == "CTE_INT":
                stackOperandos.append(currVal)
        
        print(stackOperaciones)
        print(stackOperandos)