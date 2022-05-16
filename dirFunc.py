class dirFunc:

    def __init__(self):
        self.misFunciones = {"Global" : {
                                        "tipo" : "VOID",
                                        "variables" : {}
                                    }
                            }
    
    def addFunc(self, newFunc, newType):
        self.misFunciones[newFunc] = {
            "tipo" : newType,
            "variables" : {}
        }
    
    def addType(self, currFunc, currType):
        self.misFunciones[currFunc].append(currType)
    
    def getFuncType(self, currFunc):
        return self.misFunciones[currFunc][0]
    
    def addVar(self, currFunc, currVar):
        self.misFunciones[currFunc][1]