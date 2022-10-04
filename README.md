# Proyecto final para la clase "Diseño de Compiladores"
## Compilador para el lenguaje orientado a objetos "Platinum"
### Desarrolladores: 
1. Einar López Altamirano A01656259
2. Amauri Elian Pérez Cruz A01365611

### Avance 1:
Actualmente el parser y un lexer detectan las estructuras básicas del lenguaje:
1. Clases
2. Funciones
3. Estatutos
4. Expresiones
5. Etc.

En los archivos test_case#.c se puede observar la estructura con la que se tienen que desarrollar los programas. 

Por ejemplo:
```c
class main {
    classes {
        class cars{
            vars{
                var int xxx,cc,dd[1][100];
                var float xxx[1][100];
                var char eee[2], ss, ff[2][2];
            }
            functions{
                func int test(int ii){
                    vars{
                        var int jj;
                    }
                    {
                        for(ij = 1 to 10) do {
                            ii = 1
                        }
                        for(ij = 1 to 10) do {
                            ii = 1
                        }
                        call()
                        call.charlet()
                        read(jjj)
                        write(sjs)
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
             
```
Se utiliza la terminación .c para facilitar el desarrollo en un editor de texto. No tiene ninguna otra funcionalidad.

Actualmente todas las pruebas se pueden correr correctamente y están incluidos prácticamente todos los elementos del lenguaje. No descartamos que con pruebas mucho más complejas salgan errores pero consideramos que con las pruebas que hicimos se incluyen los elementos básicos hasta el momento.


