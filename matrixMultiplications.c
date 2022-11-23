class main {
  global vars{
      var int aa,bb,index,aux;
      var int matrix[3][3];
      var int matrix2[3][3];
      var int matrix3[3][3];
  }
  classes {
  }
  functions{
    }
  {

    aa=0
    bb= 0
    index=3
    aux=3
    while(aa<index)do
    {
      while(bb<index)do
      {
        matrix[aa][bb]= 9
        matrix2[aa][bb]=aux
        matrix3[aa][bb]= (matrix[aa][bb] * matrix2[aa][bb])
        write(matrix3[aa][bb])
        bb=bb+1
      };
      bb=0

      aa=aa+1
    };

    aa=0
    bb= 0





  }
}
