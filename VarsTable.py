from Var import Var
from Error import Error
from Var import Var

class VarsTable:
    def __init__(self):
        self.table = {}

    def add(self, name, type, scope):
        currentVar = Var(type, scope)
        if name in self.table:
            return Error("Variable already declared")
        else:
            self.table[name] = currentVar 
            return None

    def search(self, name):
        if name in self.table:
            return self.table[name], None
        else: return None, Error('Variable not declared')
