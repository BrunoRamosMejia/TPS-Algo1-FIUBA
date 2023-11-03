"""Lógica del juego Unruly"""

from typing import List, Tuple, Any

Grilla = Any


def crear_grilla(desc: List[str]) -> Grilla:
    """Crea una grilla a partir de la descripción del estado inicial.

    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Se puede asumir que la cantidad de las
    filas y columnas son múltiplo de dos. **No** se puede asumir que la
    cantidad de filas y columnas son las mismas.
    Los caracteres pueden ser los siguientes:

    Caracter  Contenido de la celda
    --------  ---------------------
         ' '  Vacío
         '1'  Casillero ocupado por un 1
         '0'  Casillero ocupado por un 0

    Ejemplo:

    >>> crear_grilla([
        '  1 1 ',
        '  1   ',
        ' 1  1 ',
        '  1  0',
    ])
    """
    grilla = []
    for palabra in desc:
        nueva = list(palabra)
        grilla.append(nueva)
    return grilla

def dimensiones(grilla: Grilla) -> Tuple[int, int]:
    """Devuelve la cantidad de columnas y la cantidad de filas de la grilla
    respectivamente (ancho, alto)"""
    dimensiones = []
    dimension_x = len(grilla[0])
    dimension_y = len(grilla)
    dimensiones.append(dimension_x)
    dimensiones.append(dimension_y)
    return tuple(dimensiones)

def posicion_es_vacia(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está vacía"""
    posicion = grilla[fil][col]
    if posicion == " ":
        return True
    elif posicion == "0" or "1":
        return False

def posicion_hay_uno(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está el valor 1"""
    posicion = grilla[fil][col]
    if posicion == "1":
        return True
    elif posicion == " " or "1":
        return False


def posicion_hay_cero(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está el valor 0"""
    posicion = grilla[fil][col]
    if posicion == "0":
        return True
    elif posicion == " " or "1":
        return False


def cambiar_a_uno(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, colocando el valor 1 en la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    grilla[fil][col] = "1"


def cambiar_a_cero(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, colocando el valor 0 en la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    grilla[fil][col] = "0"


def cambiar_a_vacio(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, eliminando el valor de la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    grilla[fil][col] = " "


def fila_es_valida(grilla: Grilla, fil: int) -> bool:
    """Devuelve un booleano indicando si la fila de la grilla denotada por el
    índice `fil` es considerada válida.

    Una fila válida cuando se cumplen todas estas condiciones:
        - La fila no tiene vacíos
        - La fila tiene la misma cantidad de unos y ceros
        - La fila no contiene tres casilleros consecutivos del mismo valor
    """
    fila = grilla[fil]
    contador_1 = 0
    contador_0 = 0
    contador_vacio = 0
    for casilla in fila:
        if casilla == "1":
            contador_1 += 1
        elif casilla == "0":
            contador_0 += 1
        elif casilla == " ":
            contador_vacio += 1
    if contador_1 == contador_0:
        condicion1 = True
    else:
        condicion1 = False
    if contador_vacio == 0:
        condicion2 = True
    else:
        condicion2 = False
    for valor in range(len(fila)-2):
        if fila[valor] == fila[valor+1] == fila[valor+2]:
            condicion3 = False
            break
        else:
            condicion3 = True
    if condicion1 == condicion2 == condicion3 == True:
        return True
    else:
        return False


def columna_es_valida(grilla: Grilla, col: int) -> bool:
    """Devuelve un booleano indicando si la columna de la grilla denotada por
    el índice `col` es considerada válida.

    Las condiciones para que una columna sea válida son las mismas que las
    condiciones de las filas."""
    contador_1 = 0
    contador_0 = 0
    contador_vacio = 0
    for fila in grilla:
        if fila[col] == "1":
            contador_1 += 1
        elif fila[col] == "0":
            contador_0 += 1
        elif fila[col] == " ":
            contador_vacio += 1
    if contador_1 == contador_0:
        condicion1 = True
    else:
        condicion1 = False
    if contador_vacio == 0:
        condicion2 = True
    else:
        condicion2 = False
    for valor in range(len(grilla)-2):
        if grilla[valor][col] == grilla[valor+1][col] == grilla[valor+2][col]:
            condicion3 = False
            break
        else:
            condicion3 = True
    if condicion1 == condicion2 == condicion3 == True:
        return True
    else:
        return False
    
            


def grilla_terminada(grilla: Grilla) -> bool:
    """Devuelve un booleano indicando si la grilla se encuentra terminada.

    Una grilla se considera terminada si todas sus filas y columnas son
    válidas."""
    todas_las_filas = False
    todas_las_columnas = False
    cantidad_de_filas = len(grilla)-1
    for f in range(cantidad_de_filas):
        if fila_es_valida(grilla, f) == True:
            todas_las_filas = True
        else:
            return False
    # columna_es_valida(grilla, columnas)
    cantidad_de_columnas = len(grilla[0])-1
    for c in range(cantidad_de_columnas):
        if columna_es_valida(grilla, c):
            todas_las_columnas = True
        if todas_las_filas == True:
            if todas_las_columnas ==True:
                return True
        else:
            return False