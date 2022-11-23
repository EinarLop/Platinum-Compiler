class main {
  global vars{
      var int aa,bb,index,aux;
      var int prueba[5];
  }
  classes {
  }
  functions{
    }
  {

    aa=0
    bb= 0
    index=5
    aux=10
    while(aa<index-1)do
    {
      aux=aux-1
      prueba[aa]=aux

      aa=aa+1
    };

    aa=0
    bb= 0

    while(aa<index-1)do
    {

        write(prueba[aa])
        aa=aa+1
    };



  }
}
