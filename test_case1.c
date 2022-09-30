class main {
    classes {
        class cars{
            vars{
                var int xxx;
            }
            functions{
                func int test(int ii){
                    vars{
                        var int jj;
                    }
                    {
                        test()
                    }
                    return 1
                }    
            }
        }
    } 
    vars{
        var float jj;
    }
    functions{
        func int test(int ii){
            vars{
                var int jjj;
            }
            {
                test()
            }
            return 1
        }
    }
    {
    test()
    }
}
