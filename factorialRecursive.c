class main {
  global vars{
    var int num;
  }
  classes {
  }
  functions{

    func int fact(int nn){
       vars{
            var int value, valueTwo;
        }
      {
      if(nn<=1){
        value = 1
      }
      else{
        valueTwo = fact(nn-1)
        value = nn*valueTwo
      };
      }
      return value
    }
  }
  {
    num = fact(6)
    write(num)


  }
}
