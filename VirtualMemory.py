class VirtualMemory():
    def __init__(self, size):
        self.GI = [1000, 1999]
        self.GF = [2000, 2999]
        self.GC = [3000, 3999]
        self.GB = [4000, 4999]
        

        self.m_int = [None] * size[0]
        self.m_float = [None] * size[1]
        self.m_char = [None] * size[2]
        self.m_bool = [None] * size[3]
        self.m_tInt = [None] * size[4]
        self.m_tFloat = [None] * size[5]
        self.m_tChar = [None] * size[6]
        self.m_tBool = [None] * size[7]
        

    def add(self, address, value):
        # print(address)

        address = int(address)
        if address>= self.GI[0] and address <= self.GI[1]:
            # print("I")
            self.m_int[address - self.GI[0]] = value

        elif address>= self.GF[0] and address <= self.GF[1]:
            print("F")
            self.m_float[address - self.GF[0]] = value
        
        elif address>= self.GC[0] and address <= self.GC[1]:
            print("C")
            self.m_char[address - self.GC[0]] = value

        elif address>= self.GB[0] and address <= self.GB[1]:
            print("B")
            self.m_bool[address - self.GB[0]] = value

    def get(self, address):
        address = int(address)

        if address>= self.GI[0] and address <= self.GI[1]:
            return self.m_int[address - self.GI[0]]

        elif address>= self.GF[0] and address <= self.GF[1]:
            return self.m_float[address - self.GF[0]]
        
        elif address>= self.GC[0] and address <= self.GC[1]:
           return self.m_char[address - self.GC[0]]

        elif address>= self.GB[0] and address <= self.GB[1]:
           return self.m_bool[address - self.GB[0]]

        

        
    










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




