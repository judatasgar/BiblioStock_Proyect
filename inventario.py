from validaciones import (
    normalizar_codigo,
    normalizar_texto,
    pedir_entero_positivo
)

# Esta funcion registra un item en el inventario

def registrar_item(inventario):
    codigo = input("Ingrese el codigo del item: ")
    codigo = normalizar_codigo(codigo, [item["codigo"] for item in inventario])

    if any(item["codigo"] == codigo for item in inventario):
        print("El codigo ya existe en el inventario. No se puede registrar el item.")
        return

    titulo = input("Ingrese el titulo del item: ")
    titulo = normalizar_texto(titulo, [item["titulo"] for item in inventario])

    autor = input("Ingrese el autor del item: ")
    autor = normalizar_texto(autor, [item["autor"] for item in inventario])

    categoria = input("Ingrese la categoria del item: ")
    categoria = normalizar_texto(categoria, [item["categoria"] for item in inventario])

    ubicacion = input("Ingrese la ubicacion del item: ")
    ubicacion = normalizar_texto(ubicacion, [item["ubicacion"] for item in inventario])

    cantidad_total = pedir_entero_positivo("Ingrese la cantidad total: ")

    nuevo_item = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "cantidad_total": cantidad_total,
        "cantidad_disponible": cantidad_total,
        "ubicacion": ubicacion
    }
    inventario.append(nuevo_item)
    print("Item registrado exitosamente.")

# esta funcion muestra todos los items del inventario 

def display_items(inventario):
    if len(inventario) == 0:
        print("No hay items en el inventario.")
        
        print("============ INVENTARIO ============ ")
    
    
    for item in inventario: 
        print("Codigo:", item["codigo"])
        print("Titulo:", item["titulo"])
        print("Autor:", item["autor"])
        print("Categoria:", item["categoria"])
        print("Cantidad total:", item["cantidad_total"])
        print("Cantidad disponible:", item["cantidad_disponible"])
        print("Ubicacion:", item["ubicacion"])
        print("----------------------")
    
    # esta funcion busca un item en el inventario por su codigo y lo muestra si lo encuentra
    
def buscar_item(inventario):
    codigo = input("INgresa el codigo del item que deseas buscar: ")
    
    for item in inventario:
        if item["codigo"] == codigo:
            print("Item encontrado:")
            print("Codigo:", item["codigo"])
            print("Titulo:", item["titulo"])
            print("Autor:", item["autor"])
            print("Categoria:", item["categoria"])
            print("Cantidad total:", item["cantidad_total"])
            print("Cantidad disponible:", item["cantidad_disponible"])
            print("Ubicacion:", item["ubicacion"])
            return
    print("Item no encontrado.")    