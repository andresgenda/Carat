class Helpers:

    def aplana(self, miLista):
        if miLista == []:
            return miLista
        if isinstance(miLista[0], list):
            return self.aplana(miLista[0]) + self.aplana(miLista[1:])
        return miLista[:1] + self.aplana(miLista[1:])
    
    def checkVars(self, miLista, misVars, tipo):
        currVar = []
        if miLista[0].gettokentype() == "SEMI_COLON":
            return
        else:
            if miLista[0].gettokentype() == "ID":
                currVar.append(miLista[0].value)
                currVar.append(tipo)
                misVars.append(currVar)
            self.checkVars(miLista[1:], misVars, tipo)