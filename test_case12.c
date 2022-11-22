class main {
  global vars{
    var int num;
  }
  classes {
  }
  functions{

   func int test3(int nn){
        vars{
            var int ii;
        }
        {
          write("Test3")

        }
        return nn
    }

     func int test2(int nn){
        vars{
            var int ii;
        }
        {
          write("Test2")

        }
        return test3(nn)
    }

     func int test(int nn){
        vars{
            var int ii;
        }
        {
          write("Test1")
        }
        return test2(nn)
    }
    func int fact(int nn){
       vars{
            var int value;
        }
      {
      if(nn<=1){
        value = 1
      }
      else{
        value = nn*fact(nn-1)
      };
      }
      return value 
    }
  }
  {
    write(test(1))


  }
}
