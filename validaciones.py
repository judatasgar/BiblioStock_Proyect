import unicodedata
import re

def quitar_tildes(texto): 
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return texto_sin_tildes

def normalizar_texto(texto_nuevo, lista_existente):
    texto_nuevo = texto_nuevo.strip()
    texto_normalizado = quitar_tildes(texto_nuevo).lower()
    for texto in lista_existente:
        if quitar_tildes(texto).lower() == texto_normalizado:
            return texto
    return texto_nuevo. title()

def normalizar_codigo(texto_nuevo, lista_existente):
    codigo = texto_nuevo.strip().upper().replace(' ','')
    regex = re.match(r'^([A-Z]+)-?(\d+)$', codigo)
    if regex:
        prefijo, numero = regex.groups()
        codigo = f'{prefijo}-{int(numero):03d}'
    for existe in lista_existente:
        if existe.strip().upper() == codigo:
            return existe
    return codigo

def pedir_entero_positivo(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        print("Valor invalido. Ingrese un numero entero mayor a 0.")