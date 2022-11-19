class VirtualMemory():
    def __init__(self, size, scope):
        self.scope = scope

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

        elif scope == "CONSTANTS":
            self.I = [18000, 18999]
            self.F = [19000, 19999]
            self.C = [20000, 20999]
            self.B = [21000, 21999]

        if scope == "GLOBAL" or scope == "LOCAL":
            self.m_int = [None] * size[0]
            self.m_float = [None] * size[1]
            self.m_char = [None] * size[2]
            self.m_bool = [None] * size[3]
            self.m_tInt = [None] * size[4]
            self.m_tFloat = [None] * size[5]
            self.m_tChar = [None] * size[6]
            self.m_tBool = [None] * size[7]

        elif scope == "CONSTANTS":
            self.m_int = [None] * size[0]
            self.m_float = [None] * size[1]
            self.m_char = [None] * size[2]
            self.m_bool = [None] * size[3]

        self.m_PT = [None] * 10
        #meter fuera de los ifs los temporal pointers y colocar
        #self.m_tp = none *size
    def add(self, address, value):
        #print("----->", address)
        address = int(address)


        if address>= self.I[0] and address <= self.I[1]:
            self.m_int[address - self.I[0]] = value

        elif address>= self.F[0] and address <= self.F[1]:
            self.m_float[address - self.F[0]] = value

        elif address>= self.C[0] and address <= self.C[1]:
            self.m_char[address - self.C[0]] = value

        elif address>= self.B[0] and address <= self.B[1]:
            self.m_bool[address - self.B[0]] = value

        elif address>= self.IT[0] and address <= self.IT[1] and self.scope != "CONSTANTS":

            self.m_tInt[address - self.IT[0]] = value

        elif address>= self.FT[0] and address <= self.FT[1] and self.scope != "CONSTANTS":
            self.m_tFloat[address - self.FT[0]] = value

        elif address>= self.CT[0] and address <= self.CT[1] and self.scope != "CONSTANTS":
            self.m_tChar[address - self.CT[0]] = value

        elif address>= self.BT[0] and address <= self.BT[1] and self.scope != "CONSTANTS":
            self.m_tBool[address - self.BT[0]] = value

        elif address>= self.PT[0] and address <= self.PT[1] and self.scope != "CONSTANTS":
           # print("bbbbbb", [value, type(value), address])
            if  type(value) == str:
                jump = self.m_PT[address - self.PT[0]]
                self.add(jump, value)
                #print("add11", self.m_int)
            else:
                self.m_PT[address - self.PT[0]] = value
               # print("add12", [address, value, self.m_PT])



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
           # print("gettttt1", [address, self.get(self.m_PT[address - self.PT[0]])])
            #print("gettttt2", self.get(self.m_PT[address - self.PT[0]])

            
            return self.get(self.m_PT[address - self.PT[0]])














        # LI_BA = [5000, 5999]
        # LF_BA = [6000, 6999]
        # LC_BA = [7000, 7999]
        # LB_BA = [8000, 8999]

        # TI_BA = [9000, 9999]
        # TF_BA = [10000, 10999]
        # TC_BA = [11000, 11999]
        # TB_BA = [12000, 12999]



#     memory
#         variables
#         temp

# localMemoriesPile = []

# global = memory()
# loccal = memory()
