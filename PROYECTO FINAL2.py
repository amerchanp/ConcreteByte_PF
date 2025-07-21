import random
import time

palabras = {
    "ingenieria_civil": [
        "topografia", "estructura", "cimentacion", "puente", "hormigon", "drenaje", "rasante",
        "curva", "nivelacion", "peralte", "acero", "columna", "viga", "plano", "obra",
        "infraestructura", "desague", "carretera", "losas", "trazo", "corte", "relleno",
        "muestreo", "sismo", "resistencia", "compresion", "flexion", "concreto", "geotecnia",
        "asfalto", "calculo", "andamio", "enrase", "mamposteria", "albanileria", "dilatacion",
        "curvimetro", "longitud", "altimetria", "pendiente"
    ],
    "musica": [
        "armonia", "melodia", "compas", "tempo", "allegro", "piano", "forte", "partitura",
        "solfeo", "acorde", "intervalo", "notacion", "coro", "ensayo", "modulacion", "voz", 
        "baritono", "contrapunto", "entonacion", "pentagrama", "letra", "instrumento", "ritmo",
        "afinacion", "repertorio", "escala", "armonico", "pulso", "dinamica", "expresion",
        "timbre", "claves", "mezcla", "grabacion", "resonancia", "frecuencia", "entonar",
        "crescendo", "ligadura", "contralto"
    ],
    "programacion": [
        "funcion", "variable", "condicional", "bucle", "lista", "diccionario", "algoritmo",
        "entrada", "salida", "iteracion", "parametro", "argumento", "retorno", "logica",
        "depuracion", "bug", "ide", "sintaxis", "tipo", "indice", "concatenacion", "string",
        "arreglo", "booleano", "entero", "flotante", "comentario", "importar", "modulo",
        "libreria", "codigo", "script", "consola", "funcional", "debugger", "condicion",
        "comparacion", "operador", "buclewhile"
    ]
}

print("PROYECTO FINAL DE PROGRAMACIÓN DE COMPUTADORES")
print()
print("PRESENTADO POR:\nALEJANDRO MERCHAN\nSANTIAGO BARRIGA")
print()
print("DOCENTE: FELIPE ROLDAN")
print()
print("SOPA DE LETRAS INTERACTIVA")
print()

# ----------- Configurar dificultad -----------
while True:
    dificultad = input("Hola unaleño, elige una dificultad \nfacil: Aburridoooo 12x12\nmedio: Meh 20x20\ndificil: Uy quietoo 26x26\n \nSELECCIONEEE AQUÍ:").lower()
    if dificultad == "facil":
        tam = 12
        cantidad = 5
        break
    elif dificultad == "medio":
        tam = 20
        cantidad = 7
        break
    elif dificultad == "dificil":
        tam = 26
        cantidad = 8
        break
    else:
        print("eh, que cosita. Que elija una de estas: facil, medio o dificil")

# ----------- Seleccionar palabras -----------
tema = random.choice(list(palabras.keys()))
lista_palabras = random.sample(palabras[tema], cantidad)

# ----------- Crear cuadricula vacía -----------
cuadricula = []
for _ in range(tam):
    fila = []
    for _ in range(tam):
        fila.append(" ")
    cuadricula.append(fila)

# ----------- Insertar palabras -----------
def insertar_palabra(palabra):
    direccion = random.choice(["horizontal", "vertical", "inversa_horizontal", "inversa_vertical"])
    largo = len(palabra)

    for _ in range(400):
        if direccion == "horizontal":
            fila = random.randint(0, tam - 1)
            col = random.randint(0, tam - largo)
            todo_chill = True
            for k in range(largo):
                if cuadricula[fila][col + k] not in (" ", palabra[k]):
                    todo_chill = False
                    break
            if todo_chill:
                for k in range(largo):
                    cuadricula[fila][col + k] = palabra[k]
                return

        elif direccion == "vertical":
            fila = random.randint(0, tam - largo)
            col = random.randint(0, tam - 1)
            todo_chill = True
            for k in range(largo):
                if cuadricula[fila + k][col] not in (" ", palabra[k]):
                    todo_chill = False
                    break
            if todo_chill:
                for k in range(largo):
                    cuadricula[fila + k][col] = palabra[k]
                return

        elif direccion == "inversa_horizontal":
            fila = random.randint(0, tam - 1)
            col = random.randint(largo - 1, tam - 1)
            todo_chill = True
            for k in range(largo):
                if cuadricula[fila][col - k] not in (" ", palabra[k]):
                    todo_chill = False
                    break
            if todo_chill:
                for k in range(largo):
                    cuadricula[fila][col - k] = palabra[k]
                return

        elif direccion == "inversa_vertical":
            fila = random.randint(largo - 1, tam - 1)
            col = random.randint(0, tam - 1)
            todo_chill = True
            for k in range(largo):
                if cuadricula[fila - k][col] not in (" ", palabra[k]):
                    todo_chill = False
                    break
            if todo_chill:
                for k in range(largo):
                    cuadricula[fila - k][col] = palabra[k]
                return

for palabra in lista_palabras:
    insertar_palabra(palabra)

# ----------- Rellenar con letras aleatorias -----------
letras = "abcdefghijklmnñopqrstuvwxyz"
for i in range(tam):
    for j in range(tam):
        if cuadricula[i][j] == " ":
            cuadricula[i][j] = random.choice(letras)

# ----------- mostrar cuadricula -----------
for fila in cuadricula:
    print(" ".join(fila))

# ----------- Iniciar juego -----------
encontradas = []
inicio = time.time()

print("\nBusque estas palabras, rapido, pa que se gane un aplauso:")
print(", ".join(lista_palabras))
print("Recuerda que la primera fila y columna es 0, no 1. -no sé, así es python-")
print()

# ----------- Bucle de juego -----------
while len(encontradas) < len(lista_palabras):
    print("\nEscriba 'finalizar' si se aburrió o no le gustó y se va a hacer otra cosa, bendiciones")
    
    fila = input("Fila inicial: ")
    if fila == "finalizar":
        print("Chaooooooooooooooooooooooooo.")
        break
    while not fila.isdigit() or not (0 <= int(fila) < tam):
        fila = input("Fila inválida. Intenta de nuevo, ome: ")
        if fila == "finalizar":
            print("chaoooooooooooooooooooo.")
            break
    if fila == "finalizar":
        break
    fila = int(fila)

    col = input("Columna inicial: ")
    if col == "finalizar":
        print("chaooooooooooooooooooooooooooo.")
        break
    while not col.isdigit() or not (0 <= int(col) < tam):
        col = input("Columna inválida. Intenta de nuevo, que cosa de verdad: ")
        if col == "finalizar":
            print("chaoooooooooooooooooooooooooo.")
            break
    if col == "finalizar":
        break
    col = int(col)

    direccion = input("Dirección (arriba, abajo, izquierda, derecha): ").lower()
    while direccion not in ["arriba", "abajo", "izquierda", "derecha", "finalizar"]:
        direccion = input("Dirección inválida. Intenta de nuevo: ").lower()
    if direccion == "finalizar":
        print("ChaoooooooooooOooOOoo.")
        break

    palabra_formada = ""
    for i in range(tam):
        if direccion == "abajo":
            if fila + i >= tam:
                break
            letra = cuadricula[fila + i][col]
        elif direccion == "arriba":
            if fila - i < 0:
                break
            letra = cuadricula[fila - i][col]
        elif direccion == "derecha":
            if col + i >= tam:
                break
            letra = cuadricula[fila][col + i]
        elif direccion == "izquierda":
            if col - i < 0:
                break
            letra = cuadricula[fila][col - i]
        else:
            print("Dirección inválida.")
            break

        palabra_formada += letra

        if palabra_formada in lista_palabras and palabra_formada not in encontradas:
            encontradas.append(palabra_formada)
            print(f"¡ESA VAINA! Encontraste: {palabra_formada}")
            print("\nCUADRÍCULA ACTUAL:")
            for fila in cuadricula:
                print(" ".join(fila))
            break
    else:
        print("No se encontró ninguna palabra, jajajaj.")
        print("\nCUADRÍCULA ACTUAL:")
        for fila_actual in cuadricula:
            print(" ".join(fila_actual))

    print("Palabras que faltan, ya casiii:")
    for p in lista_palabras:
        if p not in encontradas:
            print("-", p)


# ----------- Fin del juego -----------
if len(encontradas) == len(lista_palabras):
    fin = time.time()
    tiempo_total = int(fin - inicio)
    minutos = tiempo_total // 60
    segundos = tiempo_total % 60
    print(f"\n¡Felicidades! Encontraste todas las palabras, se ganó un aplauso, uno solo.")
    print(f"Tiempo total: {minutos} minuto(s) y {segundos} segundo(s), me río de janeiro.")
