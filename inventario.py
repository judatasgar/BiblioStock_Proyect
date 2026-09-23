from validaciones import (
    normalizar_codigo,
    normalizar_texto,
    quitar_tildes,
    pedir_entero_positivo
)

# Esta funcion registra un item en el inventario

def registrar_item(inventario):
    codigo = input("Ingrese el codigo del item: ")
    codigo = normalizar_codigo(codigo)
    
    if any(item["codigo"] == codigo for item in inventario):
        print("El codigo ya existe en el inventario. No se puede registrar el item.")
        return

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