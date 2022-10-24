class main {
    classes {
        class cars{
            vars {
                var int cc;
                var float bb;
                var int aa;
            }
            functions{
                func int test1(int notUsed){
                    vars{
                        var int cc;
                        var int aa;
                        var int abc;
                    }
                    {
                        abc = cc + aa
                    }
                    return test()
                }
                 func float test2(int rr){
                    vars{
                        var float uu,qq;
                        var char cc;
                        var int rr,jj,xx,zz,ww;
                    }
                    {
                        if(cc + bb < rr * cc)
                        {
                          jj=bb+rr
                        }
                        else
                        {
                          xx=zz-cc
                        };

                        ww=aa*xx+qq
                    }
                    return 1
                }
            }
        } 
    }
    vars{
        var float dddd;
    }
    functions{
        func int test66(int ee){
            vars{
                var int ff;
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
