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

    def addQuadruple(self,operand,leftOperator,rightOperator,temporal):
        current_quadruple= Quadruple(operand,leftOperator,rightOperator,temporal)
        self.quadruples.append(current_quadruple)
        self.temporal +=1
        self.cont +=1

    def operatorsStackToString(self):
        print("prueba")
        for operator in self.operatorsStack:
            print(f"{operator}")

    def checkOperandPlusMinus(self):
        if self.operandsStack[-1] == '+' or self.operandsStack[-1] == '-':
            Roperand = self.operatorsStack.pop()
            LOperand = self.operatorsStack.pop()
            operator = operandsStack.pop()
            temporal = self.temporals
            addQuadruple(operand,LOperand,Roperand,temporal)

    def quadrupleListToString(self):
        for quad in self.quadrupleList:
            print(f"{quad.toString}")
