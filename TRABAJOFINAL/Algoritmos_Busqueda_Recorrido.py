import networkx as nx
from Grafo import *
from Nodos import nodes, connections

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