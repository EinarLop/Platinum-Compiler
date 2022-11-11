from SemanticCube import SemanticCube
from Quadruple import Quadruple
semanticCube = SemanticCube()

class QuadruplesList:
    def __init__(self):
        self.operatorsStack = []
        self.typesStack = []
        self.operandsStack = []
        self.jumpsStack = []
        self.quadruples = []
        self.cont = 1 #siempre al cuadruplo siguiente
        self.temporals = 1 #t1--tn

    #pop de cada pila
    #push de cada uno
    #checar tipos

    def addQuadruple(self,operator,leftOperand,rightOperand,temporal, typeTemp = "char"):
    # def addQuadruple(self,operator,leftOperand,rightOperand,temporal):
        current_quadruple= Quadruple(operator,leftOperand,rightOperand,temporal)
        self.quadruples.append(current_quadruple)
        if current_quadruple.operator != "=" :
            self.temporals +=1
            self.operandsStack.append(self.temporals-1) #mete el ultimo temporal

            self.typesStack.append(typeTemp)
        
            print(f"temporal {self.temporals-1} with type {typeTemp}")

        self.cont +=1

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
                self.addQuadruple(operator,LOperand,Roperand,temporal, typeTemp)
                
                


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
                self.addQuadruple(operator,LOperand,Roperand,temporal, typeTemp)

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
                self.addQuadruple(operator,result,ROperand,temporal, typeTemp)

                


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

                self.addQuadruple(operator,LOperand,ROperand,temporal, typeTemp)

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

                self.addQuadruple(operator,LOperand,ROperand,temporal, typeTemp)


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
        self.addQuadrupleCycles("=",Vcontrol,'',"VControl")

    def generateVFinalQuadruple(self):

        #primeramente se hace pop de tipos , si no es numero type-typemismatch
        #paso 1: expType=quadrupleList.typesStack.pop()
        # si no es numero typemismatch

        #else ----esto ya son los siguientes pasos
        exp = self.operandsStack.pop()
        self.addQuadrupleCycles("=",exp,'',"VFinal")

        self.addQuadrupleCycles("<","VControl","VFinal",self.temporals)
        self.jumpsStack.append(self.cont-1)
        self.addQuadrupleCycles("GotoF",self.temporals,'',None)
        self.jumpsStack.append(self.cont-1)
        self.temporals+=1


    def forChangeVC(self):
        self.addQuadrupleCycles("+","VControl",1,self.temporals)
        self.addQuadrupleCycles("=",self.temporals,'',"VControl")
        self.addQuadrupleCycles("=",self.temporals,'',self.operandsStack[-1])
        self.temporals+=1
        FIN = self.jumpsStack.pop()
        Retorno = self.jumpsStack.pop()
        self.addQuadrupleCycles("Goto",'','',Retorno)
        self.quadruples[FIN-1].temporal=Retorno
        self.operandsStack.pop()
        #popear el tipo tambien

    #######################toString#######################
    def quadrupleListToString(self):
        for quad in self.quadruples:
            if quad.toString() != None:
                print(f"{quad.toString()}")

    def operatorsStackToString(self):
        for operator in self.operatorsStack:
            print(f"{operator}")


    def operandsStackToString(self):
        for operand in self.operandsStack:
            print(f"{operand}")

    def jumpsStackToString(self):
        for operand in self.jumpsStack:
            print(f"{operand}")

    def typeStackToString(self):
        for type in self.typesStack:
            print(f"{type}")
