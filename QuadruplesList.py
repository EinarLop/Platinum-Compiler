from SemanticCube import SemanticCube
from Quadruple import Quadruple
semanticCube = SemanticCube()







class QuadruplesList:
    def __init__(self):
        self.operatorsStack = []
        self.typesStack = []
        self.operandsStack = []
        self.dimensionalOperandsStack = []
        self.jumpsStack = []
        self.quadruples = []

        self.controlledVar=[]
        self.finalVars=[]

        self.endFuncQuads = []
        self.cont = 1 #siempre al cuadruplo siguiente
        self.temporals = 1 #t1--tn

        self.counter_tInt = 0
        self.counter_tFloat = 0
        self.counter_tChar = 0
        self.counter_tBool = 0

        self.scope = "LOCAL"

        if self.scope == "GLOBAL":
            self.TI = [5000,5999]
            self.TF = [6000,6999]
            self.TC = [7000,7999]
            self.TB = [8000,8999]

        elif self.scope == "LOCAL":
            self.TI = [14000, 14999]
            self.TF = [15000, 15999]
            self.TC = [16000, 16999]
            self.TB = [17000, 17999]

    #pop de cada pila
    #push de cada uno
    #checar tipos


    def generateGoToMainQuad(self):
        current_quadruple= Quadruple('goto','','',None)
        self.quadruples.append(current_quadruple)
        self.jumpsStack.append(self.cont)
        self.cont +=1

    def fillGoToMainQuad(self):
        self.quadruples[self.jumpsStack.pop()-1].temporal=self.cont

    def addQuadruple(self,operator,leftOperand,rightOperand,temporal, typeTemp):
    # def addQuadruple(self,operator,leftOperand,rightOperand,temporal):
        #print(typeTemp)
        current_temp_memory_address = 0
        if typeTemp  == "int":
            if operator != "=" :
                current_temp_memory_address =  self.TI[0] + self.counter_tInt
                self.counter_tInt+=1
        elif typeTemp  == "float":
            if operator != "=" :
                current_temp_memory_address =  self.TF[0] + self.counter_tFloat
                self.counter_tFloat+=1
        elif typeTemp  == "char":
            if operator != "=" :
                current_temp_memory_address =  self.TC[0] + self.counter_tChar
                self.counter_tChar+=1
        elif typeTemp  == "bool":
            if operator != "=" :
                current_temp_memory_address =  self.TB[0] + self.counter_tBool
                self.counter_tBool+=1

        if temporal < 1000:
                #current_quadruple= Quadruple(operator,leftOperand,rightOperand,"t"+str(temporal)+typeTemp)
                current_quadruple= Quadruple(operator,leftOperand,rightOperand, current_temp_memory_address )
        else:
            current_quadruple= Quadruple(operator,leftOperand,rightOperand,temporal)
            #current_quadruple= Quadruple(operator,leftOperand,rightOperand,current_temp_memory_address)

        self.quadruples.append(current_quadruple)
        if current_quadruple.operator != "=" :

            self.temporals +=1
            #self.operandsStack.append("t"+str(self.temporals-1)) #mete el ultimo temporal
            self.operandsStack.append(current_temp_memory_address)
            self.typesStack.append(typeTemp)

            # print(f"temporal {self.temporals-1} with type {typeTemp}")


        self.cont +=1
        if current_quadruple.operator != "=" :
            return typeTemp

    #if else
    def addQuadrupleCondition(self,operator,leftOperand,rightOperand,temporal):
        current_quadruple= Quadruple(operator,leftOperand,rightOperand,temporal)
        self.quadruples.append(current_quadruple)
        self.cont +=1

    #readWrite
    def addQuadrupleReadWrite(self,operator,leftOperand,rightOperand,temporal):
        current_quadruple= Quadruple(operator,leftOperand,rightOperand,temporal)
        self.quadruples.append(current_quadruple)
        self.cont +=1
    #añade cuadruplo para ciclos while goto y gotof y seguramente tambien for
    def addQuadrupleCycles(self,operator,leftOperand,rightOperand,temporal):
        current_quadruple= Quadruple(operator,leftOperand,rightOperand,temporal)
        self.quadruples.append(current_quadruple)
        self.cont +=1

    def addQuadrupleEndFuncModule(self):
        current_quadruple= Quadruple('ENDFUNC','','','')
        self.quadruples.append(current_quadruple)
        self.endFuncQuads.append(self.cont)
        self.cont +=1

    def addQuadrupleERAFuncCall(self,funcName):
        current_quadruple= Quadruple('ERA',funcName,'','')
        self.quadruples.append(current_quadruple)
        self.cont +=1

    def addQuadrupleGoSubFuncCall(self,funcName,initialQuad):
        current_quadruple= Quadruple('goSub',funcName,'',initialQuad)
        self.quadruples.append(current_quadruple)
        self.cont +=1
    def addQuadrupleParamFuncCall(self,paramName,paramNumber):
        current_quadruple= Quadruple('param',paramName,'',paramNumber)
        self.quadruples.append(current_quadruple)
        self.cont +=1

    def addQuadrupleVerifyArray(self,exp,LIdim,LSdim):
        current_quadruple= Quadruple('verify',exp,LIdim,LSdim)
        self.quadruples.append(current_quadruple)
        self.cont +=1



    def checkOperatorPlusMinus(self):
        if len(self.operatorsStack) != 0:
            if self.operatorsStack[-1] == "+" or self.operatorsStack[-1] == "-":
                Roperand = self.operandsStack.pop()
                LOperand = self.operandsStack.pop()
                operator = self.operatorsStack.pop()
                temporal = self.temporals

                RType = self.typesStack.pop()
                LType = self.typesStack.pop()
                typeTemp, err = semanticCube.semantic(RType, LType, operator)
                if err != None:
                    print(f"Type miss match between {LOperand} ({LType}) and {Roperand} ({RType})")
                    exit()
                return self.addQuadruple(operator,LOperand,Roperand,temporal, typeTemp)




    def checkOperatorTimesDivide(self):
        if len(self.operatorsStack) != 0:
            if self.operatorsStack[-1] == "*" or self.operatorsStack[-1] == "/":
                Roperand = self.operandsStack.pop()
                LOperand = self.operandsStack.pop()
                operator = self.operatorsStack.pop()
                temporal = self.temporals

                RType = self.typesStack.pop()
                LType = self.typesStack.pop()
                typeTemp, err = semanticCube.semantic(RType, LType, operator)
                if err != None:
                    print(f"Type miss match between {LOperand} ({LType}) and {Roperand} ({RType})")
                    exit()
                #print(f"{LOperand} ({LType}) and {Roperand} ({RType})")
                return self.addQuadruple(operator,LOperand,Roperand,temporal, typeTemp)

    def makeAssignationResult(self):
        if len(self.operatorsStack) != 0:
            if self.operatorsStack[-1] == "=":
                result = self.operandsStack.pop()
                ROperand = ''
                operator = self.operatorsStack.pop()
                temporal = self.operandsStack.pop()
                RType = self.typesStack.pop()
                LType = self.typesStack.pop()
                typeTemp, err = semanticCube.semantic(RType, LType, operator)

                if err != None:
                    print(f"Type miss match between {temporal} ({LType}) and {result} ({RType})")
                    exit()
                #print(f"popopopo{temporal} ({LType}) and {result} ({RType})")

                return self.addQuadruple(operator,result,ROperand,temporal, typeTemp)




    def generate_sExp_quad(self,leftOperator):
        listOperandsSexp = ["<",">","<=",">=","<>"]
        if len(self.operatorsStack) != 0:
            if self.operatorsStack[-1] in listOperandsSexp:
                ROperand = self.operandsStack.pop()
                LOperand = leftOperator
                operator = self.operatorsStack.pop()
                temporal = self.temporals

                RType = self.typesStack.pop()
                LType = self.typesStack.pop()

                typeTemp, err = semanticCube.semantic(RType, LType, operator)
                if err != None:
                    print(f"Type miss match between {LOperand} ({LType}) and {ROperand} ({RType})")
                    exit()

                return self.addQuadruple(operator,LOperand,ROperand,temporal, typeTemp)

    def generate_hExp_quad(self,leftOperator):
        listOperandsHexp = ["&&","||"]
        if len(self.operatorsStack) != 0:
            if self.operatorsStack[-1] in listOperandsHexp:
                ROperand = self.operandsStack.pop()
                LOperand = leftOperator
                operator = self.operatorsStack.pop()
                temporal = self.temporals
                RType = self.typesStack.pop()
                LType = self.typesStack.pop()

                typeTemp, err = semanticCube.semantic(RType, LType, operator)
                if err != None:
                    print(f"Type miss match between {LOperand} ({LType}) and {ROperand} ({RType})")
                    exit()

                return self.addQuadruple(operator,LOperand,ROperand,temporal, typeTemp)


    #######################fondo falso#######################
    def eliminateFakeVoid(self):
        self.operatorsStack.pop()

    ######################condition##########################
    def generateGoToFCondition(self):
        condition = self.operandsStack.pop()
        self.addQuadrupleCondition("gotoF",condition,'',None)
        self.jumpsStack.append(self.cont-1)

    def fillgotoF_IF(self):
        self.quadruples[self.jumpsStack.pop()-1].temporal=self.cont


    def generateGoToCondition(self):
        false = self.jumpsStack.pop()
        self.addQuadrupleCondition("goto",'','',None)
        self.jumpsStack.append(self.cont-1)
        self.quadruples[false-1].temporal=self.cont

    ######################while##########################
    def generateGoToFWhile(self):
        condition = self.operandsStack.pop()
        #tipos
        self.addQuadrupleCycles("gotoF",condition,'',None)
        self.jumpsStack.append(self.cont-1)

    def generateGoToWhile(self):
        false = self.jumpsStack.pop()
        retorno = self.jumpsStack.pop()
        self.addQuadrupleCycles("goto",'','',retorno)
        self.quadruples[false-1].temporal=self.cont

    ######################FOR##########################
    def generateVControlQuadruple(self):

        #primeramente se hace pop de tipos , si no es numero type-typemismatch
        #paso 1: expType=quadrupleList.typesStack.pop()
        # si no es numero typemismatch

        #else ----esto ya son los siguientes pasos
        exp = self.operandsStack.pop()
        Vcontrol = self.operandsStack[-1]
        #tipos con semantica
        self.addQuadrupleCycles("=",exp,'',Vcontrol)
        self.addQuadrupleCycles("=",Vcontrol,'',self.temporals)
        self.controlledVar.append(self.temporals)
        self.temporals+=1

    def generateVFinalQuadruple(self):

        #primeramente se hace pop de tipos , si no es numero type-typemismatch
        #paso 1: expType=quadrupleList.typesStack.pop()
        # si no es numero typemismatch

        #else ----esto ya son los siguientes pasos
        exp = self.operandsStack.pop()
        self.addQuadrupleCycles("=",exp,'',self.temporals)
        self.finalVars.append(self.temporals)
        self.temporals+=1


        self.addQuadrupleCycles("<",self.controlledVar[-1],self.finalVars[-1],self.temporals)
        self.jumpsStack.append(self.cont-1)
        self.addQuadrupleCycles("GotoF",self.temporals,'',None)
        self.jumpsStack.append(self.cont-1)
        self.temporals+=1


    def forChangeVC(self):
        self.addQuadrupleCycles("+",self.controlledVar[-1],1,self.temporals)
        self.addQuadrupleCycles("=",self.temporals,'',self.controlledVar[-1])
        self.addQuadrupleCycles("=",self.temporals,'',self.operandsStack[-1])
        self.temporals+=1
        FIN = self.jumpsStack.pop()
        Retorno = self.jumpsStack.pop()
        self.addQuadrupleCycles("Goto",'','',Retorno)
        self.quadruples[FIN-1].temporal=self.cont
        self.operandsStack.pop()
        self.controlledVar.pop()
        self.finalVars.pop()
        #popear el tipo tambien

    #######################funciones#######################
    def generateEndFuncModule(self):
        self.addQuadrupleEndFuncModule()

    def generateERAFuncCall(self,funcName):
        self.addQuadrupleERAFuncCall(funcName)

    def generateGoSubFuncCall(self,funcName,initialQuad):
        self.addQuadrupleGoSubFuncCall(funcName,initialQuad)

    #######################Arrays#######################

    #######################toString#######################
    def quadrupleListToString(self):
        f = open("ovejota.txt","a+")
        for quad in self.quadruples:
            f.write(f"{quad.toString()}\n")
        f.close()
    def operatorsStackToString(self):
        for operator in self.operatorsStack:
            print(f"{operator}")


    def operandsStackToString(self):
        cont = 0
        for operand in self.operandsStack:
            cont+=1
            print(f"{operand}")

    def jumpsStackToString(self):
        for operand in self.jumpsStack:
            print(f"{operand}")

    def typeStackToString(self):
        for type in self.typesStack:
            print(f"{type}")
###################### Temporals management ######################
    def resetTemporalsCounter(self):
            self.counter_tInt = 0
            self.counter_tFloat = 0
            self.counter_tChar = 0
            self.counter_tBool = 0

    def changeScope(self):
            self.TI = [5000,5999]
            self.TF = [6000,6999]
            self.TC = [7000,7999]
            self.TB = [8000,8999]
