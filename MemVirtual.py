from helpers import Helpers

class MemVirtual:

    #Globales -> 1000-1999
    #Locales -> 2000 - 2999
    #Temporales -> 3000 - 3999
    #Constantes -> 4000 - 4999
    def __init__(self):
        self.help = Helpers()
        self.myMemory = self.initMemoria()
        self.myConstants = [[],[],[],[]]
    
    def initMemoria(self):
        glob= [1000, 1250, 1500, 1750]
        loc = [2000, 2250, 2500, 2750]
        temps = [3000, 3250, 3500, 3750]
        cte = [4000, 4250, 4500, 4750]
        return [glob, loc, temps, cte]
    
    def getSegment(self, seg):
        if seg == "INT":
            return 0
        elif seg == "FLOAT":
            return 1
        elif seg == "STRING":
            return 2
        else:
            return 3
    
    def getNextDir(self, curr_type, scope):
        segment = self.help.getOperatorType(curr_type)
        if segment == "INT":
            address = self.myMemory[scope][0]
            self.myMemory[scope][0]+=1
            return address
        elif segment == "FLOAT":
            address = self.myMemory[scope][1]
            self.myMemory[scope][1]+=1
            return address
        elif segment == "STRING":
            address = self.myMemory[scope][2]
            self.myMemory[scope][2]+=1
            return address
        elif segment == "BOOL":
            address = self.myMemory[scope][3]
            self.myMemory[scope][3]+=1
            return address
    
    def assignCte(self, curr_type, curr_val):
        segment = self.help.getOperatorType(curr_type)
        segment = self.getSegment(segment)
        if curr_val not in self.myConstants[segment]:
            self.myConstants[segment].append(curr_val)
            self.getNextDir(curr_type, 3)
    
    def getCteDir(self, curr_val, curr_type):
        segment = self.help.getOperatorType(curr_type)
        segmentNum = self.getSegment(segment)
        index = self.myConstants[segmentNum].index(curr_val)
        if segment == "INT":
            return index + 4000
        elif segment == "FLOAT":
            return index + 4250
        elif segment == "STRING":
            return index + 4500
        else:
            return index + 4750
    
    def resetLocalVars(self):
        self.myMemory[2] = [2000, 2250, 2500, 2750]
