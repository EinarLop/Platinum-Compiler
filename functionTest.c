class main {
  global vars{
      var int prueba;

  }
  classes {
  }
  functions{
    func int test1(int param1){
        vars{
            var float cc;
        }
        {
              param1= param1 + 1
              write("estamos en test1")
        }
        return param1
    }
  }
  {


    prueba= test1(69)
    write(prueba)



  }
}
