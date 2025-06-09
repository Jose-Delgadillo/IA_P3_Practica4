"""
Prácticas de Inteligencia Artificial
Algoritmos de Grafos: Árbol de Expansión Mínima (MST) - Algoritmo de Prim

Este código implementa una simulación en consola del algoritmo de Prim.
Se utiliza una matriz de adyacencia para representar un grafo no dirigido y ponderado.
En cada paso, se imprime el nodo agregado al árbol y el costo del borde seleccionado.

No usa librerías externas. Todo está en Python puro para máxima compatibilidad.
"""

INF = float('inf')

# Grafo de ejemplo (matriz de adyacencia)
grafo = [
    [0, 2, INF, 6, INF],
    [2, 0, 3, 8, 5],
    [INF, 3, 0, INF, 7],
    [6, 8, INF, 0, 9],
    [INF, 5, 7, 9, 0]
]

n = len(grafo)
visitado = [False] * n
padre = [-1] * n
clave = [INF] * n

# Comenzamos desde el nodo 0
clave[0] = 0

print("Paso a paso del algoritmo de Prim:\n")

for _ in range(n):
    # Encontrar el vértice no visitado con menor clave
    min_val = INF
    u = -1
    for v in range(n):
        if not visitado[v] and clave[v] < min_val:
            min_val = clave[v]
            u = v

    visitado[u] = True
    print(f"Agregado nodo {u} al árbol de expansión.")

    # Actualizar claves de los nodos adyacentes no visitados
    for v in range(n):
        if grafo[u][v] and not visitado[v] and grafo[u][v] < clave[v]:
            clave[v] = grafo[u][v]
            padre[v] = u
            print(f"   - Se actualiza nodo {v}: nuevo padre = {u}, nuevo costo = {grafo[u][v]}")

# Mostrar árbol resultante
print("\nÁrbol de expansión mínima resultante:")
costo_total = 0
for i in range(1, n):
    print(f"{padre[i]} -- {i} (peso: {grafo[i][padre[i]]})")
    costo_total += grafo[i][padre[i]]
print(f"Costo total del árbol: {costo_total}")
