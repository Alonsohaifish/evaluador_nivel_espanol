import json

def cargar_preguntas(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def mostrar_pregunta(p):
    print("\n" + p["pregunta"])
    for i, opcion in enumerate(p["opciones"]):
        print(f"{i+1}. {opcion}")

def obtener_respuesta():
    while True:
        try:
            return int(input("Tu respuesta: "))
        except ValueError:
            print("Ingresa un número válido.")

def evaluar_respuesta(pregunta, respuesta):
    if respuesta - 1 == pregunta["correcta"]:
        return 1
    return 0

def evaluacion_gramatical(preguntas):
    score = 0

    for p in preguntas:
        mostrar_pregunta(p)
        r = obtener_respuesta()
        score += evaluar_respuesta(p, r)

    return score