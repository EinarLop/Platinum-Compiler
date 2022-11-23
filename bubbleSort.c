class main {
  global vars{

      var int array[5];
      var int len;
      var int ii,jj,aux;
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
    array[3]=3
    array[4]=4


    for(ii=0 to len-1) do
    {
      for(jj=0 to (len-ii-1)) do
      {
        if(array[jj] > array[jj+1]){
            aux=array[jj]
            array[jj] = array[jj+1]
            array[jj+1]=aux

        };
      };
    };

    for(ii=0 to len) do
    {
      write(array[ii])

    };


  }
}
