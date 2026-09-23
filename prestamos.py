from validaciones import normalizar_codigo, normalizar_texto
 
# Esta funcion registra un prestamo de un item existente en el inventario
 
def registrar_prestamo(inventario, prestamos):
    print("\n--- Registrar préstamo ---")
    codigo = input("Ingrese el código del ítem a prestar: ")
    codigo = normalizar_codigo(codigo, [item["codigo"] for item in inventario])
 
    item = next((i for i in inventario if i["codigo"] == codigo), None)
    if item is None:
        print("No existe ningún ítem con ese código.")
        return
 
    if item["cantidad_disponible"] <= 0:
        print(f"No hay unidades disponibles de '{item['titulo']}' para prestar.")
        return
 
    persona = input("Nombre de quien solicita el préstamo: ")
    persona = normalizar_texto(persona, [p["persona"] for p in prestamos])
    item["cantidad_disponible"] -= 1
 
    nuevo_prestamo = {
        "codigo": item["codigo"],
        "titulo": item["titulo"],
        "persona": persona,
        "estado": "prestado"
    }
    prestamos.append(nuevo_prestamo)
 
    print(f"\nPréstamo registrado: '{item['titulo']}' a nombre de {persona}.")

# Esta funcion registra devolucion de un iten previamente prestado
 
def registrar_devolucion(inventario, prestamos):
    print("\n--- Registrar devolución ---")
    codigo = input("Ingrese el código del ítem a devolver: ")
    codigo = normalizar_codigo(codigo, [item["codigo"] for item in inventario])
 
    prestamo = next((p for p in prestamos if p["codigo"] == codigo and p["estado"] == "prestado"), None)
    if prestamo is None:
        print("No se encontró un préstamo activo con ese código.")
        return
 
    prestamo["estado"] = "devuelto"
 
    item = next((i for i in inventario if i["codigo"] == codigo), None)
    if item is not None:
        item["cantidad_disponible"] += 1
 
    print(f"\nDevolución registrada: '{prestamo['titulo']}' devuelto por {prestamo['persona']}.")