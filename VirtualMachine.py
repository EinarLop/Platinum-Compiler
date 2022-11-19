import linecache
import os
from VirtualMemory import VirtualMemory
from MemoryManager import MemoryManager

memoryManager = MemoryManager()
memoryManager.initGlobalMemory([20,20,20,20,20,20,20,20], "GLOBAL")
memoryManager.initConstantsMemory([10,10,10,10], "CONSTANTS")

constants_table = linecache.getline(os.getcwd() + "/ovejota.txt", 1 )
constants_table = constants_table.split(",")[:-1]
for value in constants_table:
   # value|address
    current_value = value.split("|")
    memoryManager.add(current_value[1], current_value[0])

functions_table_dict = {}
functions_table =  linecache.getline(os.getcwd() + "/ovejota.txt", 2 )
functions_table = functions_table.split(",")[:-1]

for val in functions_table:
        val = val.split("|")
        name = val[0]
        quadrupleStart = val[1]
        size = val[2].split("%")
        parameters = val[3].split(";")[:-1]
        paramNames = []
        paramTypes = []
        for param in parameters:
                current = param.split("/")
                paramNames.append(current[0])
                paramTypes.append(current[1])

                
        functions_table_dict[name] = {
                'qs': quadrupleStart,
                'size': size,
                'paramNames': paramNames,
                'paramTypes': paramTypes
        }
        


def castType(operand):
    if str(operand).find(".") == -1:
        return int(operand)
    else:
        return float(operand)

returnFromFunctionStack = []

paramIntCounter = 0
paramFloatCounter = 0

offset = 2
i = 1 + offset
while True:

    txt_current_quad = linecache.getline(os.getcwd() + "/ovejota.txt", i )

    if txt_current_quad == "":
        exit()

    current_quad = txt_current_quad.split(",")
    current_quad[3] = current_quad[3][:-1]
    
    
    match current_quad[0]:
        case "WRITE":
            if current_quad[1][0] == '"' and current_quad[1][-1] == '"':
                print(current_quad[1])   
            else:
                print(memoryManager.get(current_quad[1]))
        case "=":
                # Added str() to fix arrays
                memoryManager.add(current_quad[3], str(memoryManager.get(current_quad[1])))
        case "+":
                operandOne = memoryManager.get(current_quad[1])
                operandTwo = memoryManager.get(current_quad[2])
                operandOne = castType(operandOne)
                operandTwo = castType(operandTwo)
                #print("inside", [operandOne,operandTwo,current_quad[3] ])
                
                memoryManager.add(current_quad[3], operandOne + operandTwo)
        case "-":
                operandOne = memoryManager.get(current_quad[1])
                operandTwo = memoryManager.get(current_quad[2])
                operandOne = castType(operandOne)
                operandTwo = castType(operandTwo)
                memoryManager.add(current_quad[3], operandOne - operandTwo)
        case "*":
                operandOne = memoryManager.get(current_quad[1])
                operandTwo = memoryManager.get(current_quad[2])
                operandOne = castType(operandOne)
                operandTwo = castType(operandTwo)
                memoryManager.add(current_quad[3], operandOne * operandTwo)

        case "/":
                operandOne = memoryManager.get(current_quad[1])
                operandTwo = memoryManager.get(current_quad[2])
                operandOne = castType(operandOne)
                operandTwo = castType(operandTwo)
                memoryManager.add(current_quad[3], operandOne / operandTwo)

        case "<":
                operandOne = memoryManager.get(current_quad[1])
                operandTwo = memoryManager.get(current_quad[2])
                operandOne = castType(operandOne)
                operandTwo = castType(operandTwo)
                memoryManager.add(current_quad[3], operandOne < operandTwo)
        case "goto":
                jumpToLine = int(current_quad[3])
                i = offset + jumpToLine - 1
        case "gotoF":
            if not memoryManager.get(current_quad[1]):
                jumpToLine = int(current_quad[3])
                i = offset + jumpToLine - 1
        
        case "goSub":
                returnFromFunctionStack.append(i+1)
                jumpToLine = int(current_quad[3])
                i = offset + jumpToLine - 1
                paramIntCounter = 0
                paramFloatCounter = 0
        case "ENDFUNC":
                memoryManager.destroyLocalMemory()
                i = returnFromFunctionStack.pop(-1) - 1
        case "ERA":
                memoryManager.initLocalMemory([10,10,10,10,10,10,10,10], "LOCAL")

        case "param":
                getParamValue = memoryManager.get(int(current_quad[1])) 

                if str(getParamValue).find(".") == -1:
                        memoryManager.add(10000+paramIntCounter, getParamValue)
                        paramIntCounter += 1
                else:
                        memoryManager.add(11000+paramFloatCounter, getParamValue)
                        paramFloatCounter += 1
        case "verify":
                
                value = int(memoryManager.get(int(current_quad[1])))
                lowerLimit = int(memoryManager.get(int(current_quad[2])))
                upperLimit =  int(memoryManager.get(int(current_quad[3])))
                if value < lowerLimit or value> upperLimit-1:
                        print(f"Index out of bounds, lower limit: {lowerLimit}, upper limit: {upperLimit-1}, index: {value}")
                        exit()
    i+=1
