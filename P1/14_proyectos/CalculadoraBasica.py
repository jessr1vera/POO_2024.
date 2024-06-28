from Funciones_compartir import solicitarNumeros, calculadora, espereTecla

opcion = True
while opcion:
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- Potencia \n 6.- Raiz \n 7.- SALIR ")
    opcion = input("\t Elige una opción: ").upper()
    if opcion in ["1", "2", "3", "4", "5", "6"]:
        n1, n2 = solicitarNumeros()
        resultado = calculadora(n1, n2, opcion)
        print(resultado)
    elif opcion == "7":
        print("Saliendo del programa.")
        opcion = False
    else:
        print("Opción no válida.")
    espereTecla()

    
