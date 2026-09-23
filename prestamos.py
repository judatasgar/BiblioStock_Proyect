from validaciones import normalizar_codigo, normalizar_texto
 
# Esta funcion registra un prestamo de un item existente en el inventario
 
def registrar_prestamo(inventario, prestamos):
    print("\n--- Registrar préstamo ---")
    codigo = input("Ingrese el código del ítem a prestar: ")
    codigo = normalizar_codigo(codigo)
 
    item = next((i for i in inventario if i["codigo"] == codigo), None)
    if item is None:
        print("No existe ningún ítem con ese código.")
        return
 
    if item["cantidad_disponible"] <= 0:
        print(f"No hay unidades disponibles de '{item['titulo']}' para prestar.")
        return
 
    persona = input("Nombre de quien solicita el préstamo: ")
    persona = normalizar_texto(persona)
 
    item["cantidad_disponible"] -= 1
 
    nuevo_prestamo = {
        "codigo": item["codigo"],
        "titulo": item["titulo"],
        "persona": persona,
        "estado": "prestado"
    }
    prestamos.append(nuevo_prestamo)
 
    print(f"\nPréstamo registrado: '{item['titulo']}' a nombre de {persona}.")
 