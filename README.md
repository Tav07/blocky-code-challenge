# Blocky

## 1. Objetivos de aprendizaje
Al finalizar esta tarea, deberías ser capaz de:

- Modelar datos jerárquicos usando árboles.
- Implementar operaciones recursivas en árboles (tanto mutables como inmutables).
- Convertir un árbol en una estructura plana y bidimensional.
- Utilizar herencia para diseñar clases de acuerdo con una interfaz común.

## 2. Introducción
Blocky es un juego con movimientos simples sobre una estructura sencilla, pero, al igual
que el Cubo de Rubik, es bastante desafiante de jugar. El juego se juega en un tablero
generado aleatoriamente, compuesto por cuadrados de cuatro colores diferentes, como este:

<img src="images/blocky_1.png" width="240" height="240" style="display: block; margin: 0 auto" />

Cada jugador tiene su propio objetivo, como crear el "bloque" de color azul más 
grande posible. Después de cada movimiento, el jugador ve su puntuación, determinada 
por qué tan bien ha logrado su objetivo. El juego continúa durante un número determinado 
de turnos, y el jugador con la puntuación más alta al final es el ganador.

Ahora, veamos en más detalle las reglas del juego y las diferentes formas en que se puede 
configurar para jugar.

### 2.1 El tablero de Blocky

Llamamos "bloque" al tablero del juego. Se define mejor de manera recursiva. Un bloque es:

- Un cuadrado de un solo color, o
- Un cuadrado subdividido en 4 bloques de igual tamaño.

El bloque más grande de todos, que contiene toda la estructura, se llama el **bloque de nivel 
superior**. Decimos que este bloque está en el **nivel 0**. Si el bloque de nivel superior está 
subdividido, sus cuatro sub-bloques están en el **nivel 1**. De manera más general, si un bloque 
en el nivel k está subdividido, sus cuatro sub-bloques estarán en el **nivel k+1**.

Un tablero de Blocky tiene una **profundidad máxima permitida**, que es el número de niveles que 
puede alcanzar. Un tablero con una profundidad máxima de 0 no sería divertido, ya que no podría 
subdividirse más allá del nivel superior, lo que significaría que todo el tablero sería de un solo
color.

Este tablero fue generado con una profundidad máxima de 5:

<img src="images/blocky_2.png" width="240" height="240" style="display: block; margin: 0 auto" />

Para la puntuación, las unidades de medida son cuadrados del tamaño de los bloques en la profundidad
máxima permitida. Llamaremos a estos bloques celdas unitarias.

### 2.2 Elegir un bloque y niveles

Los movimientos que se pueden realizar incluyen acciones como rotar un bloque. Lo que hace interesantes 
estos movimientos es que pueden aplicarse a cualquier bloque en cualquier nivel. Por ejemplo, si el 
usuario selecciona todo el bloque de nivel superior en este tablero:

<img src="images/blocky_3.jpg" width="240" height="240" style="display: block; margin: 0 auto" />

y elige rotarlo en sentido antihorario, el tablero resultante es el siguiente:

<img src="images/blocky_4.jpg" width="240" height="240" style="display: block; margin: 0 auto" />

Pero si en lugar de eso, en el tablero original, rotaran el bloque en el nivel 1 (un nivel por debajo del
bloque de nivel superior) ubicado en la esquina superior izquierda, el tablero resultante sería el 
siguiente:

<img src="images/blocky_5.jpg" width="240" height="240" style="display: block; margin: 0 auto" />

Y si en su lugar rotaran el bloque un nivel más abajo, manteniéndose en la esquina superior izquierda, 
obtendrían lo siguiente:

<img src="images/blocky_6.jpg" width="240" height="240" style="display: block; margin: 0 auto" />

Por supuesto, hay muchos otros bloques dentro del tablero, en varios niveles, que el jugador podría haber 
elegido.

### 2.3 Movimientos

Estos son los movimientos permitidos en un tablero de Blocky:

- **Rotar** el bloque seleccionado, ya sea en sentido horario o antihorario.
- **Intercambiar** los 4 sub-bloques dentro del bloque seleccionado, ya sea de forma horizontal o vertical.
- **Romper (Smash)** el bloque seleccionado, ya sea un bloque de un solo color o uno que ya esté subdividido,
se reemplaza con cuatro nuevos sub-bloques generados aleatoriamente. **No se permite romper el bloque de nivel
superior**, ya que eso crearía un juego completamente nuevo. Tampoco se permite romper una **celda unitaria**,
porque ya está en la profundidad máxima permitida.

### 2.4 Objetivos y puntuación
Al inicio del juego, a cada jugador se le asigna un objetivo generado aleatoriamente. Hay dos tipos de 
objetivos:

1.	**Objetivo de bloque (Blob goal).** El jugador debe intentar formar el **bloque más grande** de un color 
específico c. Un bloque es un grupo de celdas conectadas del mismo color. Dos celdas están conectadas 
si sus lados se tocan; el contacto en las esquinas no cuenta. La puntuación del jugador es el número 
de **celdas unitarias** en el bloque más grande del color c.
2. **Objetivo de perímetro (Perimeter goal).** El jugador debe tratar de colocar la mayor cantidad 
posible de celdas de un color específico c en el **perímetro exterior** del tablero. La puntuación del 
jugador es el número total de **celdas unitarias** del color c en el perímetro. **Las celdas en las 
esquinas valen el doble.**

En ambos casos, el objetivo está relacionado con un **color específico**, al que llamaremos **color objetivo**.

### 2.5 Jugadores

El juego puede jugarse en solitario (con un solo jugador) o con dos o más jugadores. No hay un límite definido 
en la cantidad de jugadores, aunque no sería divertido con un número demasiado grande.

Existen tres tipos de jugadores:
1. Jugador humano:
   - Elige sus movimientos según la entrada del usuario.
   - **Solo puede realizar un movimiento de "romper" (smash) por partida.**
2. Jugador aleatorio:
   - Es un jugador controlado por la computadora que elige movimientos de manera aleatoria.
   - No tiene límite en los movimientos de "romper".
   - Si selecciona aleatoriamente "romper" el bloque de nivel superior o una celda unitaria (lo cual no está permitido),
   pierde su turno.
3. Jugador inteligente:
   - Es un jugador controlado por la computadora que elige sus movimientos de manera estratégica.
   - Genera un conjunto de movimientos aleatorios y evalúa la puntuación que obtendría con cada uno.
   - Elige el movimiento que le daría la **mayor puntuación posible**.
   - **No puede realizar movimientos de "romper" (smash)**.

### 2.6 Configuraciones del juego

Un juego de Blocky puede configurarse de varias maneras:
- **Profundidad máxima permitida:**
  - Aunque el patrón de colores del tablero se genera aleatoriamente, se puede controlar el nivel de 
  subdivisión de los bloques.
- **Número y tipo de jugadores:**
  -	Puede haber cualquier cantidad de jugadores de cada tipo.
  - La dificultad del jugador inteligente (**qué tan difícil es jugar contra él**) también puede configurarse.
- **Número de movimientos:**
  -	Se puede establecer un límite de movimientos para la partida.
  -	(El juego terminará antes si un jugador cierra la ventana del juego).
