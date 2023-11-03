import pila

# blanco = "#FFFFFF"
# dec_blanco = "255 255 255"

# # f'{dec:02x}'

# def hex_a_decimal_tupla(hexadecimal):
#     """
#     Convierte un numero del formato hexadecimal(str) al formato decimal(str): #RRGGBB -> 000 000 000
#     Funcion para facilitar el uso del guardado PNG
#     """
#     hexadecimal = hexadecimal[1:]
#     r = int(hexadecimal[0:2], 16)
#     g = int(hexadecimal[2:4], 16)
#     b = int(hexadecimal[4:6], 16)
#     return r, g, b

# def decimal_a_hex(decimal):
#     decimal = decimal.split(" ")
#     a = int(decimal[0])
#     b = int(decimal[1])
#     c = int(decimal[2])
#     hexa = f'#{a:02x}{b:02x}{c:02x}'
#     return hexa.upper()

# print(hex_a_decimal_tupla(blanco))

# paint = [
#     ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'],
#     ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'],
#     ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'],
#     ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'],
#     ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], 
#     ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'],
#     ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'],
#     ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'],
#     ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'],
#     ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF']
#     ]

# paleta = [
#     (0, (0, 0, 0)),
#     ("elefante", (255, 0, 0)),
#     ("nashe", (0, 0, 255)),
#     ("70", (0, 255, 0))
# ]

# print(paleta[0][0])
# print(paleta[1][0])
# print(paleta[2][0])
# print(paleta[3][0])

class paint:
    def __init__(self, lienzo):
        self.lienzo = lienzo
        self.color_seleccionado = "#FFFFFF"
        self.paleta = {"blanco":"#FFFFFF", "negro":"#000000", "rojo":"#FF0000", "azul":"#0000FF", "verde":"#00FF00", "amarillo":"#FFFF00"}
        self.historial = pila.Pila()

    def actualizar_lienzo(lienzo):