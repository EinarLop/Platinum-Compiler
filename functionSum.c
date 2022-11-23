class main {
  global vars{
      var bool sumOne;
      var int aa, bb;
  }
  classes {
  }
  functions{
    func int sum(int elementOne, int elementTwo){
      vars{
        var bool aa;
      }
      {
        write("inside sum")
      }
      return elementOne + elementTwo
    }

  }
  {
    aa = sum(7,7)
    bb = sum(5,5)

    write(sum(aa, bb))


  }

}
