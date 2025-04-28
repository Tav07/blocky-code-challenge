from typing import List, Optional
import random

# Lista de colores posibles para los bloques
COLORS = ['red', 'blue', 'green', 'yellow']

class Block:
    """
    Clase que representa un blque del juego Blocky
    Cada bloque puede ser subdividido en 4 sub-bloques o ser una celda unitaria
    """
    
    def __init__(self, color: Optional[str] = None, level: int = 0, max_depth: int = 2):
        """
        Inicializa un bloque.

        Args:
            color (str): color del bloque si es una celda unitaria
            level (int): mivel de profundidad del bloque en el arbol
            max_depth (int): profundidad maxima permitida
        """
        self.color = color if color else random.choice(COLORS)
        self.level = level
        self.max_depth = max_depth
        self.children: List[Block] = []

    def is_unit_cell(self) -> bool:
        """Retorna True si el bloque es una celda unitaria (no tiene hijos)"""
        return len(self.children) == 0

    def subdivide(self):
        """
        Divide el bloque en 4 sub-bloques si no ha alcanzado la profundidad maxima
        """
        if self.level >= self.max_depth:
            print(f"No se puede subdividir mas, nivel actual: {self.level}")
            return
        
        if not self.is_unit_cell():
            print("Este bloque ya esta subdividido")
            return

        for _ in range(4):
            child = Block(level=self.level + 1, max_depth=self.max_depth)
            self.children.append(child)

        # Al subdividir, el bloque ya no tiene color propio
        self.color = None

    def __str__(self):
        """Devuelve una representacion en string del bloque para debuggear"""
        if self.is_unit_cell():
            return f"Color: {self.color}, Nivel: {self.level}"
        else:
            return f"Subdividido (Nivel {self.level}) con {len(self.children)} hijos"

    def print_structure(self, indent: int = 0):
        """
        Imprim la estructura del bloque y sus hijos de manera jerarquica
        """
        print(' ' * indent + str(self))
        for child in self.children:
            child.print_structure(indent + 2)


