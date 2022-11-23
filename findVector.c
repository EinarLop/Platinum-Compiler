class main {
  global vars{

      var int array[5];
      var int len;
      var int ii,jj,findNum;
  }
  classes {
  }
  functions{

  }
  {
    len=5
    array[0]=5
    array[1]=2
    array[2]=1
    array[3]=54
    array[4]=4
    findNum=54

    for(ii=0 to len-1) do
    {
      if(array[ii] == findNum)
      {
        write("we found it at index",ii)
      };

    };


  }
}
