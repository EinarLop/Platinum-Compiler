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

Para probar los distintos archivos de prueba es necesario modificar el número de test en las últimas lineas del archivo main.py, de igual forma, si se desea crear nuevas pruebas solo es necesario crear un archivo con cualquier extensión (recomendamos .c) y definir en main.py que ese es el test que se desea correr. 

Para correr el compilador es necesario descargar todos los archivos del repositorio, el cual continene los siguientes archivos/carpetas:
1. Carpeta - ply: Contiene los archivos necesarios de la liberería PLY 
2. Archivo - main.py: Contiene la implementación del lexer y parser, incluido los tokens, palabras reservadas, expresiones regulares y gramáticas
3. Archivos - test_case#.c: Contienen ejemplos de programas aceptados por el lexer y parser

Y correr el archivo main.py de la siguiente forma

```bash
python3 main.py
```

