import linecache
import os
from VirtualMemory import VirtualMemory
from MemoryManager import MemoryManager

memoryManager = MemoryManager()
memoryManager.initGlobalMemory([10,10,10,10,10,10,10,10], "GLOBAL")
memoryManager.initConstantsMemory([10,10,10,10], "CONSTANTS")


i = 1
while True:

    txt_current_quad = linecache.getline(os.getcwd() + "/ovejota.txt", i )

    if txt_current_quad == "":
        exit()

    current_quad = txt_current_quad.split(",")
    current_quad[3] = current_quad[3][:-1]

    # print(current_quad)

    match current_quad[0]:
        case "WRITE":
            print(memoryManager.get(current_quad[1]))
        case "=":
            memoryManager.add(current_quad[3], current_quad[1])
            

    # print(global_memory.m_int)

    i+=1
