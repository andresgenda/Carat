# **CARAT COMPILER**
El lenguaje Carat es un lenguaje de programación gráfico para que todas las personas puedan aprender a programar con facilidad.

# Avance 1 - LéxicoSintaxis
El avance 1 consiste en establecer los tokens del lenguaje Carat, así como las gramáticas que determinan la sintaxis del mismo. Cualquier programa escrito en el lenguaje Carat debe de seguir con la sintaxis determinada en este avance. 

# Avance 2 - Directorio de funciones y Tabla de variables
El avance 2 consiste en crear un directorio de funciones, en donde se guarda el nombre de una función, junto a su tipo de retorno y sus respectivas variables. Las variables se manejan como otro directorio, en donde se guarda el nombre de cada variable junto a su respectivo tipo.

# Avance 3 - Corrección de directorio de funciones y creación de pilas
El avance 3 consistió en corregir los puntos neurálgicos referentes a la creación y correcta asignación del directorio de funciones y sus llamadas a la tabla de variables. De la misma manera, se comenzó la creación del cubo semántico y las pilas necesarias para la futura generación de cuádruplos.

# Avance 4 - Creación correcta de cubo semántico y generación de cuádruplos para operaciones aritméticas y de asignación
Lo que se generó en el avance 4 fue la correcta creación y métodos para acceder al cubo semántico, así como la generación de funciones para identificar tipo de operaciones y el tipo de operandos. De la misma manera, se creó la clase de cuádruplos para la generación de los mismos, así como los puntos neurálgicos para realizar correctamente los cuádruplos con la prioridad adecuada de las operaciones aritméticas básicas, así como su asignación a una variable.

# Avance 5 - Cuádruplos de aritmética, parentésis, comparación, condición y ciclos
Lo que se generó para el avance 5 fue la creación de cuádruplos para operaciónes aritmética con y sin paréntesis, las operaciones de comparación, los estatutos de condicion (if y else), de impresión, de lectura de datos y ciclos (while). Asimismo se comenzo la implementación de generación de cuádruplos para el estatuto for.

# Avance 6 - Generación de código de ciclos completa, generación de código de funciones, asignación de memoria virtual, refactorización de directorio de funciones
Lo que se realizó para el avance 6 fue completar la generación de código de ciclos (for). Asimismo, se término la generación de código para llamadas a funciones, así como su validación de parámetros y tipos utilizando una tabla de parámetros. De la misma forma, se asigno un espacio de memoria a cada variable, dependiendo de su scope (global, local, temporal y constante) y de su tipo. Se cambió la creación de cuádruplos para que ahora tomen en cuenta las direcciones de cada variable para cada operación. Finalmente, se refactorizó el directorio de funciones y se creó una clase especial para su uso.

# Avance 8 - Funciones especiales completas, recursividad, funciones con retorno y vacías, máquina virtual funcionando
Lo que se realizó hasta el avance 8 fue la ejecución de la aplicación propia (funciones especiales para pintar), la ejecución de operaciones aritméticas, condicionales y cíclicas. Asimismo, se ejecutan funciones de tipo void o con retorno. Las aplicaciones con retorno son capaces de llamarse a sí mismas (llamadas recursivas) y mostrar un resultado adecuado. 

# MANUAL DE USUARIO - Quick Reference Manual

```python
program Carat; 

var int miVar1, tam;

void func diamond(){
    var int cont;

    lineLf(60,200);

    cont = 0;

    while(cont < 2)do{
        lineLf(120,200);
        cont = cont + 1;
    }

    lineLf(150, 170);
    lineDown(170);

    lineLf(16.5, 180);
    lineDown(180);
    lineRt(31.5, 180);
    penUp();
    lineRt(75, 53);
    penDown();

    cont = 0;
    
    for miVar1 = 0 to 8 do {
        if(miVar1 < 2){
            lineLf(120, 50);
        }else{
            if(cont == 0){
                lineRt(120,50);
                cont = 1;
            }else{
                lineLf(120, 50);
                cont = 0;
            }
            
        }
    }

    lineLf(180, 50);
    lineLf(300, 150);
}

void func letterC(){
    arc(60, 180);
}

void func letterA(){
    lineLf(80, 120);
    lineRt(160, 120);
    lineLf(180, 60);
    lineLf(80, 20);
    penUp();
    lineDown(20);
    lineRt(80, 0);
    lineDown(60);
    lineRt(100, 0);
}

void func letterR(){
    lineLf(90, 120);
    lineLf(90, 0);
    penUp();
    arc(30, 180);
    penDown();
    arc(30, 180);
    lineLf(90, 60);
    lineLf(25, 65);
    lineLf(65, 0);
}

void func letterT(){
    lineLf(90, 120);
    lineLf(90, 25);
    lineRt(180, 50);
    lineDown(25);
    lineRt(90, 120);
    lineLf(90, 0);
}

void func nombre(){
    (letterC();)

    penUp();
    lineUp(50);
    penDown();
    
    (letterA();)

    penUp();
    lineUp(50);
    penDown();

    (letterR();)

    penUp();
    lineUp(50);
    penDown();

    (letterA();)

    penUp();
    lineUp(50);
    penDown();

    (letterT();)
}

main () {
    penColor(115, 194, 251);
    tam = 5;
    penSize(tam);

    (diamond();)

    penUp();
    point(0, 0);
    lineLf(90, 0);
    lineDown(50);
    lineLf(90, 150);
    penDown();

    penColor(0, 128, 255);

    (nombre();)
}
