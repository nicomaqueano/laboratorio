import json


# Función para obtener una lista de instancias de una clase a partir de un archivo JSON
def obtener_lista_de_objetos(lista_datos, clase):
    return [clase(datos) for datos in lista_datos]

# Función para obtener el índice de un elemento en una lista de diccionarios
def obtener_indice_de_elemento(lista, elemento):
    indices = [x.id for x in lista]
    return indices.index(elemento) if elemento in indices else None

# Función para ordernar un diccionario de manera descendente por su valor
def ordernar_por_valor(diccionario):
    return {nombre: valor for nombre, valor in sorted(diccionario.items(), key=lambda x: x[1], reverse=True)}
