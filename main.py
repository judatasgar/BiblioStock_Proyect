from persistencia import guardar_datos, cargar_datos, RUTA_INVENTARIO, RUTA_PRESTAMOS
from inventario import registrar_item, display_items, buscar_item
from prestamos import registrar_prestamo, registrar_devolucion

def mostrar_menu():
    print("\n==========================================")
    print("=== BIBLIOSTOCK - GESTION DE BIBLIOTECA ===")
    print("==========================================")
    print("1. Registrar ítem")
    print("2. Listar ítems")
    print("3. Buscar ítem")
    print("4. Registrar préstamo")
    print("5. Registrar devolución")
    print("6. Salir")
    print("==========================================")

def main():
    inventario = cargar_datos(RUTA_INVENTARIO)
    prestamos = cargar_datos(RUTA_PRESTAMOS)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_item(inventario)
        elif opcion == "2":
            display_items(inventario)
        elif opcion == "3":
            buscar_item(inventario)
        elif opcion == "4":
            registrar_prestamo(inventario, prestamos)
        elif opcion == "5":
            registrar_devolucion(inventario, prestamos)
        elif opcion == "6":
            guardar_datos(RUTA_INVENTARIO, inventario)
            guardar_datos(RUTA_PRESTAMOS, prestamos)
            print("\nDatos guardados exitosamente. ¡Saliendo de BiblioStock!\n")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione un número del 1 al 6.")

if __name__ == "__main__":
    main()