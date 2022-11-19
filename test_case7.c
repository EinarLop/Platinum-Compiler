class main {
  global vars{
      var int array[9];
      var int aa,bb,cc;
  }
  classes {
  }
  functions{
  }

  {
    aa = 0
    
    while(aa < 9) do
    {
        array[aa] = 8 - aa
        aa = aa + 1
    };
    aa = 0
    while(aa < 9) do
    {   
        write(array[aa])
        aa = aa + 1
    };
    
  }
}
 