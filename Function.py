from VarsTable import VarsTable

class Function:
    def __init__(self, type,parameters,varsTable:VarsTable, variablesCount):
        self.type = type 
        self.parameters = parameters
        self.varsTable = varsTable
        # I, F, C, B, TI, TF, TC,TB
        self.variablesCount = variablesCount
        

