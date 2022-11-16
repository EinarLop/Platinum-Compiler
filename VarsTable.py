from Var import Var
from Error import Error
from Var import Var



class VarsTable:
    def __init__(self):
        self.table = {}
        self.iCounter = 0
        self.fCounter = 0
        self.cCounter = 0
        self.bCounter = 0

    def add(self, name, type, scope, address,dim):
        currentVar = Var(type, scope, address,dim)
        if name in self.table:
            return Error("Variable already declared")
        else:
            self.table[name] = currentVar
            return None

    def search(self, name):
        if name in self.table:
            return self.table[name], None
        else: return None, Error('Variable not declared')

    def toString(self):
        for key in self.table:
            print(f"{key}: {self.table[key].type}, {self.table[key].address}, {self.table[key].dim} ")
