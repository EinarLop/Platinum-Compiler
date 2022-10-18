from SemanticCube import SemanticCube
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
