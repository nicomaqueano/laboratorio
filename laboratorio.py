import json
from reactivo import Reactivo
from experimento import Experimento
from helpers import *


class Laboratorio:
    """
    Clase que representa un laboratorio químico.
    Un laboratorio tiene reactivos, recetas y experimentos.
    """
    def __init__(self, reactivos, recetas, experimentos):
        # Generar listas de objetos Reactivo y Experimento
        self.reactivos = obtener_lista_de_objetos(reactivos, Reactivo)
        self.experimentos_posibles = obtener_lista_de_objetos(experimentos, Experimento)
        # Guardar recetas como una variable del laboratorio
        self.recetas = recetas
        # Lista para guardar los experimentos realizados
        self.experimentos_realizados = []

    # Agregar un reactivo al inventario
    def agregar_reactivo(self, reactivo_dict):
        self.reactivos.append(Reactivo(reactivo_dict))
    
    # Eliminar un reactivo del inventario
    def eliminar_reactivo(self, reactivo_id):
        idx = obtener_indice_de_elemento(self.reactivos, reactivo_id)
        if idx:
            self.reactivos.pop(idx)
        else:
            print(f"El reactivo de ID {reactivo_id} no existe.")

    # Agregar un experimento al laboratorio
    def realizar_experimento(self, experimento_id):
        # Obtener el experimento a realizar
        experimento_idx = obtener_indice_de_elemento(self.experimentos_posibles, experimento_id)
        if experimento_idx is None:
            print(f"El experimento de ID {experimento_id} no existe.")
            return None
        experimento = self.experimentos_posibles[experimento_idx]
        # Obtener la receta del experimento
        indices = [x["id"] for x in self.recetas]
        receta_idx = indices.index(experimento.receta_id) if experimento.receta_id in indices else None
        # Chequear que la receta exista en el laboratorio
        if receta_idx is None:
            print(f"La receta de ID {experimento.receta_id} no existe.")
            return None
        receta = self.recetas[receta_idx]
        # Realizar el experimento
        experimento, self.reactivos = experimento.realizar_experimento(receta, self.reactivos)
        # Guardar el experimento realizado
        self.experimentos_realizados.append(experimento)
