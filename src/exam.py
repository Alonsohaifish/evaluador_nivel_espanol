from src.grammar import evaluacion_gramatical, cargar_preguntas
from src.writing import evaluar_writing

def examen_completo():

    preguntas = cargar_preguntas("data/preguntas.json")

    print("\n=== Examen de Español ===\n")

    grammar_score = evaluacion_gramatical(preguntas)
    writing_score = evaluar_writing()

    total = grammar_score + writing_score

    print("\n=== Resultados ===")
    print(f"Gramática: {grammar_score}")
    print(f"Writing: {writing_score}")
    print(f"Total: {total}/100")

    if total >= 85:
        nivel = "C1"
    elif total >= 70:
        nivel = "B2"
    elif total >= 50:
        nivel = "B1"
    else:
        nivel = "A2"

    print(f"Nivel estimado: {nivel}")