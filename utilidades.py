import random
import math

# Defino función para agregas peliculas
def agregar_pelicula(peliculas):
    cod = random.randint(1, 1000)
    nombre = input("Ingrese el nombre de la película: ")
    anio = input("Ingrese el año de la película: ")
    categoria = input("Ingrese la categoría de la película: ")
    actores = input("Ingrese los actores de la película separados por comas: ").split(',')
    director = input("Ingrese el nombre del director de la película: ")

    pelicula = {
        "cod": cod,
        "nombre": nombre,
        "anio": anio,
        "categoria": categoria,
        "actores": actores,
        "director": director
    }

    peliculas[cod] = pelicula
    print(f"Película agregada correctamente con código {cod}")

# Función para agregar las peliculas ingresadas
def listar_peliculas(peliculas):
    if not peliculas:
        print("No hay películas registradas.")
    else:
        print("Lista de películas registradas:")
        for cod, pelicula in peliculas.items():
            print(f"Código: {cod}, Nombre: {pelicula['nombre']}, Año: {pelicula['anio']}, Categoría: {pelicula['categoria']}")
            print(f"  Actores: {', '.join(pelicula['actores'])}")
            print(f"  Director: {pelicula['director']}")
            print()

# Función para buscar peliculas por categoría
def buscar_pelicula_categoria(peliculas):
    categoria = input("Ingrese la categoría para buscar películas: ")
    encontradas = False

    for cod, pelicula in peliculas.items():
        if pelicula["categoria"].lower() == categoria.lower():
            if not encontradas:
                print(f"Películas encontradas en la categoría '{categoria}':")
                encontradas = True
            
            print(f"Código: {cod}, Nombre: {pelicula['nombre']}, Año: {pelicula['anio']}, Director: {pelicula['director']}")
    
    if not encontradas:
        print(f"No se encontraron películas en la categoría '{categoria}'.")

# Función para calcular la suma de los años de las peliculas
def sumar_anios(peliculas):
    anios = [int(pelicula["anio"]) for pelicula in peliculas.values()]
    suma_anios = math.fsum(anios)
    return suma_anios

# Función para guardar las películas en un archivo txt
def guardar_peliculas(peliculas, archivo):
    with open(archivo, 'w') as f:
        for pelicula in peliculas.values():
            f.write(f"Cod: {pelicula['cod']}\n")
            f.write(f"Nombre: {pelicula['nombre']}\n")
            f.write(f"Anio: {pelicula['anio']}\n")
            f.write(f"Categoria: {pelicula['categoria']}\n")
            f.write(f"Actores: {', '.join(pelicula['actores'])}\n")
            f.write(f"Director: {pelicula['director']}\n")
            f.write("\n")

    print(f"Películas guardadas correctamente en el archivo '{archivo}'.")
