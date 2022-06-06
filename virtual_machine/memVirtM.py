# ------------- Clase MemVirtM -------------
# Clase que genera una memoria para cada función dentro de la máquina virtual

class MemVirtM:

    #Inicia cinco arreglos con los espacios necesarios según la tabla de funciones
    def __init__(self, currFunc):
        self.varsInt = [0 for i in range(currFunc[1])]
        self.varsFl = [0 for i in range(currFunc[2])]
        self.tempsInt = [0 for i in range(currFunc[3])]
        self.tempsFl = [0 for i in range(currFunc[4])]
        self.tempsBool = [0 for i in range(currFunc[5])]
    
    #Regresa el valor que se encuentra en el arreglo correspondiente a la dirección y al índice
    def getVal(self, dir):
        if dir < 2000:
            baseType = dir - 1000
            if baseType < 250:
                return self.varsInt[baseType]
            elif baseType < 500:
                return self.varsFl[baseType - 250]
        elif dir < 3000:
            baseType = dir - 2000
            if baseType < 250:
                return self.varsInt[baseType]
            elif baseType < 500:
                return self.varsFl[baseType - 250]
        elif dir < 4000:
            baseType = dir - 3000
            if baseType < 250:
                return self.tempsInt[baseType]
            elif baseType < 500:
                return self.tempsFl[baseType - 250]
            elif baseType >= 750:
                return self.tempsBool[baseType - 750]
    
    #Asigna el valor correspondiente de acuerdo a la dirección y al índice
    def assignVal(self, dir, value):
        if dir < 2000:
            baseType = dir - 1000
            if baseType < 250:
                self.varsInt[baseType] = value
            elif baseType < 500:
                self.varsFl[baseType - 250] = value
        elif dir < 3000:
            baseType = dir - 2000
            if baseType < 250:
                self.varsInt[baseType] = value
            elif baseType < 500:
                self.varsFl[baseType - 250] = value
        elif dir < 4000:
            baseType = dir - 3000
            if baseType < 250:
                self.tempsInt[baseType] = value
            elif baseType < 500:
                self.tempsFl[baseType - 250] = value
            elif baseType >= 750:
                self.tempsBool[baseType - 750] = value

    #Auxiliar para imprimir         
    def pr(self):
        print(self.varsInt)
        print(self.varsFl)
        print(self.tempsInt)
        print(self.tempsFl)
        print(self.tempsBool)