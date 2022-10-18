class Program:
    def __init__(self, classesTable, varsTable, functionsTable):
        self.classesTable = classesTable
        self.varsTable = varsTable
        self.functionsTable = functionsTable

    def toString(self):
        print("---------- Program ----------")
        self.classesTable.toString()
        print("----- Program VarsTable -----")
        self.varsTable.toString()
        print("----- Program FunctionsTable -----")
        self.functionsTable.toString()


        