from Function import Function
from Error import Error
from VarsTable import VarsTable

class FunctionsTable:
    def __init__(self):
        self.table = {}

    def add(self,name,type,parameters,varsTable):
        currentFunction = Function(type,parameters,varsTable)

        if name in self.table:
            return Error("Function already declared")
        else:
            self.table[name] = currentFunction
            return None

    def search(self,name):
        if name in self.table:
            return self.table[name], None
        else:
            return None, Error("Function not declared")

    def toString(self):
        for key in self.table:
            print("###### Function ######")
            print(f"{key}: {self.table[key].type}")
            print("### Parameters ###")
            for parameter in self.table[key].parameters:
                print(f"{parameter.id}:  {parameter.type}")
            print("### Vars Table ###")
            self.table[key].varsTable.toString()
