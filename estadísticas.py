from helpers import ordernar_por_valor


class AnalisisDeLaboratorio:
    """
    Clase que se encarga de realizar el análisis de un laboratorio.
    Se necesita un laboratorio para realizar el análisis.
    """
    def __init__(self, laboratorio):
        self.laboratorio = laboratorio

    # Determinar los investigadores que más usan el laboratorio
    def hallar_investigadores_mas_frecuentes(self):
        # Calcular cuántas veces ha usado cada investigador el laboratorio
        investigadores = {}
        for experimento in self.laboratorio.experimentos_realizados:
            for investigador in experimento.personas:
                if investigador not in investigadores:
                    investigadores[investigador] = 1
                else:
                    investigadores[investigador] += 1
        # Ordenar los investigadores por la cantidad de veces que han usado el laboratorio
        investiagores = ordernar_por_valor(investigadores)
        # Determinar cuál es la cantidad máxima de usos
        max_usos = list(investigadores.values())[0]
        print(max_usos)
        # Retornar los investigadores con la cantidad máxima de usos
        return [nombre for nombre in investigadores if investigadores[nombre] == max_usos]

    # Determinar la receta más hecha y la menos hecha
    def hallar_recetas(self):
        # Calcular cuántas veces se ha hecho cada receta
        recetas = {}
        for experimento in self.laboratorio.experimentos_realizados:
            if experimento.receta_id not in recetas:
                recetas[experimento.receta_id] = 1
            else:
                recetas[experimento.receta_id] += 1
        # Ordenar las recetas por la cantidad de veces que se han hecho
        recetas = ordernar_por_valor(recetas)
        # Retornar la receta más hecha y la menos hecha
        return list(recetas.keys())[0], list(recetas.keys())[-1]

    # Determinar los 5 reactivos más usados
    def hallar_reactivos_mas_usados(self):
        # Calcular cuántas veces se ha usado cada reactivo
        reactivos = {x.nombre: x.veces_usado for x in self.laboratorio.reactivos}
        # Ordenar los reactivos por la cantidad de veces que se han usado
        reactivos = ordernar_por_valor(reactivos)
        # Retornar los 5 reactivos más usados
        return list(reactivos.keys())[:5]

    # Determinar los 3 reactivos con mayor desperdicicio
    def hallar_reactivos_con_mas_desperdicio(self):
        # Calcular cuánto desperdicio ha tenido cada reactivo
        reactivos = {}
        for reactivo in self.laboratorio.reactivos:
            if reactivo.id not in reactivos:
                    reactivos[reactivo.nombre] = reactivo.desperdicio
            else:
                reactivos[reactivo.nombre] += reactivo.desperdicio
        # Ordenar los reactivos por la cantidad de desperdicio
        reactivos = ordernar_por_valor(reactivos)
        # Retornar los 3 reactivos con mayor desperdicio
        return list(reactivos.keys())[:3]
    
    # Determinar los reactivos que más se vencen
    def hallar_reactivos_vencidos(self):
        # Calcular cuántas veces se ha vencido cada reactivo
        reactivos = {}
        for reactivo in self.laboratorio.reactivos:
            if reactivo.id not in reactivos:
                    reactivos[reactivo.nombre] = reactivo.veces_vencido
            else:
                reactivos[reactivo.nombre] += reactivo.veces_vencido
        # Ordenar los reactivos por la cantidad de veces que se han vencido
        reactivos = ordernar_por_valor(reactivos)
        # Determinar cuál es la cantidad máxima de vencimientos
        max_vencidos = list(reactivos.values())[0]
        # Chequear si no hay reactivos vencidos
        if max_vencidos == 0:
            return []
        # Retornar los investigadores con la cantidad máxima de usos
        return [nombre for nombre in reactivos if reactivos[nombre] == max_vencidos]

    # Determinar cuántas veces falló un experimento por falta de inventario
    def hallar_fallos_por_inventario(self):
        # Contar cuántos fallos ha habido por falta de inventario en total
        fallos = 0
        for experimento in self.laboratorio.experimentos_realizados:
            if experimento.fallo_por_inventario:
                fallos += 1
        return fallos

    # Realizar el análisis del laboratorio
    def hacer_analisis(self):
        print("Análisis del laboratorio:")
        # Investigadores que más han usado el laboratorio
        investigadores = self.hallar_investigadores_mas_frecuentes()
        print("Los investigadores que más han usado el laboratorio son:")
        for i, investigador in enumerate(investigadores):
            print(f"    {i + 1}. {investigador}")
        print("-------------------------")
        # Recetas más y menos usadas
        recetas = self.hallar_recetas()
        print(f"La receta más hecha es la {recetas[0]} y la menos hecha es la {recetas[1]}.")
        print("-------------------------")
        # Reactivos más usados
        reactivos_usados = self.hallar_reactivos_mas_usados()
        print("Los 5 reactivos más usados son:")
        for i, reactivo in enumerate(reactivos_usados):
            print(f"    {i + 1}. {reactivo}")
        print("-------------------------")
        # Reactivos con más desperdicio
        reactivos_desp = self.hallar_reactivos_con_mas_desperdicio()
        print("Los 3 reactivos con más desperdicio son:")
        for i, reactivo in enumerate(reactivos_desp):
            print(f"    {i + 1}. {reactivo}")
        print("-------------------------")
        # Reactivos que más se vencen
        reactivos_vencidos = self.hallar_reactivos_vencidos()
        if not reactivos_vencidos:
            print("Ningún reactivo estuvo caducado.")
        else:
            print("Los reactivos que más se vencen son:")
            for i, reactivo in enumerate(reactivos_vencidos):
                print(f"    {i + 1}. {reactivo}")
        print("-------------------------")
        # Fallos por inventario
        fallos = self.hallar_fallos_por_inventario()
        print(f"Se han presentado {fallos} fallos por falta de inventario.")
        print("-------------------------")
        print("Fin del análisis.")
