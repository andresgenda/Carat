import csv

class vm:
    
    def __init__(self):
        self.impQuads = []
        self.impCtes = []
        self.mem = {}
    
    def execute(self):
        self.importFiles()
        self.execQuads()
        
    def importFiles(self):
        self.importQuads()
        self.importCtes()
    
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
                    cont += 1
                rowCont += 1
                self.impCtes.append(row)
            #print(self.impCtes)
    
    def getDirValue(self, dir):
        if dir < 2000:
            #print("AQUI BUSCARE EN GLOBALES")
            return self.mem[dir]
        elif dir < 3000:
            print("AQUI BUSCARE EN LOCALES")
        elif dir < 4000:
            #print("AQUI BUSCARE EN TEMPS")
            return self.mem[dir]
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
        self.mem[dir] = val
    
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
                print("GOSUB")
            #CURRENT OPERATION -> ERA (Start the new memory for the function)
            elif currOp == 15:
                print("ERA")
            #CURRENT OPERATION -> PARAM (Send over the parameters)
            elif currOp == 16:
                print("PARAM")
            #CURRENT OPERATION -> END (The program ends)
            elif currOp == 17:
                break
            #CURRENT OPERATION -> ENDFUNC (The current function ends)
            elif currOp == 18:
                print("ENDFUNC")
            
            cont += 1