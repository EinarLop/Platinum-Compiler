class Quadruple:
  def __init__(self,operand,leftOperator,rightOperator,temporal):
      self.operand = operand
      self.leftOperator = leftOperator
      self.rightOperator = rightOperator
      self.temporal = temporal

  def toString(self):
      print( f"{self.operand}, {self.leftOperator},{self.rightOperator},{self.temporal} ")
