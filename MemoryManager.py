#Memory manager es donde guardamos una pila de memorias y donde podemos crear una memoria apartir de VirtualMemory
from VirtualMemory import VirtualMemory
#se inicia una memoria global solo una ya que solo puede existir una al igual que de constantes
#una pila de memorias locales ya que puede ir a "dormir" alguna de ellas en el transcurso del programa
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
        self.prev = False



    #aqui es donde creamos una memoria global
    def initGlobalMemory(self, size, scope):
        self.global_memory = VirtualMemory(size, scope)
    #aqui es donde creamos una memoria de constantes
    def initConstantsMemory(self, size, scope):
        self.constants_memory = VirtualMemory(size, scope)
    #aqui es donde creamos una memoria local y como podemos tener varias, se hace un push a la pila de memorias locales
    def initLocalMemory(self, size, scope):
        self.local_memories.append(VirtualMemory(size, scope))



    #una vez finalizada su uso se saca de la pila, se destruye esa memoria ya que no podemos tener 2 funciones corriendo a la vez
    def destroyLocalMemory(self):
        self.local_memories.pop()
    #con la direccion de memoria como uno de los parametros y el valor que se añade, dependiendo del rango se agrega en la memoria
    #global,local,constantes o pointers
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


    #al hacer get se hace get del valor dependiendo igualmente del rango es a donde va a buscar
    def get(self, address):
        address = int(address)

        if address>= self.global_range[0] and  address <= self.global_range[1]:
            return self.global_memory.get(address)

        elif address>= self.constant_range[0] and  address <= self.constant_range[1]:
           return self.constants_memory.get(address)

        elif address>= self.local_range[0] and  address <= self.local_range[1]:
            if self.prev and len(self.local_memories) > 1:
              self.prev = False
              return self.local_memories[-2].get(address)
            return self.local_memories[-1].get(address)

        elif address>= self.pointers_global_range[0] and  address <= self.pointers_global_range[1]:
            return self.global_memory.get(address)

        elif address>= self.pointers_local_range[0] and  address <= self.pointers_local_range[1]:
             return self.local_memories[-1].get(address)
