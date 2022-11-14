class Program:
    def __init__(self, classesTable, varsTable, functionsTable):
        self.classesTable = classesTable
        self.varsTable = varsTable
        self.functionsTable = functionsTable
        self.variablesCount = [0,0,0,0,0,0,0,0]

        for func in functionsTable.table:
            self.variablesCount = [sum(x) for x in zip(self.variablesCount, functionsTable.table[func].variablesCount)]

        # for var in varsTable = 

    def toString(self):
        print("---------- Program ----------")
        self.classesTable.toString()
        print("----- Program Global VarsTable -----")
        self.varsTable.toString()
        print("----- Program FunctionsTable -----")
        self.functionsTable.toString()
        print("----- Program Variable Count -----")
        print(self.variablesCount)
