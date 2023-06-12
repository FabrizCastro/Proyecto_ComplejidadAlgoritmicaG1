from Nodos import *
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = []
        self.connections = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_connection(self, connection):
        self.connections.append(connection)

# Crear la lista de adyacencia
adjacency_list = {}

# Iterar sobre las conexiones y construir la lista de adyacencia
for connection in connections:
    port_a = connection.port_a
    port_b = connection.port_b
    port_fee = connection.port_fee
    
    # Agregar Port B a la lista de adyacencia de Port A
    if port_a in adjacency_list:
        adjacency_list[port_a].append((port_b, port_fee))
    else:
        adjacency_list[port_a] = [(port_b, port_fee)]

# Crear un objeto de tipo DiGraph (grafo dirigido)
graph = nx.DiGraph()

# Agregar los nodos y las aristas al grafo
for port_a, ports_b in adjacency_list.items():
    graph.add_node(port_a)
    for port_b, port_fee in ports_b:
        graph.add_edge(port_a, port_b, weight=port_fee)

# Obtener la posición de los nodos en el grafo
pos = nx.spring_layout(graph)

# Dibujar los nodos y las aristas
nx.draw(graph, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, edge_color='gray', arrows=True)

# Mostrar el grafo
plt.show()