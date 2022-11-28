#clase de objeto de funcion
from VarsTable import VarsTable

class Function:
    def __init__(self, type,parameters,varsTable:VarsTable,quadrupleStart,variablesCount):
        self.type = type
        self.parameters = parameters
        self.varsTable = varsTable
        self.quadrupleStart = quadrupleStart
        self.variablesCount = variablesCount
