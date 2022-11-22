class main {
  global vars{
    var int num;
  }
  classes {
  }
  functions{

    func int test(int nn){
        vars{
            var int ii;
        }
        {
          if(nn<2)
          {
            ii= 1
          }
          else
          {
            ii= test(nn-1)
          }

        }
        return ii
    }


  }
  {
    write(test(1))


  }
}
