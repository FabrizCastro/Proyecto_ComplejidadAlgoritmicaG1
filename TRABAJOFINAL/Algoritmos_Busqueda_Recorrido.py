import networkx as nx
import matplotlib.pyplot as plt
from Grafo import *

G, info_grafo = grafo.construir_grafo()

def realizar_recorrido_dfs(source):
    dfs_nodes = list(nx.dfs_tree(G, source=source))
    print("\nRecorrido en profundidad (DFS):")
    for node in dfs_nodes:
        print(node)

    # Crear un nuevo grafo para visualizar el recorrido DFS
    dfs_graph = nx.DiGraph()
    for i in range(len(dfs_nodes) - 1):
        u = dfs_nodes[i]
        v = dfs_nodes[i+1]
        dfs_graph.add_edge(u, v)

    # Dibujar el grafo
    pos = nx.spring_layout(dfs_graph)
    nx.draw_networkx(dfs_graph, pos, with_labels=True, node_color='lightblue', edge_color='red', arrows=True)

    plt.show()


def realizar_recorrido_bfs(source):
    bfs_nodes = list(nx.bfs_tree(G, source=source))
    print("\nRecorrido en anchura (BFS):")
    for node in bfs_nodes:
        print(node)

    # Crear un nuevo grafo para visualizar el recorrido BFS
    bfs_graph = nx.DiGraph()
    for i in range(len(bfs_nodes) - 1):
        u = bfs_nodes[i]
        v = bfs_nodes[i+1]
        bfs_graph.add_edge(u, v)

    # Dibujar el grafo
    pos = nx.spring_layout(bfs_graph)
    nx.draw_networkx(bfs_graph, pos, with_labels=True, node_color='lightblue', edge_color='red', arrows=True)

    plt.show()

def buscar_nodo_por_nombre(port_name):
    for nodo in grafo.nodos:
        if nodo.port_name == port_name:
            return nodo
    return None

def calcular_peso(u, v, peso_distancia, peso_port_fee):
    # Buscar la conexión correspondiente
    distance = info_grafo['edges'][(u, v)]['distance']
    port_fee = info_grafo['edges'][(u, v)]['port_fee']

    return peso_distancia * distance + peso_port_fee * port_fee


def camino_mas_corto_bellman_ford(source, target, peso_distancia, peso_port_fee):
    distances = {nodo: float('inf') for nodo in info_grafo['nodes']}
    distances[source] = 0

    predecessors = {nodo: None for nodo in info_grafo['nodes']}

    for _ in range(len(info_grafo['nodes']) - 1):
        for u, v in info_grafo['edges']:
            weight = calcular_peso(u, v, peso_distancia, peso_port_fee)
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u

    shortest_path = []
    node = target
    while node is not None:
        shortest_path.insert(0, node)
        node = predecessors[node]

    shortest_cost = distances[target]

    # Crear un nuevo grafo para visualizar el camino más corto
    shortest_path_graph = nx.DiGraph()
    for i in range(len(shortest_path) - 1):
        u = shortest_path[i]
        v = shortest_path[i+1]
        distance = info_grafo['edges'][(u, v)]['distance']
        port_fee = info_grafo['edges'][(u, v)]['port_fee']
        shortest_path_graph.add_edge(u, v, distance=distance, port_fee=port_fee)

    # Dibujar el grafo
    pos = nx.spring_layout(shortest_path_graph)
    nx.draw_networkx(shortest_path_graph, pos, with_labels=True, node_color='lightblue', edge_color='red', arrows=True)
    edge_labels = nx.get_edge_attributes(shortest_path_graph, 'distance')
    nx.draw_networkx_edge_labels(shortest_path_graph, pos, edge_labels=edge_labels)

    plt.show()

    return shortest_path, shortest_cost




def realizar_ordenamiento_topologico():
    # Realizar el ordenamiento topológico
    
    topological_order = list(nx.topological_sort(G))

    # Ordenar los nodos manualmente basándonos en el dato 'area_global' de cada nodo
    topological_order.sort(key=lambda node_name: info_grafo['nodes'].get(node_name, {}).get('area_global', ''))

    # Crear un subgrafo con los nodos en el orden topológico
    ordered_graph = G.subgraph(topological_order)

    # Obtener la posición de los nodos en el grafo utilizando el algoritmo 'spring_layout'
    pos = nx.spring_layout(ordered_graph, seed=42)

    # Crear una lista de colores para los nodos basada en el 'area_global'
    node_colors = [info_grafo['nodes'].get(node_name, {}).get('area_global', '') for node_name in ordered_graph.nodes()]

    # Definir la paleta de colores para cada área global
    color_palette = {
        'América del Sur': 'blue',
        'América del Norte': 'red',
        'Europa': 'green',
        'América Central': 'orange',
        'Asia': 'purple',
        'Oceanía': 'brown',
        'África': 'pink'
    }

    # Asignar colores a los nodos según el área global
    node_colors = [color_palette.get(area, 'white') for area in node_colors]

    # Dibujar el grafo ordenado con colores basados en el área global de los nodos
    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(
        ordered_graph,
        pos,
        node_size=500,
        node_color=node_colors,
        alpha=0.8,
        linewidths=2,
        edgecolors='black'
    )
    nx.draw_networkx_edges(ordered_graph, pos, edge_color='black', alpha=0.5, arrows=True)
    nx.draw_networkx_labels(ordered_graph, pos, font_size=10, font_color='white')

    # Crear una leyenda para los colores
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', label=area, markerfacecolor=color, markersize=10)
        for area, color in color_palette.items()
    ]
    plt.legend(handles=legend_elements, loc='upper right')

    # Eliminar los ejes
    plt.axis('off')

    # Mostrar el grafo ordenado
    plt.show()

    return topological_order

