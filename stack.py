class Stack:
    def __init__(self):
        self.myStack=[]
    
    def isEmpty(self):
        return self.myStack == []
    
    def push(self, newItem):
        self.myStack.append(newItem)
    
    def pop(self):
        return self.myStack.pop()
    
    def top(self):
        if(self.myStack == []):
            return -1
        return self.myStack[-1]
    
    def pr(self):
        for i in self.myStack:
            print(i)