# Proyecto final para la clase "Diseño de Compiladores"
## Compilador para el lenguaje orientado a objetos "Platinum"
### Desarrolladores: 
1. Einar López Altamirano A01656259
2. Amauri Elian Pérez Cruz A01365611


### Bugs
- [ ] No se puede usar || o && o < > en expresiones normales (fuera de ciclos, ifs)
- [ ] Cubo semantico no tiene entradas para char y bool
- [ ] Agregar = a cubo
- [ ] Error en scope de variables en block de main


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


### Avance 2:
Actualmente nuestro compilador tiene clases nuevas como lo son para las Var, VarsTable, Function, FunctionsTable,Parameters,SemanticCube con los cuales hicimos pruebas para poder verificar que al crear una variable individual y hacer un add a la tabla de variables funcionara al igual que con function, se puede realizar búsqueda para ambas funciones, pero se debe especificar el parámetro como objeto para que en consola pueda desplegarse correctamente.


De momento se han agregado puntos neurálgicos solo para la parte de variables, hay métodos con los cuales ya se identifican el id, tipo y se marca que tipo de función es en nuestro testcase4.c y todo está reflejado igualmente en la gramática y con esa información que se detecta en la gramática, se va almacenando para posteriormente agregar dicha variable con la información obtenida de la gramática a la tabla de variables.

Ahora mismo la salida que recibimos en consola con los tests que hemos hecho se ven de la siguiente manera.
```
A) impresion de la tabla de variables para ver que variables hay en una sola tabla

aa: float, class
vv: float[1000000], class
zz: float, class
ww: int[100000][10], class
jj: int, class
cc: float, function
dd: float, global
ff: int, function
None
```

```
B) impresión con busqueda de una sola función para ver si existe en la tabla de funciones, se busca con su nombre
###functionSearch###
aa: float, class
vv: float[1000000], class
zz: float, class
ww: int[100000][10], class
jj: int, class
cc: float, function
dd: float, global
ff: int, function
type:int None
##parameters##
int:eggs
int:shoes
```


### Avance 3:
El avance tres no se ha completado el avance de esta semana respecto a los cuádruplos, se realizó una refactorización además de que se creó la clase 'class' donde se almacenan las funciones consecuentemente con sus propias tablas de variables, el avance de cuádruplos se tiene creadas las clases de Quadruple y QuadrupleList además de los primeros pasos de puntos neurálgicos vistos en clase para almacenar en stack de lista de operadores y operandos. El avance se prevé que se termine en los próximos días a partir del día actual 17/10/2022. Relacionado a el avance 2 el directorio de variables, funciones y clases ha sido completado y probado.


### Avance 4:
El avance tres ha sido completado, en gran parte se ha completado igualmente el avance 4, siguen faltando detalles respecto al chequeo de tipos y un detalle de temporales en la variable de control del ciclo for, pero fuera de eso se han completado toda la generación de cuadruplos sin incluir llamadas a funciones y llamada a atributos de objetos. Se adjunta ejemplo de como se verian los cuadruplos generados.
![image](https://user-images.githubusercontent.com/52212675/200008137-4852d4c7-97be-4b22-99c8-ade79b49b035.png)

#### Avance 5:
Generación de los cuadruplos de función (Sin ERA),y sin los cuadruplos de parametros validación de número y tipo de parametros en llamadas de función, número de variables (IFCH, TITFTCTH) por función y por clase.

