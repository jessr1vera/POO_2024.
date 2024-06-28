from Funciones_compartir import insertarPelicula, eliminarPelicula, consultarPeliculas, buscarPelicula, vaciarLista

peliculas = []

opcion_peliculas = True
while opcion_peliculas:
    print("\n\t..::: MENU PELÍCULAS :::... \n 1.- Agregar \n 2.- Eliminar \n 3.- Consultar \n 4.- Buscar \n 5.- Vaciar lista \n 6.- Salir ")
    opcion = input("\t Elige una opción: ").upper()

    if opcion == '1':
        insertarPelicula(peliculas)
    elif opcion == '2':
        eliminarPelicula(peliculas)
    elif opcion == '3':
        consultarPeliculas(peliculas)
    elif opcion == '4':
        buscarPelicula(peliculas)
    elif opcion == '5':
        vaciarLista(peliculas)
    elif opcion == '6':
        opcion_peliculas = False
        print("Regresando al menú principal.")
    else:
        print("Opción no válida, intente de nuevo.")