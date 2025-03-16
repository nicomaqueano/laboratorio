import datetime
from helpers import obtener_indice_de_elemento


class Reactivo:
    """
    Clase que representa un reactivo de laboratorio. Un reactivo tiene los siguientes atributos:
    - id (int): identificador único del reactivo
    - nombre (str): nombre del reactivo
    - descripcion (str): descripción del reactivo
    - costo (float): costo del reactivo
    - categoria (str): categoría a la que pertenece el reactivo
    - inventario_disponible (float): cantidad de reactivo disponible en el inventario
    - unidad_medida (str): unidad de medida en la que se mide el reactivo
    - minimo_sugerido (int): cantidad mínima sugerida de reactivo en el inventario
    - conversiones_posibles (list[dict]): lista de diccionarios con las conversiones posibles del reactivo
    - fecha_caducidad (str): fecha de caducidad del reactivo
    """
    
    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.descripcion = datos["descripcion"]
        self.costo = datos["costo"]
        self.categoria = datos["categoria"]
        self.inventario_disponible = datos["inventario_disponible"]
        self.unidad_medida = datos["unidad_medida"]
        self.minimo_sugerido = datos["minimo_sugerido"]
        self.conversiones_posibles = datos["conversiones_posibles"]
        self.fecha_caducidad = datos["fecha_caducidad"]
        self.veces_usado = 0
        self.veces_vencido = 0
        self.desperdicio = 0

    # Convertir cantidad en el inventario a otra unidad de medida
    def convertir_unidad(self, unidad_final):
        # Chequear que la unidad final sea distinta a la actual
        if unidad_final == self.unidad_medida:
            print(f"El reactivo {self.nombre} ya está en la unidad {unidad_final}.")
        else:
            # Chequear que la unidad final sea una de las unidades posibles
            idx = obtener_indice_de_elemento(self.conversiones_posibles, unidad_final)
            if not idx:
                print(f"La unidad {unidad_final} no es una unidad de medida válida para el reactivo {self.nombre}.")
            else:
                factor_conversion = self.conversiones_posibles[idx]["factor"]
                # Actualizar el inventario disponible, mínimo sugerido y costo
                self.inventario_disponible *= factor_conversion
                self.minimo_sugerido *= factor_conversion
                self.costo /= factor_conversion
                # Actualizar la unidad de medida
                self.unidad_medida = unidad_final
                print(f"El reactivo {self.nombre} se ha convertido a la unidad {unidad_final}")

    # Función para revisar si está caducado a la fecha de un experimento
    def esta_caducado(self, fecha_experimento):
        # Chequear si este producto puede caducar
        if not self.fecha_caducidad:
            print(f"El reactivo {self.nombre} no tiene fecha de caducidad.")
            return False
        # Convertir las fechas a objetos datetime y comparar
        fecha_caducidad = datetime.datetime.strptime(self.fecha_caducidad, "%Y-%m-%d")
        fecha_experimento = datetime.datetime.strptime(fecha_experimento, "%Y-%m-%d")
        return fecha_experimento > fecha_caducidad

    # Chequear si hay disponibilidad
    def hay_disponibilidad(self, cantidad):
        return self.inventario_disponible > cantidad

    # Agregar cantidad al inventario
    def agregar_inventario(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a agregar debe ser mayor a 0.")
        else:
            self.inventario_disponible += cantidad

    # Restar cantidad al inventario
    def restar_inventario(self, cantidad):
        # Chequear si hay suficiente cantidad en el inventario
        if cantidad > self.inventario_disponible:
            print(f"No hay suficiente reactivo {self.nombre} en el inventario.")
        else:
            self.inventario_disponible -= cantidad
            if self.inventario_disponible < self.minimo_sugerido:
                print(f"El reactivo {self.nombre} está por debajo del mínimo sugerido. Recomendamos reponerlo.")

    # Agregar uso al reactivo
    def agregar_uso(self):
        self.veces_usado += 1

    # Agregar vez que se ha vencido
    def agregar_vencimiento(self):
        self.veces_vencido += 1
