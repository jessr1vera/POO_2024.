def insertarPelicula(peliculas):
    pelicula = input("Introduce el nombre de la película a agregar: ")
    peliculas.append(pelicula)
    print(f"Película '{pelicula}' agregada a la lista.")

def eliminarPelicula(peliculas):
    pelicula = input("Introduce el nombre de la película a eliminar: ")
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        print(f"Película '{pelicula}' eliminada de la lista.")
    else:
        print(f"La película '{pelicula}' no se encuentra en la lista.")

def consultarPeliculas(peliculas):
    if peliculas:
        print("Lista de películas:")
        for i, pelicula in enumerate(peliculas, 1):
            print(f"{i}. {pelicula}")
    else:
        print("La lista de películas está vacía.")

def buscarPelicula(peliculas):
    pelicula = input("Introduce el nombre de la película a buscar: ")
    if pelicula in peliculas:
        print(f"La película '{pelicula}' se encuentra en la lista.")
    else:
        print(f"La película '{pelicula}' no se encuentra en la lista.")

def vaciarLista(peliculas):
    peliculas.clear()
    print("La lista de películas ha sido vaciada.")


def espereTecla():
    input("Oprima cualquier tecla para continuar...")





import math

def solicitarNumeros():
    n1 = float(input("Introduce el primer número: "))
    n2 = float(input("Introduce el segundo número: "))
    return n1, n2

def calculadora(n1, n2, opcion):
    if opcion == "1":
        return f"El resultado de la suma es: {n1 + n2}"
    elif opcion == "2":
        return f"El resultado de la resta es: {n1 - n2}"
    elif opcion == "3":
        return f"El resultado de la multiplicación es: {n1 * n2}"
    elif opcion == "4":
        return f"El resultado de la división es: {n1 / n2}" 
    elif opcion == "5":
        return f"El resultado de la potencia es: {n1 ** n2}"
    elif opcion == "6":
        return f"El resultado de la raíz es: {math.sqrt(n1)}" 
    else:
        return "Opción no válida"

def espereTecla():
    input("Presiona una tecla para continuar...")



