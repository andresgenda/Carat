# ------------- Clase Quadruples -------------
# Genera los cuádruplos según el tipo de operación

from semanticube import SemanticCube
from helpers import Helpers
from stack import Stack

class Quadruples:

    def __init__(self):
        self.scube = SemanticCube()
        self.help = Helpers()

    #Imprime los cuádruplos comenzando desde el 1
    def printQuads(self, misNuevosQuads):
        for (i, item) in enumerate(misNuevosQuads, start=1):
            print(i, item)
    
    #Saca el último cuádruplo generado (GOTO), y lo llena con el último salto en la pila
    def fillGotoWhile(self, miStackJmps, misNuevosQuads):
        quadToFill = miStackJmps.pop()
        myGoto = miStackJmps.pop()
        misNuevosQuads[quadToFill][3] = myGoto
    
    #Saca dos elementos de la pila de saltos, y actualiza el cuádruplo con el número del segundo
    #elemento que se saco de la pila con el número del primer elemento que se saco
    def fillGoto(self, miStackJmps, misNuevosQuads):
        #A donde voy a realizar mi salto
        myGoto = miStackJmps.pop()
        #El número de cuádruplo que voy a llenar
        quadToFill = miStackJmps.pop()
        misNuevosQuads[quadToFill][3] = myGoto
    
    def emptyExpNoEqual(self, miStackOpernds, miStackTps, miStackOps, misNuevosQuads, memVir, dirFuncs, currFunc):
        while miStackOps.top() != "EQUAL" and miStackOps.top() != -1:
            checkOp = miStackOps.pop()
            self.executeQuadGenCopy(checkOp, miStackOpernds, miStackTps, misNuevosQuads, memVir, dirFuncs, currFunc)
    
    #Vacía el stack de operaciones hasta llegar a un paréntesis abierto
    def emptyParenth(self, miStackOpernds, miStackTps, miStackOps, misNuevosQuads, memVir, dirFuncs, currFunc):
        while miStackOps.top() != "OPEN_PARENTH":
            checkOp = miStackOps.pop()
            self.executeQuadGenCopy(checkOp, miStackOpernds, miStackTps, misNuevosQuads, memVir, dirFuncs, currFunc)
        miStackOps.pop()
    
    #Genera el cuádruplo de escritura o lectura
    def read_writeQuad(self, op, var, misNuevosQuads):
        new_quad = [op, "", "", var]
        misNuevosQuads.append(new_quad)
    
    #Funcion que checa el tipo de operación y realiza el cuádruplo correspondiente, o bien manda a llamar a la función de
    #generación correspondiente
    def assignQuadCopy(self, miStackOpernds, miStackTps, miStackOps, misNuevosQuads, memVir, dirFuncs, currFunc):
        while miStackOps.isEmpty() == False:
            checkOp = miStackOps.pop()
            currOp = checkOp
            checkOp = self.help.getOperationType(checkOp)
            #ARIT O COMP
            if checkOp == 1 or checkOp == 2 or checkOp == 4:
                self.executeQuadGenCopy(currOp, miStackOpernds, miStackTps, misNuevosQuads, memVir, dirFuncs, currFunc)
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

    #Funcion que recibe la operación por generar, utiliza los primeros dos elementos de la pila de operandos
    #y en base a ellos calcula la dirección en donde se va a almacenar el resultado
    def executeQuadGenCopy(self, currOp, miStackOpernds, miStackTps, misNuevosQuads, memVir, dirFuncs, currFunc):
        op2 = miStackOpernds.pop()
        op1 = miStackOpernds.pop()
        type2 = miStackTps.pop()
        type1 = miStackTps.pop()
        result_type = self.scube.matchTypes(type1, type2, currOp)
        if result_type != "ERROR":
            result = memVir.getNextDir(result_type, 2)
            dirFuncs.setNumTemps(currFunc, result_type)
            new_quad = [currOp, op1, op2, result]
            misNuevosQuads.append(new_quad)
            miStackOpernds.push(result)
            miStackTps.push(result_type)