class main {
  global vars{
      var bool sumOne;
      var int aa;
  }
  classes {
  }
  functions{
    func int sum(int elementOne){
      vars{
        var bool aa;
      }
      {
        write("inside sum")
      }
      return elementOne + elementOne 
    }
  }
  {
    aa = sum(1)

    write(aa)
  }
  
}

 