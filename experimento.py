import random
from helpers import obtener_indice_de_elemento


class Experimento:
    """
    Clase que representa un experimento de laboratorio. 
    Para crear un experimento, se necesitan los siguientes atributos:
    - id (int): identificador único del experimento
    - receta_id (int): identificador de la receta asociada al experimento
    - personas (list[str]): lista de personas responsables del experimento
    - fecha (str): fecha en la que se realizó el experimento
    - costo_asociado (float): costo asociado al experimento
    - resultado (str): resultado del experimento
    """

    def __init__(self, datos_experimento):
        self.id = datos_experimento["id"]
        self.receta_id = datos_experimento["receta_id"]
        self.personas = datos_experimento["personas_responsables"]
        self.fecha = datos_experimento["fecha"]
        self.costo_asociado = datos_experimento["costo_asociado"]
        self.resultado = datos_experimento["resultado"]
        self.fallo_por_inventario = False

    # Realizar el experimento dado
    def realizar_experimento(self, receta, reactivos):
        # Iterar sobre los reactivos utilizados en la receta
        for reactivo_utilizado in receta["reactivos_utilizados"]:
            # Chequear que el reactivo exista en el laboratorio
            reactivo_idx = obtener_indice_de_elemento(reactivos, reactivo_utilizado["reactivo_id"])
            if reactivo_idx is None:
                print(f"El reactivo {reactivo_utilizado} no existe en el laboratorio.")
                self.resultado = "Fallo por reactivo inexistente."
                return self, reactivos
            reactivo = reactivos[reactivo_idx]
            # Chequear si el reactivo está caducado
            if reactivo.esta_caducado(self.fecha):
                print(f"El reactivo {reactivo.nombre} ha caducado.")
                reactivo.agregar_vencimiento()
                self.resultado = "Fallo por reactivo caducado."
                return self, reactivos
            # Chequear que la unidad de medida de la receta corresponda a la del inventario
            if reactivo.unidad_medida != reactivo_utilizado["unidad_medida"]:
                reactivo.convertir_unidad(reactivo_utilizado["unidad_medida"])
            # Chequear que haya suficiente reactivo en el inventario
            if not reactivo.hay_disponibilidad(reactivo_utilizado["cantidad_necesaria"]):
                print(f"No hay suficiente reactivo de ID {reactivo_utilizado['reactivo_id']} para realizar el experimento de ID {self.id}.")
                self.fallo_por_inventario = True
                self.resultado = "Fallo por falta de inventario."
                return self, reactivos
            # Restar la cantidad de reactivo utilizada con un error simulado
            desperdicio = reactivo_utilizado["cantidad_necesaria"] * random.uniform(0.1 / 100, 22.5 / 100)
            cantidad_real = reactivo_utilizado["cantidad_necesaria"] + desperdicio
            reactivo.restar_inventario(cantidad_real)
            reactivo.desperdicio += desperdicio
            # Actualizar el contador de veces de uso del reactivo
            reactivo.agregar_uso()
            # Calcular el costo
            self.costo_asociado = cantidad_real * reactivo.costo
        # Aumentar el contador de veces hecho del experimento
        return self, reactivos
