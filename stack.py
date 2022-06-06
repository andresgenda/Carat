# ------------- Clase Stack -------------
#Inicia un arreglo vacío para poder trabajar con él como si fuera un Stack
class Stack:
    def __init__(self):
        self.myStack=[]
    
    #Regresa si el arreglo está vacío
    def isEmpty(self):
        return self.myStack == []
    
    #Agrega un elemento al arreglo
    def push(self, newItem):
        self.myStack.append(newItem)
    
    #Saca el último elemento del arreglo y lo regresa
    def pop(self):
        return self.myStack.pop()
    
    #Revisa el último elemento del arreglo, o bien, el tope del Stack
    def top(self):
        if(self.myStack == []):
            return -1
        return self.myStack[-1]
    
    #Imprime los elementos del arreglo
    def pr(self):
        for i in self.myStack:
            print(i)