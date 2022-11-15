class Quadruple:
  def __init__(self,operator,leftOperand,rightOperand,temporal):
      self.operator = operator
      self.leftOperand = leftOperand
      self.rightOperand = rightOperand
      self.temporal = temporal

  def toString(self):
      print( f"{self.operator},{self.leftOperand},{self.rightOperand},{self.temporal} ")
      return f"{self.operator},{self.leftOperand},{self.rightOperand},{self.temporal}"