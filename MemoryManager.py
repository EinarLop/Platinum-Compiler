from VirtualMemory import VirtualMemory

class MemoryManager():
    def __init__(self):
        self.global_memory = None
        self.temp_memories = [1,2]
        self.constants_memory = None
        self.global_range = [1000, 8999]
        self.local_range = [10000, 17999]
        self.constant_range = [18000, 21999]


    def initGlobalMemory(self, size, scope):
        self.global_memory = VirtualMemory(size, scope)
    
    def initConstantsMemory(self, size, scope):
        self.constants_memory = VirtualMemory(size, scope)
    
    def add(self, address, value):
        address = int(address)
        if address>= self.global_range[0] and  address <= self.global_range[1]:
            self.global_memory.add(address, value)

        elif address>= self.constant_range[0] and  address <= self.constant_range[1]:
            self.constants_memory.add(address, value)
    
    def get(self, address):
        address = int(address)
        if address>= self.global_range[0] and  address <= self.global_range[1]:
            return self.global_memory.get(address)

        elif address>= self.constant_range[0] and  address <= self.constant_range[1]:
           return self.constants_memory.get(address)
    
    
