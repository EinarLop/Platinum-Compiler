from Error import Error


class SemanticCube:
    def __init__(self):
        self.cube = {
            'int': {
                'int': {
                    '+': 'int',
                    '-': 'int',
                    '/': 'float',
                    '*': 'int',
                    '&&': 'boolean',
                    '||': 'boolean',
                    '<': 'boolean',
                    '>': 'boolean',
                    '<=': 'boolean',
                    '>=': 'boolean'
                },
                'float': {
                    '+':'float',
                    '-':'float',
                    '/':'float',
                    '*':'float',
                    '&&': 'boolean',
                    '||': 'boolean',
                    '<': 'boolean',
                    '>': 'boolean',
                    '<=': 'boolean',
                    '>=': 'boolean'
                }
            },
            'float': {
                  'float': {
                    '+':'float',
                    '-':'float',
                    '/':'float',
                    '*':'float',
                    '&&': 'boolean',
                    '||': 'boolean',
                    '<': 'boolean',
                    '>': 'boolean',
                    '<=': 'boolean',
                    '>=': 'boolean'
                  },
                  'int': {
                    '+':'float',
                    '-':'float',
                    '/':'float',
                    '*':'float',
                    '&&': 'boolean',
                    '||': 'boolean',
                    '<': 'boolean',
                    '>': 'boolean',
                    '<=': 'boolean',
                    '>=': 'boolean'
                  }
                  
            },
            'char':{
                'char':'char'
            }
            
        }
    def semantic(self, operand1, operand2, operator):
        if operand1 in self.cube and operand2 in self.cube[operand1] and operator in self.cube[operand1][operand2]:
           return self.cube[operand1][operand2][operator], None
        else: return None, Error('Type Mismatch')




