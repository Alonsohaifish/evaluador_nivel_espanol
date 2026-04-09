import language_tool_python

tool = language_tool_python.LanguageTool('es')

def evaluar_writing():
    print("\n--- Sección de Writing ---")
    texto = input("Escribe sobre tu día, mínimo 10 palabras:\n")

    matches = tool.check(texto)
    errores = len(matches)

    palabras = len(texto.split())

    if palabras < 5:
        print("Texto demasiado corto.")
        return 0

    score = max(0, 30 - errores)

    print(f"Errores detectados: {errores}")
    return score