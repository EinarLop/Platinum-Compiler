from SemanticCube import SemanticCube
from Quadruple import Quadruple
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


    def addQuadruple(self,operator,leftOperand,rightOperand,temporal):
        current_quadruple= Quadruple(operator,leftOperand,rightOperand,temporal)
        self.quadruples.append(current_quadruple)
        if current_quadruple.operator is not "=" :
            self.temporals +=1
            self.operandsStack.append(self.temporals-1) #mete el ultimo temporal
        self.cont +=1

    #if else
    def addQuadrupleCondition(self,operator,leftOperand,rightOperand,temporal):
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
                self.addQuadruple(operator,LOperand,Roperand,temporal)


    def checkOperatorTimesDivide(self):
        if len(self.operatorsStack) != 0:
            if self.operatorsStack[-1] == "*" or self.operatorsStack[-1] == "/":
                Roperand = self.operandsStack.pop()
                LOperand = self.operandsStack.pop()
                operator = self.operatorsStack.pop()
                temporal = self.temporals
                self.addQuadruple(operator,LOperand,Roperand,temporal)

    def makeAssignationResult(self):
        if len(self.operatorsStack) != 0:
            if self.operatorsStack[-1] == "=":
                result = self.operandsStack.pop()
                LOperand = ''
                operator = self.operatorsStack.pop()
                temporal = self.operandsStack.pop()
                self.addQuadruple(operator,LOperand,result,temporal)


    def generate_sExp_quad(self,leftOperator):
        listOperandsSexp = ["<",">","<=",">=","<>"]
        if len(self.operatorsStack) != 0:
            if self.operatorsStack[-1] in listOperandsSexp:
                ROperand = self.operandsStack.pop()
                LOperand = leftOperator
                operator = self.operatorsStack.pop()
                temporal = self.temporals
                self.addQuadruple(operator,LOperand,ROperand,temporal)

    def generate_hExp_quad(self,leftOperator):
        listOperandsHexp = ["&&","||"]
        if len(self.operatorsStack) != 0:
            if self.operatorsStack[-1] in listOperandsHexp:
                ROperand = self.operandsStack.pop()
                LOperand = leftOperator
                operator = self.operatorsStack.pop()
                temporal = self.temporals
                self.addQuadruple(operator,LOperand,ROperand,temporal)
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
    #######################toString#######################
    def quadrupleListToString(self):
        for quad in self.quadruples:
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
