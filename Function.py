from VarsTable import VarsTable

class Function:
    def __init__(self, type,parameters,varsTable:VarsTable,quadrupleStart):
        self.type = type
        self.parameters = parameters
        self.varsTable = varsTable
        self.quadrupleStart = quadrupleStart
