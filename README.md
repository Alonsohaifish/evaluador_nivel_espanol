# Evaluador de nivel para español
---

## Objetivo

Crear un evaluador automático de nivel de español de distintas habilidades. 

---

## Descripción
Este proyecto evalúa el nivel (A1–C1) de un estudiante utilizando: 
- Preguntas de gramática de opción múltiple
- Corrección de un escrito a partir de NLP

## Features
- Automatic grammar scoring
- Writing correction using LanguageTool
- CEFR level classification

## Instalación
Clona el repositorio:

```bash
[git clone https://github.com/Alonsohaifish/extraccion-palabras-clave-español.git]
cd corrector_gramatical_espanol
```
Instala las dependencias:

```bash
pip install -r requirements.txt
```
## Estructura del proyecto
evaluador_nivel_espanol/
data/
  preguntas.json
src/
  init__.py
  grammar.py
  writing.py
  utils.py
  exam.py
main.py
requirements.txt
README.md
.gitignore


## Uso

Ejecuta el script principal:

```bash
python main.py
```
Esto:

1. Comienza con las preguntas del examen gramatical.
2. Realiza la prueba escrita.
3. Muestra el puntaje de las dos pruebas y el nivel del estudiante. 

##  Ejemplo del evaluador

### Entrada:

Texto detectado:  Hola, me llamo Alonso. Yo tenías 15 años y no tengo dinero

### Salida:

Corrección:  Hola, me llamo Alonso. Yo tenía 15 años y no tengo dinero.
Error: Posible falta de concordancia entre «Yo» y «tenías».
Sugerencias: ['tenía']
```


