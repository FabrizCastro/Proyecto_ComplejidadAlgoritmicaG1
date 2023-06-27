import tkinter as tk
from Grafo import *
from Nodos import nodes, connections
from Algoritmos_Busqueda_Recorrido import *

class InterfazGrafica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interfaz de Grafos")
        self.configure(bg="#F5F5F5")  # Color de fondo

        # Agregar imagen de fondo
        self.configure(background='blue')
        self.geometry("1000x700")

        # Crear los elementos de la interfaz
        self.label = tk.Label(self, text="Bienvenido a la representación de la interconexión de los grandes puertos del mundo", bg="#F5F5F5", fg="#333333", font=("Berlin Sans FB", 16))
        self.label.pack(pady=10)

        self.button_mostrar_grafo = tk.Button(self, text="Mostrar Grafo", command=self.mostrar_grafo, bg="#DC3545", fg="#FFFFFF", font=("Berlin Sans FB", 14))
        self.button_mostrar_grafo.pack(pady=(40,20))

        self.frame_destino = tk.Frame(self, bg="#F5F5F5")
        self.frame_destino.pack(pady=(30, 50))

        self.label_destino = tk.Label(self.frame_destino, text="Seleccione el puerto de destino:", bg="#F5F5F5", fg="#333333", font=("Berlin Sans FB", 16))
        self.label_destino.grid(row=0, column=0, padx=10)

        self.dropdown_value = tk.StringVar(self)
        self.dropdown_value.set(nodes[0].port_name)  # Establecer el valor inicial del menú desplegable
        self.dropdown = tk.OptionMenu(self.frame_destino, self.dropdown_value, *[node.port_name for node in nodes])
        self.dropdown.config(width=20)
        self.dropdown.grid(row=0, column=1, padx=10)

        self.entry_firstinput = tk.Label(self.frame_destino, text="Inicio:", bg="#F5F5F5", fg="#333333", font=("Berlin Sans FB", 16))
        self.entry_firstinput.grid(row=1, column=0, padx=10, pady=10)

        self.entry = tk.Entry(self.frame_destino, font=("Berlin Sans FB", 14))
        self.entry.grid(row=1, column=1, padx=10, pady=10)

        self.label_input = tk.Label(self.frame_destino, text="Destino final:", bg="#F5F5F5", fg="#333333", font=("Berlin Sans FB", 16))
        self.label_input.grid(row=2, column=0, padx=10, pady=10)

        self.entry_destino = tk.Entry(self.frame_destino, font=("Berlin Sans FB", 14))
        self.entry_destino.grid(row=2, column=1, padx=10, pady=10)

        self.label_inputnotentry = tk.Label(self.frame_destino, text="Destino no deseado:", bg="#F5F5F5", fg="#333333", font=("Berlin Sans FB", 16))
        self.label_inputnotentry.grid(row=3, column=0, padx=10, pady=10)

        self.not_entry = tk.Entry(self.frame_destino, font=("Berlin Sans FB", 14))
        self.not_entry.grid(row=3, column=1, padx=10, pady=10)

        self.frame_funciones = tk.Frame(self, bg="#F5F5F5")
        self.frame_funciones.pack(pady=(10, 0))

        self.button_bfs = tk.Button(self.frame_funciones, text="Recorrido en anchura (BFS)", command=self.mostrar_recorrido_bfs, bg="#007BFF", fg="#FFFFFF", font=("Berlin Sans FB", 14))
        self.button_bfs.grid(row=0, column=0, pady=10)

        self.button_dfs = tk.Button(self.frame_funciones, text="Recorrido en profundidad (DFS)", command=self.mostrar_recorrido_dfs, bg="#FFC107", fg="#333333", font=("Berlin Sans FB", 14))
        self.button_dfs.grid(row=0, column=1, pady=10)

        self.button_shortest = tk.Button(self.frame_funciones, text="Mostrar camino más eficaz", command=self.mostrar_camino_mas_corto, bg="#28A745", fg="#FFFFFF", font=("Berlin Sans FB", 14))
        self.button_shortest.grid(row=0, column=2, pady=10)


        # Agregar los elementos para mostrar el resultado del camino más corto
        self.resultado_camino_label = tk.Label(self, text="", bg="#F5F5F5", fg="#333333", font=("Berlin Sans FB", 16))
        self.resultado_camino_label.pack(pady=10)

        self.resultado_costo_label = tk.Label(self, text="", bg="#F5F5F5", fg="#333333", font=("Berlin Sans FB", 16))
        self.resultado_costo_label.pack(pady=10)

    def mostrar_recorrido_bfs(self):
        nodo_inicial = self.entry.get()
        realizar_recorrido_bfs(nodo_inicial)

    def mostrar_recorrido_dfs(self):
        nodo_inicial = self.entry.get()
        realizar_recorrido_dfs(nodo_inicial)

    def mostrar_camino_mas_corto(self):
        name_inicial = self.entry.get()
        name_destino = self.entry_destino.get()
        name_nodeseado = self.not_entry.get()
        peso_distancia = 1  # Peso para la distancia
        peso_port_fee = 2  # Peso para el costo del puerto

        try:
            nodo_inicial = buscar_nodo_por_nombre(name_inicial)
            nodo_destino = buscar_nodo_por_nombre(name_destino)

            shortest_path, shortest_cost = camino_mas_corto_bellman_ford(name_inicial, name_destino, peso_distancia, peso_port_fee)

            if name_nodeseado in shortest_path:
                alternative_path_found = False

                # Buscar ruta alternativa
                for nodo_intermedio in shortest_path:
                    if nodo_intermedio != name_nodeseado:
                        alternative_path, alternative_cost = camino_mas_corto_bellman_ford(name_inicial, nodo_intermedio, peso_distancia, peso_port_fee)
                        alternative_path.extend(camino_mas_corto_bellman_ford(nodo_intermedio, name_destino, peso_distancia, peso_port_fee)[0][1:])
                        if not alternative_path_found and len(alternative_path) > 1:
                            alternative_path_found = True
                            self.resultado_camino_label.config(text="Mejor opción: " + ", ".join(alternative_path))
                            self.resultado_costo_label.config(text="Costo de la mejor opción: " + str(alternative_cost))
                            break

                if not alternative_path_found:
                    self.resultado_camino_label.config(text="No se encontró una ruta alternativa sin pasar por el nodo no deseado")
                    self.resultado_costo_label.config(text="")

            else:
                self.resultado_camino_label.config(text="Mejor opción: " + ", ".join(shortest_path))
                self.resultado_costo_label.config(text="Costo de la mejor opción: " + str(shortest_cost))

        except ValueError as e:
            print("Error:", str(e))

    def actualizar_destino(self, selected_node):
        self.nodo_destino = selected_node

    def mostrar_grafo(self):
        ordered_graph = realizar_ordenamiento_topologico()
        print(ordered_graph)
        # Realizar alguna acción con el grafo ordenado

if __name__ == "__main__":
    interfaz = InterfazGrafica()
    interfaz.mainloop()