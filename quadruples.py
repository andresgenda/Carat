from semanticube import SemanticCube
from helpers import Helpers

class Quadruples:

    def __init__(self):
        self.scube = SemanticCube()
        self.help = Helpers()

    def evalQuads(self, tokenList):
        stackOperandos = []
        stackTipos = []
        stackOperaciones = []

        print(tokenList)

        for currOp in tokenList:
            currVal = currOp.value
            currTok = currOp.gettokentype()

            #Check if my current token is an operation or an operator
            checkToken = self.help.operator_operation(currTok)

            if checkToken == 1:
                stackOperaciones.append(currVal)
            elif checkToken == 2:
                stackOperandos.append(currVal)
                stackTipos.append(currTok)
            elif checkToken == 3:
                stackOperandos.append(currTok)
                stackTipos.append("h")
        
        print(stackOperaciones)
        print(stackOperandos)
        print(stackTipos)
        self.scube.matchTypes("INT", "INT","ADD")

        # mivar1 = 1 + 2 * 3 * 4 + 5 / 6 * 7

        #si es plus o menos
        #div o mult