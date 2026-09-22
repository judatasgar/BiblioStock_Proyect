import json
import os

RUTA_INVENTARIO = "inventario.json"
RUTA_PRESTAMOS = "prestamos.json"

def cargar_datos(ruta):
    """Carga los datos desde un archivo JSON. Si no existe o falla, retorna una lista vacía."""
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

def guardar_datos(ruta, datos):
    """Guarda la lista de datos especificada en la ruta JSON dada."""
    with open(ruta, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=2, ensure_ascii=False)