class main {
  global vars{
      var int prueba;
  }
  classes {
  }
  functions{
    func int sum(int elementOne, int elementTwo){
      vars{
        var int aa;
      }
      {
        write(elementOne + elementTwo)
      }
      return aa
    }
  }

  {
    
    sum(1,100)
    sum(200, 300)

  }
}
 