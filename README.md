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

Para que un usuario pueda correr una aplicación desarrollada en el lenguaje “Carat” es necesario instalar un ambiente de desarrollo Python 3.0, así como la dependencia Anaconda para correr el Lexer y el Parser.

Las acciones que se pueden realizar son las siguientes:

# Inicio de programa
```
program MiPrograma;
```
Cualquier programa escrito en el lenguaje “Carat” debe de ser iniciado con la línea anterior, cambiando el nombre MiPrograma por el nombre de elección del usuario.

# Declaración de variables
```
var int miVariable1, miVariable2;
var float miFloat1;
```
Para declarar una variable es necesario escribir la palabra var, seguido por el tipo que se desea declarar. Una vez hecho esto, se pueden declarar las variables deseadas.

# Función main
```
main(){
	...
}
```
Para ejecutar cualquier programa, es necesario crear la función main, y dentro de ella poner los estatutos por ejecutar.

# Input
```
input(miVariable1);
```
Para recibir datos de entrada, se utiliza la función input.

# Print
```
print(“Hello, world!”);
```
Para imprimir datos en la consola, se utiliza la función print. La función puede recibir datos enteros, flotantes, strings, o nombres de variables.

# Asignación
```
miVariable1 = 5 + 5;
```
Para realizar una asignación, es necesario haber declarado la variable anteriormente.

# For
```
for i = 0 to 5 do {
	print(i);
}
```
Se debe tomar en consideración que la variable i ya fue declarada anteriormente. El estatuto for se detiene cuando la variable de control es mayor o igual que el límite establecido.

# While
```
while (i > 0) do {
	print(i);
	i = i - 1;
}
```
El estatuto while se ejecuta hasta que la condición deje de ser verdadera.

# If - Else
```
if (i > 5) {
	print(“Variable i es mayor que 5”);
} else {
	print(“Variable i es menor o igual que 5”);
}
```
El estatuto if entra a la condición si esta es verdadera, de otra forma, se va dentro del estatuto else.

# Función Void
```
void func fact(int x) {
    var int resultado;

    resultado = x;

    while(x > 1) do {
        x = x - 1;
        resultado = resultado * x;
    }
    
    print(resultado);
}
```
La función de tipo void, no tiene ningún valor de retorno.

# Función con Retorno
```
int func fact(int x) {
    if(x == 0){
        return(1);
    }
    return(x * (fact(x-1);));
}
```
La función debe de retornar el mismo tipo con el que fue declarado.

# Llamada a función
```
miVar1 = (fact(5););
```
Para llamar a una función, es necesario poner paréntesis que encierran a la función que se desea llamar.

# Pintar hacia arriba
```
lineUp(50);
```
Esta función pinta una línea hacia arriba, dependiendo de la dirección en la que vaya el cursor. El parámetro que recibe es el número de desplazamiento.

# Pintar hacia abajo
```
lineDown(50);
```
Esta función pinta una línea hacia abajo, dependiendo de la dirección en la que vaya el cursor. El parámetro que recibe es el número de desplazamiento.

# Pintar hacia la derecha
```
lineRt(25, 100);
```
Esta función pinta una línea hacia la derecha, dependiendo de la dirección en la que vaya el cursor. El primer parámetro es el ángulo hacia la derecha que tomará el cursor, y el segundo parámetro es el desplazamiento.

# Pintar hacia la izquierda
```
lineLf(25, 100);
```
Esta función pinta una línea hacia la izquierda, dependiendo de la dirección en la que vaya el cursor. El primer parámetro es el ángulo hacia la izquierda que tomará el cursor, y el segundo parámetro es el desplazamiento.

# Moverse a una coordenada
```
point(0, 0);
```
Esta función lleva al cursor a una coordenada sobre el canvas. Los números solo pueden ser positivos y en caso de tener la pluma abajo, el desplazamiento se pintará. El primer parámetro representa el desplazamiento en ‘x’ y el segundo el desplazamiento en ‘y’.

# Pintar un círculo
```
circle(25);
```
Esta función pinta un círculo. El parámetro que recibe representa el radio del círculo

# Pintar un arco
```
arc(25, 90);
```
Esta función pinta un arco. El primer parámetro representa el radio del arco y el segundo parámetro representa el ángulo en donde se detendrá el cursor.

# Pintar sobre el canvas
```
penDown();
```
Esta función baja la pluma sobre el canvas, pintando lo que se le indique.

# Dejar de pintar sobre el canvas
```
penUp();
```
Esta función sube la pluma del canvas, dejando de pintar lo que se le indique.

# Color de la pluma
```
penColor(255,255,255);
```
Esta función cambia el color de la pluma. Los parámetros que recibe son los valores R, G y B del color al que se desea cambiar respectivamente.

# Tamaño de la pluma
```
penSize(10);
```
Esta función cambia el tamaño de la pluma. El parámetro que recibe es el tamaño de la pluma.

# Borrar el canvas
```
clear();
```
Esta función borra todo lo pintado en el canvas.

Algunas consideraciones que son importantes de tomar en cuenta dentro del lenguaje “Carat”, son las siguientes:
Las operaciones aritméticas que son permitidas son: +, -, *, /
Las operaciones de comparación permitidas son: >, <, !=, ==
Las operaciones de condición permitidas son: &, |
La operación de asignación es =

Ejemplo general de un programa escrito en Carat, que imprime en pantalla el logo del lenguaje:

```
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
```
