import linecache
import os
from VirtualMemory import VirtualMemory
from MemoryManager import MemoryManager

memoryManager = MemoryManager()
memoryManager.initGlobalMemory([10,10,10,10,10,10,10,10], "GLOBAL")
memoryManager.initConstantsMemory([10,10,10,10], "CONSTANTS")

constants_table = linecache.getline(os.getcwd() + "/ovejota.txt", 1 )
constants_table = constants_table.split(",")[:-1]
for value in constants_table:
   # value|address
    current_value = value.split("|")
    memoryManager.add(current_value[1], current_value[0])






offset = 1
i = 1 + offset
while True:

    txt_current_quad = linecache.getline(os.getcwd() + "/ovejota.txt", i )

    if txt_current_quad == "":
        exit()

    current_quad = txt_current_quad.split(",")
    current_quad[3] = current_quad[3][:-1]
    

    # print(current_quad)

    match current_quad[0]:
        case "WRITE":
            if current_quad[1][0] == '"' and current_quad[1][-1] == '"':
                print(current_quad[1])
            # Not a constant
            elif  int(current_quad[1])<18000:
                print(current_quad, memoryManager.get(memoryManager.get(current_quad[1])))
            # Constant
            elif int(current_quad[1])>=18000:
                print(current_quad, memoryManager.get(current_quad[1]))   
        case "=":
            memoryManager.add(current_quad[3], current_quad[1])
        case "+":
            # Not constant and constant
            if int(current_quad[1])<18000 and int(current_quad[2])>=18000:
                print("if 1", memoryManager.get(current_quad[1]))
            
                operandOne= memoryManager.get(memoryManager.get(current_quad[1]))
                operandTwo= memoryManager.get(current_quad[2])
                memoryManager.add(current_quad[3], int(operandOne)+ int(operandTwo))

            # Constant and not constant
            elif int(current_quad[1])>=18000 and int(current_quad[2])<18000:
                print("if 2")

                operandOne= memoryManager.get(current_quad[1])
                operandTwo= memoryManager.get(memoryManager.get(current_quad[2]))
                memoryManager.add(current_quad[3], int(operandOne)+ int(operandTwo))

            # Not a constant and Not a constant
            elif int(current_quad[1])<18000 and int(current_quad[2])<18000 :
                print("if 3")

                operandOne = memoryManager.get(memoryManager.get(current_quad[1]))
                operandTwo = memoryManager.get(memoryManager.get(current_quad[2]))
                memoryManager.add(current_quad[3], int(operandOne)+ int(operandTwo))

                 
            # Constant and constant
            elif int(current_quad[1])>=18000 and int(current_quad[2])>=18000:
                print("if 4")

                operandOne = memoryManager.get(current_quad[1])
                operandTwo = memoryManager.get(current_quad[2])
                print(current_quad[1], current_quad[2])
               
                memoryManager.add(current_quad[3], int(operandOne)+ int(operandTwo))
                





            

    
    #print(memoryManager.constants_memory.m_int)
    i+=1
