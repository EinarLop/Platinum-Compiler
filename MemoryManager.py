from VirtualMemory import VirtualMemory

class MemoryManager():
    def __init__(self):
        self.global_memory = None
        self.local_memories = []
        self.constants_memory = None
        self.global_range = [1000, 8999]
        self.local_range = [10000, 17999]
        self.constant_range = [18000, 21999]
        self.pointers_global_range = [30000, 30999]
        self.pointers_local_range = [31000, 31999]
        #self.lookPrev = False




    def initGlobalMemory(self, size, scope):
        self.global_memory = VirtualMemory(size, scope)

    def initConstantsMemory(self, size, scope):
        self.constants_memory = VirtualMemory(size, scope)

    def initLocalMemory(self, size, scope):
        self.local_memories.append(VirtualMemory([10,10,10,10,10,10,10,10], "LOCAL"))
        



    def destroyLocalMemory(self):
        self.local_memories.pop()

    def add(self, address, value):
        address = int(address)
        if address>= self.global_range[0] and  address <= self.global_range[1]:
            self.global_memory.add(address, value)

        elif address>= self.constant_range[0] and  address <= self.constant_range[1]:
            self.constants_memory.add(address, value)

        elif address>= self.local_range[0] and  address <= self.local_range[1]:
            self.local_memories[-1].add(address, value)

        elif address>= self.pointers_global_range[0] and  address <= self.pointers_global_range[1]:
             self.global_memory.add(address, value)

        elif address>= self.pointers_local_range[0] and  address <= self.pointers_local_range[1]:
             self.local_memories[-1].add(address, value)



    def get(self, address, prev=False):
        address = int(address)

        if address>= self.global_range[0] and  address <= self.global_range[1]:
            return self.global_memory.get(address)

        elif address>= self.constant_range[0] and  address <= self.constant_range[1]:
           return self.constants_memory.get(address)

        elif address>= self.local_range[0] and  address <= self.local_range[1]:
            # Remove the 2 following lines if program breaks
            if prev and len(self.local_memories) > 1:
              return self.local_memories[-2].get(address)
            return self.local_memories[-1].get(address)

        elif address>= self.pointers_global_range[0] and  address <= self.pointers_global_range[1]:
            return self.global_memory.get(address)

        elif address>= self.pointers_local_range[0] and  address <= self.pointers_local_range[1]:
             return self.local_memories[-1].get(address)
