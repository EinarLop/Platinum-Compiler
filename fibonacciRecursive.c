class main {
  global vars{
    var int num;
  }
  classes {
  }
  functions{

    func int fibo(int nn){
       vars{
            var int value, valueTwo, valueThree;
        }
      {
      if(nn<=1){
        value = nn
      }
      else{
        valueTwo = fibo(nn-1)
        valueThree = fibo(nn-2)
        value = valueTwo + valueThree
      };
      }
      return value
    }
  }
  {
    num = fibo(9)
    write(num)
  }
}
