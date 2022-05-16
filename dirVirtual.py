class dirVirtual:

    #Globales -> 1000-1999
    #Locales -> 2000 - 2999
    #Temporales -> 3000 - 3999
    #Constantes -> 4000 - 4999
    def __init__(self):
        self.memgral = [1000, 2000, 3000, 4000]
        self.maxV = 250
        self.memory = self.initMem()
    
    def initMem(self):
        glob = [1000, 1250, 1500, 1750]
        loc = [2000, 2250, 2500, 2750]
        temps = [3000, 3250, 3500, 3750]
        cte = [4000, 4250, 4500, 4750]
        return [glob, loc, temps, cte]
    
    def getScope(self, currScope):
        if currScope == "global":
            return 0
        elif currScope == "local":
            return 1
        elif currScope == "temporal":
            return 2
        elif currScope == "constante":
            return 3

    