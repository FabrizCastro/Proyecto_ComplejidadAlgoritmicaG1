import networkx as nx
from Grafo import *
from Nodos import nodes, connections
from itertools import cycle

# Realizar el recorrido en anchura (BFS)
def realizar_recorrido_bfs(source):
    bfs_nodes = list(nx.bfs_tree(graph, source=source))
    print("\nRecorrido en anchura (BFS):")
    for node in bfs_nodes:
        print(node)

# Realizar recorrido en profundidad (DFS)
def realizar_recorrido_dfs(source):
    dfs_nodes = list(nx.dfs_tree(graph,source=source))
    print("\nRecorrido en profundidad (DFS):")
    for node in dfs_nodes:
        print(node)

# Calcular el camino más corto usando el algoritmo de Dijkstra
def calcular_camino_mas_corto(source, target):
    shortest_path = nx.dijkstra_path(graph, source=source, target=target)
    print("\nCamino más eficaz:")
    print(shortest_path)

def realizar_ordenamiento_topologico():
    # Realizar el ordenamiento topológico
    topological_order = list(nx.topological_sort(graph))

    # Ordenar los nodos manualmente basándonos en el dato 'area_local' de cada nodo
    topological_order.sort(key=lambda node_name: next((node.area_global for node in nodes if node.port_name == node_name), ''))

    # Crear un subgrafo con los nodos en el orden topológico
    ordered_graph = graph.subgraph(topological_order)

    # Obtener la posición de los nodos en el grafo utilizando el algoritmo 'spring_layout'
    pos = nx.spring_layout(ordered_graph, seed=42)

    # Crear una paleta de colores para las áreas globales
    color_palette = {
        'América del Sur': 'blue',
        'América del Norte': 'red',
        'Europa': 'green',
        'América Central': 'orange',
        'Asia': 'purple',
        'Oceanía': 'yellow',
        'África': 'brown'
    }

    # Obtener el área global de cada nodo y asignarle un color correspondiente
    node_colors = [color_palette[next((node.area_global for node in nodes if node.port_name == node_name), '')] for node_name in ordered_graph.nodes()]

    # Dibujar los nodos y las aristas
    nx.draw_networkx_nodes(ordered_graph, pos, node_size=500, node_color=node_colors)
    nx.draw_networkx_labels(ordered_graph, pos, font_size=10)
    nx.draw_networkx_edges(ordered_graph, pos, alpha=0.5)

    # Mostrar el grafo
    plt.show()

    return ordered_graph
