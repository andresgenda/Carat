class constants:

    def __init__(self):
        self.ctes = [[],[],[],[]]
    
    def addCte(self, value):
        if value not in self.ctes:
            self.ctes.append(value)
    