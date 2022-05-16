class quadOrigin:

    def __init__(self):
        self.quad = {
            "operation" : "",
            "op1" : "",
            "op2" : "",
            "result" : ""
        }
    
    def updateOperation(self, op):
        self.quad["operation"] = op
    
    def updateOp1(self, op1):
        self.quad["op1"] = op1
    
    def updateOp2(self, op2):
        self.quad["op2"] = op2

    def updateResult(self, res):
        self.quad["result"] = res