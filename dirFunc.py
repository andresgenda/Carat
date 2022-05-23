class DirFunc:

    def __init__(self):
        self.misFunciones = {}
    
    def addFunc(self, newFunc, newType):
        self.misFunciones[newFunc] = {
            "tipo" : newType,
            "startDir" : "",
            "size" : "",
            "params" : [],
            "vars" : {}
        }
    
    def getFuncType(self, currFunc):
        return self.misFunciones[currFunc][0]
    
    def addVar(self, currFunc, currVars):
        self.misFunciones[currFunc]["vars"] = currVars
    
    def addParams(self, currFunc, currParams):
        self.misFunciones[currFunc]["params"] = currParams
    
    def getVarMem(self, currFunc, currID):
        return self.misFunciones[currFunc]["vars"][currID][1]
    
    def getIDType(self, currFunc, currID):
        return self.misFunciones[currFunc]["vars"][currID][0]
    
    def getVars(self, currFunc):
        return self.misFunciones[currFunc]["vars"]

    def pr(self):
        for key in self.misFunciones:
            print("----------- FUNCION", key, "-----------")
            print("Tipo:", self.misFunciones[key]["tipo"])
            print("Direccion de inicio:", self.misFunciones[key]["startDir"])
            print("Tamaño:", self.misFunciones[key]["size"])
            print("Parametros:", self.misFunciones[key]["params"])
            print("Variables:", self.misFunciones[key]["vars"])