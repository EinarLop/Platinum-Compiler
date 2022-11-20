class main {
  global vars{
      var int array[9];
      var int aa,bb,cc;
      var float dd;
  }
  classes {
  }
  functions{
  
    func int test(int nn){
      vars{
        var int value;
    
      }
      {
        value = test(1)

      }
      return value
    }
  }
  {
   write(test(6))

  }
}
 