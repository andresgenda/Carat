# ------------- Clase DirFunc -------------
# Clase encargada de crear y manejar funciones que conciernen a la tabla de variables

import numpy as np

class DirFunc:

    def __init__(self):
        self.misFunciones = {}
    
    #Agrega una nueva función a la tabla de funciones
    def addFunc(self, newFunc, newType):
        self.misFunciones[newFunc] = {
            "tipo" : newType,
            "startDir" : "",
            "numParamsInt" : 0,
            "numParamsFl" : 0,
            "numLocalsInt" : 0,
            "numLocalsFl" : 0,
            "numVarsInt" : 0,
            "numVarsFl" : 0,
            "numTempsInt" : 0,
            "numTempsFl" : 0,
            "numTempsBl" : 0,
            "params" : [],
            "vars" : {}
        }
    
    #Regresa el tipo de la funcion
    def getFuncType(self, currFunc):
        return self.misFunciones[currFunc]["tipo"]
    
    #Agrega una tabla de variables
    def addVar(self, currFunc, currVars):
        self.misFunciones[currFunc]["vars"] = currVars
    
    #Agrega la tabla de parametros
    def addParams(self, currFunc, currParams):
        self.misFunciones[currFunc]["params"] = currParams
    
    #Regresa el parámetro correspondiente al índice que se busca
    def getParam(self, currFunc, currIdx):
        #Si el índice está fuera de rango, no existe
        if currIdx >= len(self.misFunciones[currFunc]["params"]):
            return -1
        return self.misFunciones[currFunc]["params"][currIdx]
    
    #Regresa la dirección de memoria de la variable
    def getVarMem(self, currFunc, currID):
        return self.misFunciones[currFunc]["vars"][currID][1]
    
    #Regresa el tipo de la variable
    def getIDType(self, currFunc, currID):
        return self.misFunciones[currFunc]["vars"][currID][0]
    
    #Regresa las variables de la función
    def getVars(self, currFunc):
        return self.misFunciones[currFunc]["vars"]
    
    #Asigna la dirección de inicio de la función
    def setStart(self, currFunc, start):
        self.misFunciones[currFunc]["startDir"] = start
    
    #Regresa la dirección de inicio de la función
    def getStart(self, currFunc):
        return self.misFunciones[currFunc]["startDir"]
    
    #Le suma 1 al número de parámetros
    def setNumParams(self, currFunc):
        for key in self.misFunciones[currFunc]["params"]:
            if key == "INT":
                self.misFunciones[currFunc]["numParamsInt"] += 1
            elif key == "FLOAT":
                self.misFunciones[currFunc]["numParamsFl"] += 1
    
    #Le suma 1 al número de variables
    def setNumVars(self, currFunc):
        for key in self.misFunciones[currFunc]["vars"]:
            if self.misFunciones[currFunc]["vars"][key][0] == "INT":
                self.misFunciones[currFunc]["numLocalsInt"] += 1
            elif self.misFunciones[currFunc]["vars"][key][0] == "FLOAT":
                self.misFunciones[currFunc]["numLocalsFl"] += 1

    #Le suma 1 al número de temporales
    def setNumTemps(self, currFunc, currType):
        if currType == "INT":
            self.misFunciones[currFunc]["numTempsInt"] += 1
        elif currType == "FLOAT":
            self.misFunciones[currFunc]["numTempsFl"] += 1
        elif currType == "BOOL":
            self.misFunciones[currFunc]["numTempsBl"] += 1
    
    #Exporta el arreglo creado de funciones
    def exportFuncs(self):
        myFuncs = np.array(self.dictToArray())
        np.savetxt('ExportedFiles/exportedFuncs.csv', myFuncs, delimiter=",", fmt="%s")
    
    #Hace que el diccionario ahora sea un arreglo para su exportación
    def dictToArray(self):
        funcsArray = []
        for key in self.misFunciones:
            currFunc = []
            currFunc.append(key)
            funcInfo = self.misFunciones[key]
            currFunc.append(funcInfo["tipo"])
            currFunc.append(funcInfo["numVarsInt"])
            currFunc.append(funcInfo["numVarsFl"])
            currFunc.append(funcInfo["numTempsInt"])
            currFunc.append(funcInfo["numTempsFl"])
            currFunc.append(funcInfo["numTempsBl"])
            funcsArray.append(currFunc)
        return funcsArray
    
    #Elimina una llave
    def deleteKey(self, currFunc, key):
        self.misFunciones[currFunc].pop(key)
    
    #Asigna el número total de variables
    def setVarsTotal(self, currFunc):
        locVarsInt = self.misFunciones[currFunc]["numLocalsInt"]
        self.misFunciones[currFunc]["numVarsInt"] = locVarsInt
        locVarsFl = self.misFunciones[currFunc]["numLocalsFl"]
        self.misFunciones[currFunc]["numVarsFl"] = locVarsFl

    #Auxiliar para imprimir mis funciones
    def pr(self):
        for key in self.misFunciones:
            print("----------- FUNCION", key, "-----------")
            print("Tipo:", self.misFunciones[key]["tipo"])
            print("Direccion de inicio:", self.misFunciones[key]["startDir"])
            print("Numero de variables locales enteras:", self.misFunciones[key]["numVarsInt"])
            print("Numero de variables locales flotantes:", self.misFunciones[key]["numVarsFl"])
            print("Numero de temporales enteras:", self.misFunciones[key]["numTempsInt"])
            print("Numero de temporales flotantes:", self.misFunciones[key]["numTempsFl"])
            print("Numero de temporales booleanas:", self.misFunciones[key]["numTempsBl"])