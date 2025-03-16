import json
from laboratorio import Laboratorio
from estadísticas import AnalisisDeLaboratorio


# Constantes: rutas de los archivos JSON
REACTIVOS = "./api-proyecto/reactivos.json"
EXPERIMENTOS = "./api-proyecto/experimentos.json"
RECETAS = "./api-proyecto/recetas.json"


# Programa para ejecutar el laboratorio
def main():
    # Cargar los datos de los archivos JSON
    with open(REACTIVOS, "r") as file:
        reactivos = json.load(file)
    with open(EXPERIMENTOS, "r") as file:
        experimentos = json.load(file)
    with open(RECETAS, "r") as file:
        recetas = json.load(file)
    # Crear una instancia de Laboratorio
    lab = Laboratorio(reactivos, recetas, experimentos)
    # Ejecutar el programa
    for experimento in experimentos:
        lab.realizar_experimento(experimento["id"])
    # Guardar los resultados en un archivo JSON
    res = [exp.__dict__ for exp in lab.experimentos_realizados]
    with open("./api-proyecto/experimentos_realizados.json", "w") as file:
        json.dump(res, file, indent=4)
    # Imprimir los resultados
    analisis = AnalisisDeLaboratorio(lab)
    analisis.hacer_analisis()

# Ejecutar el programa
if __name__ == "__main__":
    main()
    
