import os
import platform

def borrarPantalla():

    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def esperarTecla():
    input("Presiona cualquier tecla para continuar...")
