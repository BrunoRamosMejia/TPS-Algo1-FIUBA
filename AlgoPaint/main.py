import gamelib
import png
import pila
import copy

ANCHO_VENTANA, ALTO_VENTANA, DELTA_INFO = 600, 600, 100
INFO1 = "Controles: 1-7: Blanco - Negro - Rojo - Azul - Verde - Amarillo - Ingresar color"
INFO2 = "c: Cargar PPM - g: Guardar PPM - p: Guardar PNG"
INFO_COLOR_ACTUAL = "Color actual : "
VACIO = " "
LAPIZ, BALDE = "lapiz" , "balde"
CARGAR, GUARDAR, ARCHIVO_PNG = "c", "g", "p"
PALETA = {"blanco":"#FFFFFF", "negro":"#000000", "rojo":"#FF0000", "azul":"#0000FF", "verde":"#00FF00", "amarillo":"#FFFF00"}
TECLAS = {"1": "blanco", "2": "negro", "3": "rojo", "4": "azul", "5": "verde", "6": "amarillo", "7": "entrada"}
BLANCO = "#FFFFFF"
X_INICIAL, Y_INICIAL = 20, 20

def paint_nuevo(ancho, alto):
    '''inicializa el estado del programa con una imagen vacía de ancho x alto pixels'''
    paint = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            fila.append(BLANCO)
        paint.append(fila)
    return paint

def paint_mostrar(paint, pincel, herramienta):
    '''dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_begin()
    casilla = 30
    for i, fila in enumerate(paint):
        for j, columna in enumerate(fila):
            x = j * casilla
            y = i * casilla
            pixel = columna
            gamelib.draw_rectangle(x, y, x + casilla, y + casilla, outline='black', fill=pixel)
    
    """Informacion"""
    gamelib.draw_text(INFO1, ANCHO_VENTANA//2, ALTO_VENTANA + (DELTA_INFO//4), size=12, fill='white', italic=True)
    gamelib.draw_text(INFO2, ANCHO_VENTANA//2, ALTO_VENTANA + DELTA_INFO - (DELTA_INFO//2), size=12, fill='white', italic=True)
    gamelib.draw_text(f'{INFO_COLOR_ACTUAL}{pincel} - Herramienta : {herramienta}', ANCHO_VENTANA//2, ALTO_VENTANA + DELTA_INFO - (DELTA_INFO//4), size=12, fill='white', italic=True)
    gamelib.draw_end()

def paint_actualizar(paint, x, y, pincel, herramienta):
    """
    Actualiza el estado del juego
    """
    dim_fil, dim_col = dimensiones_paint(paint)
    j = x // (ANCHO_VENTANA // dim_fil)
    i = y // (ALTO_VENTANA // dim_col)
    if i > dim_fil - 1 or j > dim_col - 1:
        return paint
    else:
        if herramienta == LAPIZ:
            paint[i][j] = pincel
            return paint
        elif herramienta == BALDE:
            fila, columna = i, j
            paint = balde_actualizar(paint, fila, columna, pincel, dim_fil, dim_col)
            return paint


def manejo_de_archivos(paint, tecla):
    """
    Recibe las teclas ingresadas y Permite Cargar y guardar los Archivos en Formato PPM o PNG, para despues aplicarlos al paint
    """
    try:
        if tecla == CARGAR:
            paint = cargar_archivo()
            return paint

        elif tecla == GUARDAR:
            paint = guardar_archivo_PPM(paint)
            return paint

        elif tecla == ARCHIVO_PNG:
            paint = guardar_archivo_PNG(paint)
            return paint

    except FileNotFoundError:
        gamelib.say("Archivo no Encontrado")
        return paint

def cargar_archivo():
    ruta_archivo = gamelib.input("Ingrese la ruta del archivo: ")
    paint = []
    with open(ruta_archivo, 'r') as archivo:
        res = []
        for linea in archivo:
            linea_dividida = linea.rstrip('\n')
            res.append(linea_dividida)
        dimensiones = res[1].split(" ")
        h = int(dimensiones[0])
        w = int(dimensiones[1])
        pixeles = res[3:]
        pixeles_nuevo = []
        for pixel in pixeles:
            pixel_nuevo = decimal_a_hex(pixel)
            pixeles_nuevo.append(pixel_nuevo)
        for i in range(h):
            fila = []
            for j in range(w):
                fila.append(pixeles_nuevo[i * w + j])
            paint.append(fila)
    # print(paint) test
    return paint

def guardar_archivo_PPM(paint):
    ruta_archivo = gamelib.input("PPM: Ingrese la ruta de guardado: ")
    with open(ruta_archivo, 'w') as archivo:
        encabezado = gamelib.input("Encabezado: ")
        archivo.write(f'{encabezado}\n')
        dim_ancho, dim_alto = dimensiones_paint(paint)
        archivo.write(f'{dim_ancho} {dim_alto}\n')
        archivo.write('255\n')
        for fila in paint:
            for pixel in fila:
                pixel = hex_a_decimal(pixel)
                archivo.write(f'{pixel}\n')
    return paint

def guardar_archivo_PNG(paint):
    ruta_archivo = gamelib.input("PNG: Ingrese la ruta de guardado: ") + ".png"
    paleta = []
    imagen = []
    for fila in paint:
        nueva_fila = []
        for pixel in fila:
            pixel_decimal = hex_a_decimal_tupla(pixel)
            if pixel_decimal not in paleta:
                paleta.append(pixel_decimal)
            indice_color = paleta.index(pixel_decimal)
            nueva_fila.append(indice_color)
        imagen.append(nueva_fila)
    png.escribir(ruta_archivo, paleta, imagen)
    return paint

def balde_actualizar(paint, fila, columna, pincel, dim_fil, dim_col):
    """
    Actualiza de forma recursiva el paint cuando la herramienta actual es el balde
    """
    color_original = paint[fila][columna]
    color_nuevo = pincel
    if color_nuevo != color_original:
        paint[fila][columna] = color_nuevo
        adyacentes = [(fila, columna-1), (fila, columna+1), (fila-1, columna), (fila+1, columna)]
        for f, c in adyacentes:
            if 0 <= f < dim_fil and 0 <= c < dim_col:
                if paint[f][c] == color_original:
                    balde_actualizar(paint, f, c, pincel, dim_fil, dim_col)
        return paint
    return paint

# ==================== FUNCIONES AUX ====================

def dimensiones_paint(paint):
    """
    Devuelve las dimensiones del paint en una tupla de la siguiente forma: (Dimensiones de las fila, Dimensiones de las columnas)
    """
    dim_filas =  len(paint)
    dim_columnas = len(paint[0])
    return (dim_filas, dim_columnas)

def color_actualizar(pincel, tecla):
    """
    Devuelve el color en formato Hexadecimal seleccionado por el usuario 
    """
    if tecla != "7":
        teclas = TECLAS
        color = teclas[tecla]
        pincel = PALETA[color]
    else:
        nuevo_color = gamelib.input("Ingrese el Color deseado: ")
        if nuevo_color is None:
            return pincel
        if len(nuevo_color) == 7 and nuevo_color[0] == "#":
            pincel = str(nuevo_color)
        elif nuevo_color[0] != "#" or len(nuevo_color) != 7:
            pincel = "#FFFFFF"
            gamelib.say("Color Incorrecto, ingrese un nuevo Numero")
    return pincel

def hex_a_decimal(hexadecimal):
    """
    Convierte un numero del formato hexadecimal(str) al formato decimal(str): #RRGGBB -> 000 000 000
    """
    hexadecimal = hexadecimal[1:]
    r = int(hexadecimal[0:2], 16)
    g = int(hexadecimal[2:4], 16)
    b = int(hexadecimal[4:6], 16)
    return f'{r} {g} {b}'

def hex_a_decimal_tupla(hexadecimal):
    """
    Convierte un numero del formato hexadecimal(str) al formato decimal(str): #RRGGBB -> 000 000 000
    Funcion para facilitar el uso del guardado PNG
    """
    hexadecimal = hexadecimal[1:]
    r = int(hexadecimal[0:2], 16)
    g = int(hexadecimal[2:4], 16)
    b = int(hexadecimal[4:6], 16)
    return r, g, b

def decimal_a_hex(decimal):
    """
    Convierte un numero del formato decimal (str) a hexadecimal(str): 000 000 000 -> #RRGGBB
    """
    decimal = decimal.split(" ")
    a = int(decimal[0])
    b = int(decimal[1])
    c = int(decimal[2])
    hexa = f'#{a:02x}{b:02x}{c:02x}'
    return hexa.upper()

def cambio_de_herramienta(tecla):
    """
    Define la herramienta a utilizar en el programa
    """
    return BALDE if tecla == "b" else LAPIZ

def deshacer_z(historial, pila_rehacer, paint):
    if historial.esta_vacia():
        return paint
    pila_rehacer.apilar(copy.deepcopy(paint))
    paint = historial.desapilar()
    return paint

def rehacer_x(historial, pila_rehacer, paint):
    if pila_rehacer.esta_vacia():
        return paint
    historial.apilar(copy.deepcopy(paint))
    paint = pila_rehacer.desapilar()
    return paint

# ==================== MAIN ====================

def main():
    gamelib.title("AlgoPaint: Por Bruno Ramos Mejia.")
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA + DELTA_INFO)

    paint = paint_nuevo(X_INICIAL, Y_INICIAL)
    pincel = BLANCO
    herramienta = LAPIZ

    historial = pila.Pila()
    pila_rehacer = pila.Pila()

    while gamelib.loop(fps=15):
        paint_mostrar(paint, pincel, herramienta)

        for ev in gamelib.get_events():
            if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
                x, y = ev.x, ev.y
                historial.apilar(copy.deepcopy(paint))
                paint = paint_actualizar(paint, x, y, pincel, herramienta)
                while not pila_rehacer.esta_vacia():
                    pila_rehacer.desapilar()
            elif ev.type == gamelib.EventType.KeyPress:
                tecla = ev.key
                if tecla in "1234567":
                    pincel = color_actualizar(pincel, tecla)
                elif tecla in "gcp":
                    paint = manejo_de_archivos(paint, tecla)
                elif tecla in "bv":
                    herramienta = cambio_de_herramienta(tecla)
                elif tecla in "zx":
                    if tecla == "z":
                        paint = deshacer_z(historial, pila_rehacer, paint)
                    else:
                        paint = rehacer_x(historial, pila_rehacer, paint)

gamelib.init(main)