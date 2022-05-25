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
