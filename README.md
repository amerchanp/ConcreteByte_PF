# SOPA DE LETRAS
## ConcreteByte
### Alejandro Merchan
### Santiago Barriga

Diseñaremos una sopa de letras con tamaño de 10x10 casillas.

Empezaremos importando RANDOM para ayudarnos de la herramienta de aleatorio, defininedo las letras que irán en los espacios sin palabras, una constante para el tamaño de la sopa de letras y las palabras a ocultar.

```
import random

# Dimensiones de la sopa
TAMANO = 10

# Letras disponibles para rellenar
LETRAS = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Palabras que se van a ocultar
palabras = ["GATO", "CASA", "LUNA", "SOL", "PERRO"]

```

Luego, creamos una matriz llamada sopa, la cual se irá rellenando con herramientas que mas adelante en el código estableceremos, recorreremos la cantidad definida en TAMANO y se le agregará un . (al principio vacía pero se va a ir llenando) para al final agregarlas a la matriz.
En la función lo que hacemos es covertir las filas en strings, separando cada letra con un espacio.

```
# Crear una cuadrícula vacía (lista de listas)
sopa = []
for i in range(TAMANO):
    fila = []
    for j in range(TAMANO):
        fila.append(".")  # Inicialmente vacía
    sopa.append(fila)

# Función para imprimir la sopa
def imprimir_sopa(sopa):
    for fila in sopa:
        print(" ".join(fila))

```

```mermaid
flowchart TD
    A[Inicio] --> B[Crear matriz vacía]
    B --> C[Recorrer filas (i en range(TAMANO))]
    C --> D[Crear fila vacía]
    D --> E[Recorrer columnas (j en range(TAMANO))]
    E --> F[Agregar "." a la fila]
    F --> G[Agregar fila completa a la matriz]
    G --> H[¿Quedan filas por recorrer?]
    H -- Sí --> C
    H -- No --> I[Imprimir sopa]
    I --> J[Fin]
```

Ese es el avance inicial de proyecto, muchas gracias.
