"""
Árbol de Expansión Mínima – Algoritmo de Prim (versión gráfica sencilla)

Requisitos:
    • Python 3.x con la biblioteca estándar (tkinter ya incluida).

Cómo usar:
    1. Guarda este archivo como prim_simulador.py
    2. Ejecuta:  python prim_simulador.py
    3. Pulsa «Paso» para ir construyendo el MST. «Reiniciar» vuelve a empezar.
"""

import tkinter as tk
from tkinter import messagebox

# ----------- Datos del grafo (puedes cambiarlos) -----------
INF = float('inf')
# Matriz de adyacencia (5 × 5 en este ejemplo)
G = [
    [0,   2,  INF, 6,   INF],
    [2,   0,  3,   8,   5  ],
    [INF, 3,  0,   INF, 7  ],
    [6,   8,  INF, 0,   9  ],
    [INF, 5,  7,   9,   0  ],
]
N = len(G)

# Coordenadas para dibujar nodos en el canvas
POS = [
    ( 60, 160),   # 0
    (180,  40),   # 1
    (300, 160),   # 2
    (120, 280),   # 3
    (240, 280),   # 4
]

# ----------- Lógica del algoritmo de Prim -----------
class PrimSim:
    def __init__(self, canvas):
        self.cv = canvas
        self.reset()

    def reset(self):
        # Estructuras de Prim
        self.visited = [False] * N
        self.parent  = [-1]    * N
        self.key     = [INF]   * N
        self.key[0]  = 0       # Comenzamos en el nodo 0
        self.step_no = 0

        # Redibujar grafo inicial
        self._draw_base()
        self._update_canvas()

    def step(self):
        # Si todos los nodos ya están visitados, detenemos
        if all(self.visited):
            messagebox.showinfo("Finalizado", "Árbol mínimo completado.")
            return

        # Elegir el nodo no visitado con menor clave
        u = min(
            (i for i in range(N) if not self.visited[i]),
            key=lambda i: self.key[i],
            default=None
        )

        if u is None:  # Grafo no conectado
            messagebox.showwarning("Aviso", "No hay más nodos alcanzables.")
            return

        self.visited[u] = True  # Añadir al MST

        # Actualizar claves de sus vecinos
        for v in range(N):
            if 0 < G[u][v] < INF and not self.visited[v] and G[u][v] < self.key[v]:
                self.key[v]    = G[u][v]
                self.parent[v] = u

        self.step_no += 1
        self._update_canvas()

    # ----------- Dibujado -----------
    def _draw_base(self):
        """Dibuja nodos y pesos una sola vez (aristas grises)."""
        self.cv.delete("all")
        # Aristas
        for i in range(N):
            x1, y1 = POS[i]
            for j in range(i + 1, N):
                if G[i][j] < INF:
                    x2, y2 = POS[j]
                    self.cv.create_line(x1, y1, x2, y2, fill="lightgray", width=2)
                    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                    self.cv.create_text(mx, my, text=str(G[i][j]), font=("Arial", 9))
        # Nodos (círculos azules vacíos)
        for i, (x, y) in enumerate(POS):
            self.cv.create_oval(x-18, y-18, x+18, y+18, fill="white", outline="black", width=2, tags=f"node{i}")
            self.cv.create_text(x, y, text=str(i), font=("Arial", 12, "bold"), tags=f"label{i}")

    def _update_canvas(self):
        """Colorea nodos visitados y dibuja las aristas seleccionadas."""
        # Aristas seleccionadas: azul fuerte
        for v in range(1, N):
            u = self.parent[v]
            if u != -1:
                self._draw_edge(u, v, color="dodgerblue", width=4)

        # Nodos: verde si visitado
        for i in range(N):
            fill = "palegreen" if self.visited[i] else "white"
            self.cv.itemconfig(f"node{i}", fill=fill)

        # Texto de estado
        self.cv.delete("status")
        status = f"Paso {self.step_no} – Claves: {self.key}"
        self.cv.create_text(240, 10, text=status, font=("Arial", 10), tags="status")

    def _draw_edge(self, u, v, color, width):
        x1, y1 = POS[u]
        x2, y2 = POS[v]
        self.cv.create_line(x1, y1, x2, y2, fill=color, width=width)

# ----------- Crear interfaz -----------
def main():
    root = tk.Tk()
    root.title("Simulador gráfico de Prim (simple)")

    canvas = tk.Canvas(root, width=360, height=330, bg="white")
    canvas.pack(padx=10, pady=10)

    sim = PrimSim(canvas)

    controls = tk.Frame(root)
    controls.pack(pady=5)

    tk.Button(controls, text="Paso",     command=sim.step).pack(side="left", padx=5)
    tk.Button(controls, text="Reiniciar", command=sim.reset).pack(side="left", padx=5)
    tk.Button(controls, text="Salir",     command=root.destroy).pack(side="left", padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
