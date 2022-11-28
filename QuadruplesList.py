from SemanticCube import SemanticCube
from Quadruple import Quadruple
semanticCube = SemanticCube()

class QuadruplesList:
    def __init__(self):
        #creacion de todas las pilas necesarias para la manipulacion de cuadruplos
        self.operatorsStack = []
        self.typesStack = []
        self.operandsStack = []
        self.dimensionalOperandsStack = []
        self.jumpsStack = []
        self.quadruples = []

        #pila de variables controladas y variables finales, es decir para el ciclo for
        self.controlledVar=[]
        self.finalVars=[]

        self.endFuncQuads = []
        self.cont = 1 #siempre al cuadruplo siguiente
        self.temporals = 1 #t1--tn

        #contador de temporales para cuadruplos
        self.counter_tInt = 0
        self.counter_tFloat = 0
        self.counter_tChar = 0
        self.counter_tBool = 0
        self.counter_tPointer = 0

        self.scope = "LOCAL"

        #temporales globales con sus rangos para aumentar la direccion base a los contadores
        if self.scope == "GLOBAL":
            self.TI = [5000,5999]
            self.TF = [6000,6999]
            self.TC = [7000,7999]
            self.TB = [8000,8999]
            self.TP = [30000,30999]


        #temporales locales con sus rangos para aumentar la direccion base a los contadores
        elif self.scope == "LOCAL":
            self.TI = [14000, 14999]
            self.TF = [15000, 15999]
            self.TC = [16000, 16999]
            self.TB = [17000, 17999]
            self.TP = [31000,31999]

    #generar cuadruplo gotoMain
    def generateGoToMainQuad(self):
        current_quadruple= Quadruple('goto','','',None)
        self.quadruples.append(current_quadruple)
        self.jumpsStack.append(self.cont)
        self.cont +=1
    #rellena el cuadruplo gotoMain poppeando de la pila de saltos
    def fillGoToMainQuad(self):
        self.quadruples[self.jumpsStack.pop()-1].temporal=self.cont
    #añade un nuevo cuadruplo y esta es la adición mas general, ya que tiene temporal y dependiendo del tipo de temporal se asigna de acuerdo a la dirBase y a los contadores
    def addQuadruple(self,operator,leftOperand,rightOperand,temporal, typeTemp):
        current_temp_memory_address = 0 #si no es una asignacion tiene un temporal nuevo asi que se debe checar el tipo y asignar temporaless
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
        elif typeTemp == "pointer":
            if operator != "=" :
                current_temp_memory_address =  self.TP[0] + self.counter_tPointer
                self.counter_tPointer+=1
        if temporal < 1000:
                current_quadruple= Quadruple(operator,leftOperand,rightOperand, current_temp_memory_address )
        else:
            current_quadruple= Quadruple(operator,leftOperand,rightOperand,temporal)

        #se mete el cuadruplo generado a la pila de operadores
        self.quadruples.append(current_quadruple)
        if current_quadruple.operator != "=" :
            #si no es una asignación se pushea el temporal y su tipos
            self.temporals +=1
            self.operandsStack.append(current_temp_memory_address)
            self.typesStack.append(typeTemp)

        #se aumenta el numero de cuadruplos que hay
        self.cont +=1
        if current_quadruple.operator != "=" :
            return typeTemp

    #if else con el cual solo se aumenta el contador de cuadruplos y se añade a la pila de cuadruplos
    def addQuadrupleCondition(self,operator,leftOperand,rightOperand,temporal):
        current_quadruple= Quadruple(operator,leftOperand,rightOperand,temporal)
        self.quadruples.append(current_quadruple)
        self.cont +=1

    #readWrite con el cual solo se aumenta el contador de cuadruplos y se añade a la pila de cuadruplos
    def addQuadrupleReadWrite(self,operator,leftOperand,rightOperand,temporal):
        current_quadruple= Quadruple(operator,leftOperand,rightOperand,temporal)
        self.quadruples.append(current_quadruple)
        self.cont +=1
    #añade cuadruplo para ciclos while goto y gotof y for y se añade a la pila de cuadruplos y aumenta contador
    def addQuadrupleCycles(self,operator,leftOperand,rightOperand,temporal):
        current_quadruple= Quadruple(operator,leftOperand,rightOperand,temporal)
        self.quadruples.append(current_quadruple)
        self.cont +=1
    #genera cuadruplo ENDFUNC con el cual solo se aumenta el contador de cuadruplos y se añade a la pila de cuadruplos
    # y tambien se añade el contador de cuadruplo para saber en que cuadruplo termina
    def addQuadrupleEndFuncModule(self):
        current_quadruple= Quadruple('ENDFUNC','','','')
        self.quadruples.append(current_quadruple)
        self.endFuncQuads.append(self.cont)
        self.cont +=1
    #genera cuadruplo ERA  con el cual solo se aumenta el contador de cuadruplos y se añade a la pila de cuadruplos
    def addQuadrupleERAFuncCall(self,funcName):
        current_quadruple= Quadruple('ERA',funcName,'','')
        self.quadruples.append(current_quadruple)
        self.cont +=1
    #genera cuadruplo goSUB con el cual solo se aumenta el contador de cuadruplos y se añade a la pila de cuadruplos
    def addQuadrupleGoSubFuncCall(self,funcName,initialQuad):
        current_quadruple= Quadruple('goSub',funcName,'',initialQuad)
        self.quadruples.append(current_quadruple)
        self.cont +=1
    #genera cuadruplo param con el cual solo se aumenta el contador de cuadruplos y se añade a la pila de cuadruplos
    def addQuadrupleParamFuncCall(self,paramName,paramNumber):
        current_quadruple= Quadruple('param',paramName,'',paramNumber)
        self.quadruples.append(current_quadruple)
        self.cont +=1
    #genera cuadruplo verify con el cual solo se aumenta el contador de cuadruplos y se añade a la pila de cuadruplos
    def addQuadrupleVerifyArray(self,exp,LIdim,LSdim):
        current_quadruple= Quadruple('verify',exp,LIdim,LSdim)
        self.quadruples.append(current_quadruple)
        self.cont +=1


    #checa si el tope de la pila de operandos es + o - para resolver
    #hace pop de pila de operadores para el izq y derecho, junto con sus tipos
    #se hace pop de la pila de operandos para saber cual de los 2 simbolos es
    def checkOperatorPlusMinus(self):
        if len(self.operatorsStack) != 0:
            if self.operatorsStack[-1] == "+" or self.operatorsStack[-1] == "-":
                Roperand = self.operandsStack.pop()
                LOperand = self.operandsStack.pop()
                operator = self.operatorsStack.pop()
                temporal = self.temporals

                RType = self.typesStack.pop()
                LType = self.typesStack.pop()
                typeTemp, err = semanticCube.semantic(RType, LType, operator) #cubo semantico para saber si el "baila mija con el señor"
                if err != None:
                    print(f"Type miss match between in plus/minus {LOperand} ({LType}) and {Roperand} ({RType})")
                    exit()
                return self.addQuadruple(operator,LOperand,Roperand,temporal, typeTemp)



    #checa si el tope de la pila de operandos es * o / para resolver
    #hace pop de pila de operadores para el izq y derecho, junto con sus tipos
    #se hace pop de la pila de operandos para saber cual de los 2 simbolos es
    def checkOperatorTimesDivide(self):
        if len(self.operatorsStack) != 0:
            if self.operatorsStack[-1] == "*" or self.operatorsStack[-1] == "/":
                Roperand = self.operandsStack.pop()
                LOperand = self.operandsStack.pop()
                operator = self.operatorsStack.pop()
                temporal = self.temporals

                RType = self.typesStack.pop()
                LType = self.typesStack.pop()
                typeTemp, err = semanticCube.semantic(RType, LType, operator) #"¿baila mija con el señor?"
                if err != None:
                    print(f"Type miss match between {LOperand} ({LType}) and {Roperand} ({RType})")
                    exit()

                return self.addQuadruple(operator,LOperand,Roperand,temporal, typeTemp)
    #checa si el tope de la pila de operandos es = para resolver
    #hace pop de pila de operadores para el izq y derecho, junto con sus tipos para saber a cual se le asigna a cual
    #se hace pop de la pila de operandos para sacar el =
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


                return self.addQuadruple(operator,result,ROperand,temporal, typeTemp)



    #checa si el tope de la pila de operandos es alguno de los operadores de s_exp para resolver
    #hace pop de pila de operadores para el izq y derecho, junto con sus tipos para si se pueden combinar en una exp
    #se hace pop de la pila de operandos para sacar el operador correspondiente
    def generate_sExp_quad(self,leftOperator):
        listOperandsSexp = ["<",">","<=",">=","<>","=="]
        if len(self.operatorsStack) != 0:
            if self.operatorsStack[-1] in listOperandsSexp:
                ROperand = self.operandsStack.pop()
                LOperand = leftOperator
                operator = self.operatorsStack.pop()
                temporal = self.temporals

                RType = self.typesStack.pop()
                LType = self.typesStack.pop()

                typeTemp, err = semanticCube.semantic(RType, LType, operator) #"¿baila mija con el señor?"
                if err != None:
                    print(f"Type miss match between {LOperand} ({LType}) and {ROperand} ({RType})")
                    exit()

                return self.addQuadruple(operator,LOperand,ROperand,temporal, typeTemp)


    #checa si el tope de la pila de operandos es alguno de los operadores de h_exp para resolver
    #hace pop de pila de operadores para el izq y derecho, junto con sus tipos para si se pueden combinar en una exp
    #se hace pop de la pila de operandos para sacar el operador correspondiente
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

                typeTemp, err = semanticCube.semantic(RType, LType, operator) #¿baila mija con el señor?
                if err != None:
                    print(f"Type miss match between {LOperand} ({LType}) and {ROperand} ({RType})")
                    exit()

                return self.addQuadruple(operator,LOperand,ROperand,temporal, typeTemp)


    #######################fondo falso#######################
    #elimina el fondo falso haciendo pop de pila de operadores para sacar el (
    def eliminateFakeVoid(self):
        self.operatorsStack.pop()

    ######################condition##########################
    #genera gotoF, si no es de tipo bool entonces no se puede evaluar el condicional
    def generateGoToFCondition(self):
        if self.typesStack.pop() != "bool":
            print(f"Conditional not bool")
            exit()
        condition = self.operandsStack.pop() #hacer pop de pila de operadores para saber que se va a evaluar
        self.addQuadrupleCondition("gotoF",condition,'',None)
        self.jumpsStack.append(self.cont-1) #pushear a pila de saltos para despues volver a rellenar
    #rellenar gotoF haciendo pop de la pila de saltos
    def fillgotoF_IF(self):
        self.quadruples[self.jumpsStack.pop()-1].temporal=self.cont

    #generar goto y meter en pila de saltos y rellenar gotoF ya que esto viene si hay un else
    def generateGoToCondition(self):
        false = self.jumpsStack.pop()
        self.addQuadrupleCondition("goto",'','',None)
        self.jumpsStack.append(self.cont-1)
        self.quadruples[false-1].temporal=self.cont

    ######################while##########################
    #genera gotoF de while
    def generateGoToFWhile(self):
        condition = self.operandsStack.pop()
        #tipos
        self.addQuadrupleCycles("gotoF",condition,'',None)
        self.jumpsStack.append(self.cont-1) #pushear a pila de saltos para despues volver a rellenar

    #generar goto y rellenar gotoF ya que de aqui seguiria el cuadruplo fuera del while y hacemos doble pop en pila de saltos
    #uno para rellenar el gotoF con cont y retorno para saber a que cuadruplo regresar para volver a evaluar exp de while
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
        expType=self.typesStack.pop()
        if expType != "int" and expType != "float":
            print(f"Variable {expType} not numeric, type mistmatch in first EXP in for cycle")
            exit()
        else:
        #else ----esto ya son los siguientes pasos
            exp = self.operandsStack.pop()
            Vcontrol = self.operandsStack[-1]
            controlType= self.typesStack[-1]
            current_temp_memory_address = 0
            #tipos con semantica
            # ver si se puede asignar el tipo del id a asignar y la exp que se le quiere asignar
            typeTemp, err = semanticCube.semantic(expType, controlType, "=")
            if err != None:
                print(f"Type miss match between for assignation")
                exit()
            #crear cuadruplo para asignar a la que sera variable de control
            quad=Quadruple("=",exp,'',Vcontrol)
            self.quadruples.append(quad)
            self.cont+=1
            #checar su tipo para saber que temporal usar con direccion base
            if expType  == "int":
                    current_temp_memory_address =  self.TI[0] + self.counter_tInt
                    self.counter_tInt+=1
            elif expType  == "float":
                    current_temp_memory_address =  self.TF[0] + self.counter_tFloat
                    self.counter_tFloat+=1
            #agregar la variable de control a un temporal para saber cual es y poder acceder a ella
            quad=Quadruple("=",Vcontrol,'',current_temp_memory_address)
            self.quadruples.append(quad)
            self.cont+=1
            # y para poder acceder a la variabel de control se coloca en una pila de variables controladas
            self.controlledVar.append(self.quadruples[-1].temporal)

    def generateVFinalQuadruple(self):

        #primeramente se hace pop de tipos , si no es numero type-typemismatch
        #paso 1: expType=quadrupleList.typesStack.pop()
        # si no es numero typemismatch

        expType=self.typesStack.pop()
        current_temp_memory_address = 0
        if expType != "int" and expType != "float":
            print(f"Variable {expType} not numeric, type mistmatch in first EXP in for cycle")
            exit()
        else:
            exp = self.operandsStack.pop()
            if expType  == "int":
                    current_temp_memory_address =  self.TI[0] + self.counter_tInt
                    self.counter_tInt+=1
            elif expType  == "float":
                    current_temp_memory_address =  self.TF[0] + self.counter_tFloat
                    self.counter_tFloat+=1
            self.addQuadrupleCycles("=",exp,'',current_temp_memory_address)
            self.finalVars.append(current_temp_memory_address)

            current_temp_memory_address =  self.TB[0] + self.counter_tBool
            self.counter_tBool+=1

            self.addQuadrupleCycles("<",self.controlledVar[-1],self.finalVars[-1],current_temp_memory_address)
            self.jumpsStack.append(self.cont-1)
            self.addQuadrupleCycles("gotoF",current_temp_memory_address,'',None)
            self.jumpsStack.append(self.cont-1)

    #cambios de la variable de control de for
    def forChangeVC(self,oneConstant):
        current_temp_memory_address= 0

        if self.typesStack[-1]  == "int":
                current_temp_memory_address =  self.TI[0] + self.counter_tInt
                self.counter_tInt+=1
        elif self.typesStack[-1]  == "float":
                current_temp_memory_address =  self.TF[0] + self.counter_tFloat
                self.counter_tFloat+=1
        #despues de checar el tipo de variable que es la variable de control se le suma uno para que siga el ciclo for y dejarlo en el temporal correcto
        self.addQuadrupleCycles("+",self.controlledVar[-1],oneConstant,current_temp_memory_address)
        #despues iguala dicho resultado del temporal a la variable de control para que se cumpla que vaya sumando de 1 en 1
        self.addQuadrupleCycles("=",current_temp_memory_address,'',self.controlledVar[-1])
        self.addQuadrupleCycles("=",current_temp_memory_address,'',self.operandsStack[-1])
        #hace pop en pila de saltos 2 veces, el primero para rellenar gotoF afuera del ciclo y el siguiente es para saber el cuadruplo que hay que regresar generando un goTo
        FIN = self.jumpsStack.pop()
        Retorno = self.jumpsStack.pop()
        self.addQuadrupleCycles("goto",'','',Retorno)
        self.quadruples[FIN-1].temporal=self.cont
        self.operandsStack.pop()
        self.controlledVar.pop()
        self.finalVars.pop()
        self.typesStack.pop()

    #######################funciones#######################
    #generar cuadruplo ENDFUNC
    def generateEndFuncModule(self):
        self.addQuadrupleEndFuncModule()

    #generar cuadruplo ERA con el nombre de la funcion
    def generateERAFuncCall(self,funcName):
        self.addQuadrupleERAFuncCall(funcName)
    #generar cuadruplo goSub con el nombre de la funcion y su cuaddruplo inicial
    def generateGoSubFuncCall(self,funcName,initialQuad):
        self.addQuadrupleGoSubFuncCall(funcName,initialQuad)
    #generar cuadruplo de RETURN
    def generateFuncReturnQuad(self,funcName):
        operator="Ret"
        exp=self.operandsStack.pop()
        type=self.typesStack.pop()
        self.addQuadruple(operator,funcName,'',exp, type)

    # cuadruplo para generar igualación de variable de retorno a un temporal para poder usar en operaciones futuras
    def assignGlobalFuncCall(self,varGlobal,typeVar):
        current_temp_address = 0
        if typeVar  == "int":
                current_temp_memory_address =  self.TI[0] + self.counter_tInt
                self.counter_tInt+=1
        elif typeVar  == "float":
                current_temp_memory_address =  self.TF[0] + self.counter_tFloat
                self.counter_tFloat+=1
        elif typeVar  == "char":
                current_temp_memory_address =  self.TC[0] + self.counter_tChar
                self.counter_tChar+=1
        elif typeVar  == "bool":
                current_temp_memory_address =  self.TB[0] + self.counter_tBool
                self.counter_tBool+=1
        elif typeVar == "pointer":
                current_temp_memory_address =  self.TP[0] + self.counter_tPointer
                self.counter_tPointer+=1
        quad=Quadruple("=",varGlobal,'',current_temp_memory_address)
        self.quadruples.append(quad)

        self.operandsStack.append(self.quadruples[-1].temporal)
        self.cont+=1
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
    #reinicio de temporales que se llama despues del fin de la funcion
    def resetTemporalsCounter(self):
            self.counter_tInt = 0
            self.counter_tFloat = 0
            self.counter_tChar = 0
            self.counter_tBool = 0
    #cambio de scope locales de temporales a globales 
    def changeScope(self):
            self.TI = [5000,5999]
            self.TF = [6000,6999]
            self.TC = [7000,7999]
            self.TB = [8000,8999]
            self.TP = [30000,30999]
