class main {
  global vars{
      var int prueba;
  }
  classes {
  }
  functions{
    func int sum(int bb, int cc){
      vars{
        var int aa;
      }
      {
        aa = 1 + 1
        write(aa)
      }
      return aa
    }
  }

  {
    prueba = 1 + 1
    write("Hello World")
    sum(1,2)
    sum(1,3)
    write("Hello World After Functions")

  }
}
 