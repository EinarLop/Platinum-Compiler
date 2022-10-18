from Error import Error
from Class import Class

class ClassesTable:
    def __init__(self):
        self.table = {}
        self.tempGlobalVars = None

    def add(self,name,functionsTable,varsTable):
        currentClass = Class(functionsTable,varsTable)
        if name in self.table:
            return Error("Class already declared")
        else:
            self.table[name] = currentClass
            return None
    
    def search(self,name):
        if name in self.table:
            return self.table[name], None
        else:
            return None, Error("Class not declared")


    def toString(self):
        for key in self.table:
            print("###### Class ######")
            print(key, ":")
            print("### Vars Table ###")
            self.table[key].varsTable.toString()
            print("### Functions Table ###")
            self.table[key].functionsTable.toString()
