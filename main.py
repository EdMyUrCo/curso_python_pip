
jugadores = {}

def menu():
    print("\n--- Menú de opciones ---")
    print("1. Agregar jugador")
    print("2. Modificar tarjetas rojas de un jugador")
    print("3. Eliminar jugador")
    print("4. Mostrar lista de jugadores")
    print("5. Salir")
    print("------------------------")

while True:
    menu()
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        # Agregar un jugador
        nombre = input("Nombre del jugador: ").strip()
        if nombre in jugadores:
            print(f"El jugador '{nombre}' ya está registrado.")
        else:
            try:
                tarjetas = int(input(f"Tarjetas rojas de '{nombre}': ").strip())
                if tarjetas < 0:
                    print("El número de tarjetas no puede ser negativo.")
                else:
                    jugadores[nombre] = tarjetas
                    print(f"Jugador '{nombre}' agregado con {tarjetas} tarjeta(s) roja(s).")
            except ValueError:
                print("Por favor, ingresa un número válido para las tarjetas.")

    elif opcion == "2":
        # Modificar tarjetas rojas de un jugador
        nombre = input("Nombre del jugador a modificar: ").strip()
        if nombre in jugadores:
            try:
                tarjetas = int(input(f"Nueva cantidad de tarjetas rojas para '{nombre}': ").strip())
                if tarjetas < 0:
                    print("El número de tarjetas no puede ser negativo.")
                else:
                    jugadores[nombre] = tarjetas
                    print(f"Tarjetas rojas de '{nombre}' actualizadas a {tarjetas}.")
            except ValueError:
                print("Por favor, ingresa un número válido para las tarjetas.")
        else:
            print(f"El jugador '{nombre}' no está registrado.")

    elif opcion == "3":
        # Eliminar un jugador
        nombre = input("Nombre del jugador a eliminar: ").strip()
        if nombre in jugadores:
            del jugadores[nombre]
            print(f"Jugador '{nombre}' eliminado del registro.")
        else:
            print(f"El jugador '{nombre}' no está registrado.")

    elif opcion == "4":
        # Mostrar lista de jugadores
        if jugadores:
            print("\n--- Lista de jugadores ---")
            for nombre, tarjetas in jugadores.items():
                print(f"{nombre}: {tarjetas} tarjeta(s) roja(s)")
        else:
            print("No hay jugadores registrados.")

    elif opcion == "5":
        # Salir del programa
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, elige una opción del menú.")