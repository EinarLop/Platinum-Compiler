class main {
  global vars{
    var int num1,num2;
  }
  classes {
  }
  functions{

    func int fibonacci(int terms){
        vars{
            var int nextTerm;
            var int ii;
        }
        {
          num1=0
          num2=1
          nextTerm = num1+num2
          for(ii=3 to terms)do
          {
            write("next term",nextTerm)
            num1=num2
            num2=nextTerm
            nextTerm=num1+num2
          };
          write("last term")
        }
        return nextTerm
    }


  }
  {
    write(fibonacci(10))
  }
}
