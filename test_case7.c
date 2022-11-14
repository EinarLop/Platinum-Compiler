class main {
  global vars{
      var float dddd;
  }
    classes {
        class cars{
            vars {
                var int cc;
                var float bb;
            }
            functions{
                func int test1(int notUsed,float ccc){
                    vars{
                        var float cc;
                        var float zz;
                        var int ii;
                    }
                    {
                          read(cc)
                          write("hola mundo")
                          ii= 99 + cc*(cc-bb)
                    }
                    return 1
                }
                func int test2(int alo, float qqq){
                    vars{
                        var float cc;
                        var float aa;
                        var int abc;
                    }
                    {

                          aa = aa

                    }
                    return 1
                }
            }
        }

    }
    functions{
        func int test66(int ee){
            vars{
                var int ff;
            }
            {
                ff = 2
            }
            return 1
        }
    }
    {
        aa=1
    }
}
