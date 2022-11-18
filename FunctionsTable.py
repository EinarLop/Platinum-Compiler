from Function import Function
from Error import Error
from VarsTable import VarsTable

class FunctionsTable:
    def __init__(self):
        self.table = {}

    def add(self,name,type,parameters,varsTable,quadrupleStart, tempTable=[]):
        if name in self.table:
            print(f"Function  {name} already declared")
            exit()
        
                        # I,F,C,B
        variablesCount = [0,0,0,0]
        for var in varsTable.table:
            if varsTable.table[var].type == "int":
                variablesCount[0]+=1
            elif varsTable.table[var].type == "float":
                variablesCount[1]+=1
            elif varsTable.table[var].type == "char":
                variablesCount[2]+=1
            elif varsTable.table[var].type == "bool":
                variablesCount[3]+=1

        for param in parameters:
            if param.type  == "int":
                variablesCount[0]+=1
            elif param.type  == "float":
                variablesCount[1]+=1
            elif param.type  == "char":
                variablesCount[2]+=1
            elif param.type  == "bool":
                variablesCount[3]+=1


        variablesCount =  variablesCount + tempTable

        currentFunction = Function(type,parameters,varsTable,quadrupleStart, variablesCount)

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
            print("### Quadruple of start ###")
            print(self.table[key].quadrupleStart)

            print("### Variable Count ###")
            print(self.table[key].variablesCount)
