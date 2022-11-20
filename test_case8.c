class main {
  global vars{
      var int prueba;
      var float popp;
      var char jej;
      var bool jkjkjkjk;
      var int array[2];
      var int matrix[2][5];
      var int qqq;

  }
  classes {
  }
  functions{
    func int test1(int param1){
        vars{
            var float cc;
            var float zz;
            var int ii;
            var int array2[6];
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
