class Helpers:

    def aplana(self, miLista):
        if miLista == []:
            return miLista
        if isinstance(miLista[0], list):
            return self.aplana(miLista[0]) + self.aplana(miLista[1:])
        return miLista[:1] + self.aplana(miLista[1:])
    
    def checkVars(self, miLista):
        if miLista[0].gettokentype() == "SEMI_COLON":
            print("FINALLY")
        else:
            self.checkVars(miLista[1:])