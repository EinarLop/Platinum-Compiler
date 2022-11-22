class main {
  global vars{
      var int aa, bb;
      var float cc,dd;
      var bool zz,yy;
  }
  classes {
  }
  functions{

  }
  {
    cc = 2*(22.1+11/44)+((22/11)*2+1)
    dd= (((900*2+57.11/(11+11*4.3))*10+34)*cc)/cc
    write("variable cc",cc)
    write("variable dd",dd)

    if(cc<dd)
    {
      write("cc is less than dd")
    };

    if(dd>cc)
    {
      write("dd is greater than cc")
    };

    aa=22
    bb=22
    if(aa<=bb)
    {
      write("aa is less or equal than bb")
    };
    aa=50
    bb=50
    if(aa>=bb)
    {
      write("aa is greater than or equal than bb")
    };

    aa=33
    bb=33
    if(aa==bb)
    {
      write("aa is equal to bb")
    };
    aa=1
    bb=1
    if(aa == 1 && bb==1 )
    {
      write("aa AND bb")
    };
    aa=1
    bb=2
    if(aa == 1 || bb==1 )
    {
      write("aa OR bb")
    };
    read(aa)
  }

}
