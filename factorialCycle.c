class main {
  global vars{
    var int num;
  }
  classes {
  }
  functions{

    func int factorial(int fact){
        vars{
            var int ii, factorial;
        }
        {
          factorial=1
          for(ii=1 to fact+1)do
          {
            factorial=factorial*ii
          };
          write("factorial de",fact)
        }

        return factorial
    }


  }
  {
    write(factorial(4))


  }
}
