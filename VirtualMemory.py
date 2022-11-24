class VirtualMemory():
    def __init__(self, size, scope):
        self.scope = scope
        #mapeo de memoria que se trato de realizar de la manera mas general posible
        #dependiendo si el scope es global o local, los rangos de memoria cambian
        #tanto para variables como temporales
        if scope == "GLOBAL" :
            self.I = [1000, 1999]
            self.F = [2000, 2999]
            self.C = [3000, 3999]
            self.B = [4000, 4999]
            self.IT = [5000,5999]
            self.FT = [6000,6999]
            self.CT = [7000,7999]
            self.BT = [8000,8999]
            self.PT = [30000,30999]


        elif scope == "LOCAL":
            self.I = [10000, 10999]
            self.F = [11000, 11999]
            self.C = [12000, 12999]
            self.B = [13000, 13999]
            self.IT = [14000, 14999]
            self.FT = [15000, 15999]
            self.CT = [16000, 16999]
            self.BT = [17000, 17999]
            self.PT = [31000,31999]
        #rango de direcciones virtuales constantes
        elif scope == "CONSTANTS":
            self.I = [18000, 18999]
            self.F = [19000, 19999]
            self.C = [20000, 20999]
            self.B = [21000, 21999]
        #dependiendo de cualquiera de los scopes se crea la memoria con arreglos de temporales y locales
        #con el tamaño de cada uno de los espacios con valor none inicial
        if scope == "GLOBAL" or scope == "LOCAL":
            self.m_int = [None] * size[0]
            self.m_float = [None] * size[1]
            self.m_char = [None] * size[2]
            self.m_bool = [None] * size[3]
            self.m_tInt = [None] * size[4]
            self.m_tFloat = [None] * size[5]
            self.m_tChar = [None] * size[6]
            self.m_tBool = [None] * size[7]
        #igualmente dependiendo del tamaño de cada uno de los locales constantes se crean sus arreglos respectivos
        elif scope == "CONSTANTS":
            self.m_int = [None] * size[0]
            self.m_float = [None] * size[1]
            self.m_char = [None] * size[2]
            self.m_bool = [None] * size[3]
        #fuera de todo siempre se crean los temporales pointer que pueden estar localmente o globalmente
        self.m_PT = [None] * 1000

        #metodo add con el cual dependiendo del rango en el que este la direccion, se añade al arreglo correspondiente de memorias
        # en el cual dependiendo de en cual caiga, se le resta la direccion base
    def add(self, address, value):
        address = int(address)

        #rangos de locales de cada tipo
        if address>= self.I[0] and address <= self.I[1]:
            self.m_int[address - self.I[0]] = value

        elif address>= self.F[0] and address <= self.F[1]:
            self.m_float[address - self.F[0]] = value

        elif address>= self.C[0] and address <= self.C[1]:
            self.m_char[address - self.C[0]] = value

        elif address>= self.B[0] and address <= self.B[1]:
            self.m_bool[address - self.B[0]] = value

        #rangos de temporales que deben de estar en el rango de direccion y que no sean direcciones constantes
        elif address>= self.IT[0] and address <= self.IT[1] and self.scope != "CONSTANTS":

            self.m_tInt[address - self.IT[0]] = value

        elif address>= self.FT[0] and address <= self.FT[1] and self.scope != "CONSTANTS":
            self.m_tFloat[address - self.FT[0]] = value

        elif address>= self.CT[0] and address <= self.CT[1] and self.scope != "CONSTANTS":
            self.m_tChar[address - self.CT[0]] = value

        elif address>= self.BT[0] and address <= self.BT[1] and self.scope != "CONSTANTS":
            self.m_tBool[address - self.BT[0]] = value

        elif address>= self.PT[0] and address <= self.PT[1] and self.scope != "CONSTANTS":
            if  type(value) == str:
                jump = self.m_PT[address - self.PT[0]]
                self.add(jump, value)
            else:
                self.m_PT[address - self.PT[0]] = value


    #igualmente dependiendo del rango de direccion en el que este, se accede a la casilla del arreglo
    #restandole la direccion base se llega a esa direccion de memoria que estamos buscando su valor
    def get(self, address):
        address = int(address)

        if address>= self.I[0] and address <= self.I[1]:
            return self.m_int[address - self.I[0]]

        elif address>= self.F[0] and address <= self.F[1]:
            return self.m_float[address - self.F[0]]

        elif address>= self.C[0] and address <= self.C[1]:
           return self.m_char[address - self.C[0]]

        elif address>= self.B[0] and address <= self.B[1]:
           return self.m_bool[address - self.B[0]]

        elif address>= self.IT[0] and address <= self.IT[1] and self.scope != "CONSTANTS":
            return self.m_tInt[address - self.IT[0]]

        elif address>= self.FT[0] and address <= self.FT[1] and self.scope != "CONSTANTS":
            return self.m_tFloat[address - self.FT[0]]

        elif address>= self.CT[0] and address <= self.CT[1] and self.scope != "CONSTANTS":
            return self.m_tChar[address - self.CT[0]]

        elif address>= self.BT[0] and address <= self.BT[1] and self.scope != "CONSTANTS":
            return self.m_tBool[address - self.BT[0]]

        elif address>= self.PT[0] and address <= self.PT[1] and self.scope != "CONSTANTS":
            #el unico caso donde se hace un doble salto es en temporal pointer ya que los temporales pointer almacenan una direccion de memoria
            return self.get(self.m_PT[address - self.PT[0]])
