print("Bienvenido a la lista de tareas")

opciones = {
    1: "Ver tareas pendientes",
    2: "Agregar tarea",
    3: "Eliminar tarea",
    4: "Mostrar tareas",
    5: "Salir"
}

def mostrar_menu():
    print("\nMenú de opciones:")
    for opcion, descripcion in opciones.items():
        print(f"{opcion}. {descripcion}")

def agregar_tarea(tareas):
    tarea = input("Ingrese la tarea que desea agregar: ")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada a la lista.")

def eliminar_tarea(tareas):
    if not tareas:
        print("No hay tareas para eliminar.")
        return
    print("Tareas pendientes:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea}")
    try:
        indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada}' eliminada de la lista.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.") 

def mostrar_tareas(tareas):
    print("Tareas pendientes:")
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def main():
    tareas = []
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                mostrar_tareas(tareas)
            elif opcion == 2:
                agregar_tarea(tareas)
            elif opcion == 3:
                eliminar_tarea(tareas)
            elif opcion == 4:
                mostrar_tareas(tareas)
            elif opcion == 5:
                print("Saliendo de la lista de tareas.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
