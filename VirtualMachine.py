import linecache
import os
from VirtualMemory import VirtualMemory

global_memory = VirtualMemory([10,10,10,10,10,10,10,10])

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
            print(global_memory.get(current_quad[1]))
        case "=":
            global_memory.add(current_quad[3], current_quad[1])

    # print(global_memory.m_int)
    
    i+=1
   
