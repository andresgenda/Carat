class DirFunc:

    def __init__(self):
        self.misFunciones = {}
    
    def addFunc(self, newFunc, newType):
        self.misFunciones[newFunc] = {
            "tipo" : newType,
            "startDir" : "",
            "numParams" : "",
            "numLocals" : "",
            "numTemps" : "",
            "params" : [],
            "vars" : {}
        }
    
    def getFuncType(self, currFunc):
        return self.misFunciones[currFunc][0]
    
    def addVar(self, currFunc, currVars):
        self.misFunciones[currFunc]["vars"] = currVars
    
    def addParams(self, currFunc, currParams):
        self.misFunciones[currFunc]["params"] = currParams
    
    def getParam(self, currFunc, currIdx):
        if currIdx >= len(self.misFunciones[currFunc]["params"]):
            return -1
        return self.misFunciones[currFunc]["params"][currIdx]
    
    def getVarMem(self, currFunc, currID):
        return self.misFunciones[currFunc]["vars"][currID][1]
    
    def getIDType(self, currFunc, currID):
        return self.misFunciones[currFunc]["vars"][currID][0]
    
    def getVars(self, currFunc):
        return self.misFunciones[currFunc]["vars"]
    
    def setStart(self, currFunc, start):
        self.misFunciones[currFunc]["startDir"] = start
    
    def getStart(self, currFunc):
        return self.misFunciones[currFunc]["startDir"]
    
    def setNumParams(self, currFunc):
        size = len(self.misFunciones[currFunc]["params"])
        self.misFunciones[currFunc]["numParams"] = size

    def pr(self):
        for key in self.misFunciones:
            print("----------- FUNCION", key, "-----------")
            print("Tipo:", self.misFunciones[key]["tipo"])
            print("Direccion de inicio:", self.misFunciones[key]["startDir"])
            print("Numero de parametros:", self.misFunciones[key]["numParams"])
            print("Numero de variables locales:", self.misFunciones[key]["numLocals"])
            print("Numero de temporales:", self.misFunciones[key]["numTemps"])
            print("Parametros:", self.misFunciones[key]["params"])
            print("Variables:", self.misFunciones[key]["vars"])