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

          ii= test(nn-1)
        }
        return 1
    }


  }
  {
    write(test(4))


  }
}
