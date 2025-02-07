# Blocky

## Objetivos de aprendizaje
Al finalizar esta tarea, deberías ser capaz de:

- Modelar datos jerárquicos usando árboles.
- Implementar operaciones recursivas en árboles (tanto mutables como inmutables).
- Convertir un árbol en una estructura plana y bidimensional.
- Utilizar herencia para diseñar clases de acuerdo con una interfaz común.

## Introducción
Blocky es un juego con movimientos simples sobre una estructura sencilla, pero, al igual
que el Cubo de Rubik, es bastante desafiante de jugar. El juego se juega en un tablero
generado aleatoriamente, compuesto por cuadrados de cuatro colores diferentes, como este:

<img src="images/blocky_1.png" width="240" height="240" style="display: block; margin: 0 auto" />

Cada jugador tiene su propio objetivo, como crear el "bloque" de color azul más 
grande posible. Después de cada movimiento, el jugador ve su puntuación, determinada 
por qué tan bien ha logrado su objetivo. El juego continúa durante un número determinado 
de turnos, y el jugador con la puntuación más alta al final es el ganador.
