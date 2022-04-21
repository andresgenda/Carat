from llvmlite import ir

class Success():
    def eval(self):
        print(self.value.eval())
