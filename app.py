from funciones_peliculas import agregar_pelicula, listar_peliculas, buscar_pelicula_categoria, sumar_anios, guardar_peliculas

# Función principal del programa
def main():
    peliculas = {}

    while True:
        print("\nMenú:")
        print("1. Agregar película")
        print("2. Listar películas")
        print("3. Buscar película por categoría")
        print("4. Sumar años de todas las películas")
        print("5. Salir y guardar películas en archivo")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                agregar_pelicula(peliculas)
            elif opcion == 2:
                listar_peliculas(peliculas)
            elif opcion == 3:
                buscar_pelicula_categoria(peliculas)
            elif opcion == 4:
                suma_anios = sumar_anios(peliculas)
                print(f"La suma de todos los años registrados es: {suma_anios}")
            elif opcion == 5:
                archivo = input("Ingrese el nombre del archivo para guardar las películas: ")
                guardar_peliculas(peliculas, archivo)
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        
        except ValueError:
            print("Error: Ingrese un número válido para la opción.")

if __name__ == "__main__":
    main()
