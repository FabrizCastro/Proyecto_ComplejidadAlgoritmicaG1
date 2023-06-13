import tkinter as tk
from Algoritmos_Busqueda_Recorrido import *
from tkinter import messagebox

class InterfazGrafica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interfaz de Grafos")
        self.configure(bg="#F5F5F5")  # Color de fondo
        
        # Agregar imagen de fondo
        self.configure(background='blue')
        self.geometry("700x700")
        
        # Crear los elementos de la interfaz
        self.label = tk.Label(self, text="Ingrese el nombre del nodo inicial:", bg="#F5F5F5", fg="#333333", font=("Arial", 16))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self, font=("Arial", 14))
        self.entry.pack(pady=10)
        
        self.button_bfs = tk.Button(self, text="Recorrido en anchura (BFS)", command=self.mostrar_recorrido_bfs, bg="#007BFF", fg="#FFFFFF", font=("Arial", 14))
        self.button_bfs.pack(pady=10)
        
        self.button_dfs = tk.Button(self, text="Recorrido en profundidad (DFS)", command=self.mostrar_recorrido_dfs, bg="#FFC107", fg="#333333", font=("Arial", 14))
        self.button_dfs.pack(pady=10)
        
        self.frame_destino = tk.Frame(self, bg="#F5F5F5")
        self.frame_destino.pack(pady=(80, 10), padx=10, anchor="w")  # Padding de 80 en la parte superior y 10 en la inferior
        
        self.label_destino = tk.Label(self.frame_destino, text="Seleccione el puerto de destino:", bg="#F5F5F5", fg="#333333", font=("Arial", 16))
        self.label_destino.grid(row=0, column=0, padx=10)

        self.dropdown_value = tk.StringVar(self)
        self.dropdown_value.set(nodes[0].port_name)  # Establecer el valor inicial del menú desplegable
        self.dropdown = tk.OptionMenu(self.frame_destino, self.dropdown_value, * [node.port_name for node in nodes])
        self.dropdown.config(width=20)
        self.dropdown.grid(row=0, column=1, padx=10)
        
        self.label_input = tk.Label(self.frame_destino, text="Destino final:", bg="#F5F5F5", fg="#333333", font=("Arial", 16))
        self.label_input.grid(row=1, column=0, padx=10, pady=10)
        
        self.entry_destino = tk.Entry(self.frame_destino, font=("Arial", 14))
        self.entry_destino.grid(row=1, column=1, padx=10, pady=10)
        
        self.button_shortest = tk.Button(self, text="Mostrar camino más eficaz", command=self.mostrar_camino_mas_corto, bg="#28A745", fg="#FFFFFF", font=("Arial", 14))
        self.button_shortest.pack(pady=10)
        
        self.button_mostrar_grafo = tk.Button(self, text="Mostrar Grafo", command=self.mostrar_grafo, bg="#DC3545", fg="#FFFFFF", font=("Arial", 14))
        self.button_mostrar_grafo.pack(pady=(100,20))

        self.nodo_destino = nodes[0].port_name

    def mostrar_recorrido_bfs(self):
        nodo_inicial = self.entry.get()
        realizar_recorrido_bfs(nodo_inicial)
    
    def mostrar_recorrido_dfs(self):
        nodo_inicial = self.entry.get()
        realizar_recorrido_dfs(nodo_inicial)
    
    def mostrar_camino_mas_corto(self):
        nodo_inicial = self.entry.get()
        nodo_destino = self.entry_destino.get()
        
        calcular_camino_mas_corto(nodo_inicial, nodo_destino)

    def actualizar_destino(self, selected_node):
        self.nodo_destino = selected_node

    def mostrar_grafo(self):
        plt.show()



if __name__ == "__main__":
    # Crear una instancia del grafo
    # Crear una instancia de la interfaz gráfica
    interfaz = InterfazGrafica()
    interfaz.mainloop()