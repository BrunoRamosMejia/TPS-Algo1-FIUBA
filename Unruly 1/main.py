import random

import niveles
import unruly

def main():
    nivel = random.choice(niveles.NIVELES)
    grilla = unruly.crear_grilla(nivel)
    # continuar el código...
    estado = unruly.grilla_terminada(grilla)
    print("=============================================================================")
    print("                ʙɪᴇɴᴠᴇɴɪᴅᴏ ᴀ ᴜɴʀᴜʟʏ (ᴘᴏʀ ʙʀᴜɴᴏ ʀᴀᴍᴏꜱ ᴍᴇᴊɪᴀ)")                
    print("=============================================================================")
    print("Instrucciones: Completar la grilla con los valores '1' y '0' hasta llenar")
    print("toda la grilla")
    print("Para colocar un valor (Sea 1, 0 o Vacio), ingrese los valores correspondientes")
    print("Fila, Columna y Valor que desea agregar separados por una barra '/'.")
    print("ACLARACION DE COORDENADAS: Las coordenadas estan representadas en Filas y")
    print("columnas, ambas que van desde 0 en adelante dependiendo de las dimensiones")
    print("de la grilla.")
    print("============================= G r i l l a ===================================")
    mostrar_grilla(grilla)
    while estado == False:
        colocar_valor(grilla)
        print("Estado del Juego:")
        mostrar_grilla(grilla)
        estado = unruly.grilla_terminada(grilla)
    print("       ¡𝙁𝙀𝙇𝙄𝘾𝙄𝘿𝘼𝘿𝙀𝙎! ¡𝙂𝘼𝙉𝘼𝙎𝙏𝙀 𝙀𝙇 𝙅𝙐𝙀𝙂𝙊!")
    print("             ¡𝙂𝙍𝘼𝘾𝙄𝘼𝙎 𝙋𝙊𝙍 𝙅𝙐𝙂𝘼𝙍!")

def colocar_valor(grilla):
    entrada = input("Ingrese un valor [Fila/Columna/Valor)]: ")
    instruccion = entrada.split("/")
    if len(instruccion) == 3:
        fila = int(instruccion[0])
        columna = int(instruccion[1])
        valor = instruccion[2]
        if valor == "vacio":
            unruly.cambiar_a_vacio(grilla, columna, fila)
        elif valor == "1":
            unruly.cambiar_a_uno(grilla, columna, fila)
        elif valor == "0":
            unruly.cambiar_a_cero(grilla, columna, fila)
    else:
        print("El valor ingresado no es valido. Porfavor vuelva a ingresar otro valor")

def mostrar_grilla(grilla):
    cont_fila = -1
    cont_columna = -1
    print("   ", end="")
    for fila in grilla:
        cont_columna += 1
        print(f"| {cont_columna} ", end="")
    print()
    for fila in grilla:
        cont_fila += 1
        print(f" {cont_fila} ", end="")
        for columna in fila:
            print(f"| {columna} ", end="")
        print()

main()