class main {
  global vars{
      var int aa,bb,index,aux;
  }
  classes {
  }
  functions{
    func int pelos(int value){
        vars{
            var int ii, factorial;
        }
        {
            write("inside pelos")
            value = value * 2 + 3
        }

        return value
    }

    func int patito(int value){
        vars{
            var int ii, factorial;
        }
        {
            value = pelos(value * 2) 
        }

        return value
    }

    }
  {
    
    write(patito(4))

  }
}