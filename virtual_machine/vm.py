import csv
import turtle
from stack import Stack
from pathlib import Path
from virtual_machine.memVirtM import MemVirtM

class vm:
    
    def __init__(self):
        self.impQuads = []
        self.impCtes = []
        self.impFuncs = {}
        self.activeMems = Stack()
        self.globalMem = ""
        self.currMem = ""
        self.newMem = ""
        self.stackJumps = Stack()
        self.canvas = turtle.Turtle()
    
    def execute(self):
        self.importFiles()
        self.startGlobalMem()
        self.execQuads()
        
    def importFiles(self):
        self.importQuads()
        self.importCtes()
        self.importFuncs()
    
    def importQuads(self):
        with open("ExportedFiles/exportedQuads.csv") as file:
            file = csv.reader(file)
            for row in file:
                cont = 0
                while(cont < 4):
                    row[cont] = row[cont].replace("[","")
                    row[cont] = row[cont].replace("]","")
                    row[cont] = row[cont].replace(" ","")
                    if row[cont].isdigit():
                        row[cont] = int(row[cont])
                    cont += 1
                self.impQuads.append(row)
    
    def importCtes(self):
        with open("ExportedFiles/exportedCtes.csv") as file:
            file = csv.reader(file)
            rowCont = 0
            for row in file:
                cont = 0
                while(cont < len(row)):
                    if rowCont != 2:
                        row[cont] = row[cont].replace("[","")
                        row[cont] = row[cont].replace("]","")
                        row[cont] = row[cont].replace(" ","")
                        row[cont] = row[cont].replace("'", "")
                        if rowCont == 0:
                            if row[cont] != '':
                                row[cont] = int(row[cont])
                        elif rowCont == 1:
                            if row[cont] != '':
                                row[cont] = float(row[cont])
                    else:
                        row[cont] = row[cont].replace("[","")
                        row[cont] = row[cont].replace("]","")
                        row[cont] = row[cont].replace("'", "")
                    cont += 1
                rowCont += 1
                self.impCtes.append(row)
            #print(self.impCtes)
    
    def importFuncs(self):
        with open("ExportedFiles/exportedFuncs.csv") as file:
            file = csv.reader(file)
            for row in file:
                cont = 1
                while(cont < len(row)):
                    if row[cont].isdigit():
                        row[cont] = int(row[cont])
                    elif isinstance(row[cont], str):
                        row[cont] = row[cont].replace("\'", "")
                    cont += 1
                self.impFuncs[row[0]] = row[1:]
    
    def startGlobalMem(self):
        self.globalMem = MemVirtM(self.impFuncs["Carat"])
        self.currMem = self.globalMem
        self.activeMems.push(self.globalMem)
    
    def getDirValue(self, dir):
        if dir < 2000:
            return self.globalMem.getVal(dir)
        elif dir < 4000:
            return self.currMem.getVal(dir)
        elif dir < 5000:
            return self.getCteValue(dir)
        

    def getCteValue(self, dir):
        baseType = dir - 4000
        if baseType < 250:
            return self.impCtes[0][baseType]
        elif baseType < 500:
            return self.impCtes[1][baseType-250]
        elif baseType < 750:
            return self.impCtes[2][baseType-500]
        else:
            return self.impCtes[3][baseType-750]
    
    def assignValToDir(self, dir, val):
        if dir < 2000:
            self.globalMem.assignVal(dir, val)
        else:
            self.currMem.assignVal(dir, val)
    
    def execQuads(self):
        gotoMain = self.impQuads[0][3]
        cont = gotoMain - 1
        while(cont < len(self.impQuads)):
            quadToExec = self.impQuads[cont]
            currOp = quadToExec[0]
            op1 = quadToExec[1]
            op2 = quadToExec[2]
            res = quadToExec[3]
            #ARITMETHIC OPERATIONS ------------------------------------------------------------
            if currOp < 5:
                op1Val = self.getDirValue(op1)
                op2Val = self.getDirValue(op2)
                #CURRENT OPERATION -> ADD
                if currOp == 1:
                    self.assignValToDir(res, op1Val + op2Val)
                #CURRENT OPERATION -> SUBSTRACT
                elif currOp == 2:
                    self.assignValToDir(res, op1Val - op2Val)
                #CURRENT OPERATION -> MULTIPLICATION
                elif currOp == 3:
                    self.assignValToDir(res, op1Val * op2Val)
                #CURRENT OPERATION -> DIVISION
                elif currOp == 4:
                    op1type = op1 % 1000
                    op2type = op2 % 1000
                    if op1type >= 250 or op2type >= 250:
                        self.assignValToDir(res, op1Val / op2Val)
                    else:
                        self.assignValToDir(res, op1Val // op2Val)
            #ARITMETHIC OPERATIONS END --------------------------------------------------------
            #CURRENT OPERATION -> ASSIGN
            elif currOp == 5:
                op1Val = self.getDirValue(op1)
                self.assignValToDir(res, op1Val)
            #COMPARISON OPERATIONS ------------------------------------------------------------
            elif currOp < 10:
                op1Val = self.getDirValue(op1)
                op2Val = self.getDirValue(op2)
                #CURRENT OPERATION -> MORE THAN '>'
                if currOp == 6:
                    self.assignValToDir(res, op1Val > op2Val)
                #CURRENT OPERATION -> LESS THAN '<'
                elif currOp == 7:
                    self.assignValToDir(res, op1Val < op2Val)
                #CURRENT OPERATION -> IS EQUAL TO '=='
                elif currOp == 8:
                    self.assignValToDir(res, op1Val == op2Val)
                #CURRENT OPERATION -> IS DIFFERENT THAN '!='
                elif currOp == 9:
                    self.assignValToDir(res, op1Val != op2Val)
            #COMPARISON OPERATIONS END --------------------------------------------------------
            #CURRENT OPERATION -> PRINT
            elif currOp == 10:
                resValue = self.getDirValue(res)
                print(resValue)
            #CURRENT OPERATION -> INPUT
            elif currOp == 11:
                resType = res % 1000
                if resType < 250:
                    resVal = int(input())
                else:
                    resVal = float(input())
                self.assignValToDir(res, resVal)
            #CURRENT OPERATION -> GOTO
            elif currOp == 12:
                cont = res - 2
            #CURRENT OPERATION -> GOTO (FALSE)
            elif currOp == 13:
                op1Val = self.getDirValue(op1)
                if(op1Val == False):
                    cont = res - 2
            #CURRENT OPERATION -> GOSUB (Go to the start of a function)
            elif currOp == 14:
                self.stackJumps.push(cont)
                self.currMem = self.newMem
                self.activeMems.push(self.currMem)
                cont = res - 2
            #CURRENT OPERATION -> ERA (Start the new memory for the function)
            elif currOp == 15:
                funcName = res
                self.newMem = MemVirtM(self.impFuncs[funcName])
            #CURRENT OPERATION -> PARAM (Send over the parameters)
            elif currOp == 16:
                valueToPass = self.getDirValue(op1)
                self.newMem.assignVal(2000 + res, valueToPass)
            #CURRENT OPERATION -> END (The program ends)
            elif currOp == 17:
                turtle.done()
                break
            #CURRENT OPERATION -> ENDFUNC (The current function ends)
            elif currOp == 18:
                self.activeMems.pop()
                self.currMem = self.activeMems.top()
                cont = self.stackJumps.pop()
            #CURRENT OPERATION -> RETURN
            elif currOp == 19:
                resVal = self.getDirValue(res)
                self.assignValToDir(op1, resVal)
                self.activeMems.pop()
                self.currMem = self.activeMems.top()
                cont = self.stackJumps.pop()
            #CURRENT OPERATION -> LINEUP (Pinta una linea para arriba en la direccion que va)
            elif currOp == 20:
                resVal = self.getDirValue(res)
                self.canvas.forward(resVal)
            #CURRENT OPERATION -> LINEDOWN (Pinta una linea para abajo en la direccion que va)
            elif currOp == 21:
                resVal = self.getDirValue(res)
                self.canvas.backward(resVal)
            #CURRENT OPERATION -> RIGHT (Cambia el angulo hacia la derecha)
            elif currOp == 22:
                resVal = self.getDirValue(res)
                self.canvas.right(resVal)
            #CURRENT OPERATION -> LEFT (Cambia el angulo hacia la izquierda)
            elif currOp == 23:
                resVal = self.getDirValue(res)
                self.canvas.left(resVal)
            #CURRENT OPERATION -> CLEAR (Borra lo que se había dibujado)
            elif currOp == 24:
                self.canvas.clear()
            #CURRENT OPERATION -> PINTAR (Baja la pluma para pintar mientras se mueve)
            elif currOp == 25:
                self.canvas.pendown()
            #CURRENT OPERATION -> NO PINTAR (Sube la pluma para no pintar mientras se mueve)
            elif currOp == 26:
                self.canvas.penup()

            
            cont += 1