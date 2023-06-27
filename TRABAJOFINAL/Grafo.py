import os
import pandas as pd
import networkx as nx

class Nodo:
    def __init__(self, id, country, port_name, type, area_local, area_global):
        self.id = id
        self.country = country
        self.port_name = port_name
        self.type = type
        self.area_local = area_local
        self.area_global = area_global

class Conexion:
    def __init__(self, id_connection, id_port_a, country_a, port, distance, port_fee, id_port_b, country_b, port_b):
        self.id_connection = id_connection
        self.id_port_a = id_port_a
        self.country_a = country_a
        self.port = port
        self.distance = distance
        self.port_fee = port_fee
        self.id_port_b = id_port_b
        self.country_b = country_b
        self.port_b = port_b

class Grafo:
    def __init__(self):
        self.nodos = []
        self.conexiones = []

    def agregar_nodo(self, id, country, port_name, type, area_local, area_global):
        nodo = Nodo(id, country, port_name, type, area_local, area_global)
        self.nodos.append(nodo)

    def agregar_conexion(self, id_connection, id_port_a, country_a, port, distance, port_fee, id_port_b, country_b, port_b):
        conexion = Conexion(id_connection, id_port_a, country_a, port, distance, port_fee, id_port_b, country_b, port_b)
        self.conexiones.append(conexion)

    def obtener_nodo_por_id(self, id):
        for nodo in self.nodos:
            if nodo.id == id:
                return nodo
        return None

    def obtener_conexiones_de_nodo(self, id):
        conexiones = []
        for conexion in self.conexiones:
            if conexion.id_port_a == id:
                conexiones.append(conexion)
        return conexiones
    
    def construir_grafo(self):
        G = nx.DiGraph()  # Cambio a un grafo dirigido
        info_grafo = {'nodes': {}, 'edges': {}}

        for nodo in self.nodos:
            G.add_node(nodo.port_name)
            info_grafo['nodes'][nodo.port_name] = {
                'country': nodo.country,
                'area_local': nodo.area_local,
                'area_global': nodo.area_global
            }

        for conexion in self.conexiones:
            G.add_edge(conexion.port, conexion.port_b)
            info_grafo['edges'][(conexion.port, conexion.port_b)] = {
                'distance': conexion.distance,
                'port_fee': conexion.port_fee
            }

        return G, info_grafo

# Obtén la ruta del directorio actual del script
dir_actual = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta relativa del archivo Excel
ruta_excel = os.path.join(dir_actual, 'Port_Data.xlsx')

# Lee el archivo Excel
df = pd.read_excel(ruta_excel, sheet_name='Port_Data')
df_connections = pd.read_excel(ruta_excel, sheet_name='Connections')

# Crea una instancia del grafo
grafo = Grafo()

# Itera sobre los nodos
for i in range(len(df)):
    id_nodo = df['Id'][i]
    country = df['Country'][i]
    port_name = df['Port Name'][i]
    tipo = df['Type'][i]
    area_local = df['Area Local'][i]
    area_global = df['Area Global'][i]

    grafo.agregar_nodo(id_nodo, country, port_name, tipo, area_local, area_global)

# Itera sobre las conexiones
for i in range(len(df_connections)):
    id_connection = df_connections['ID_Connection'][i]
    id_port_a = df_connections['Id_Port_A'][i]
    country_a = df_connections['Country'][i]
    port = df_connections['Port'][i]
    distance = df_connections['Distance (nm)'][i]
    port_fee = df_connections['Port Fee($)/h'][i]
    id_port_b = df_connections['Id_Port_B'][i]
    country_b = df_connections['Country_B'][i]
    port_b = df_connections['Port_B'][i]

    grafo.agregar_conexion(id_connection, id_port_a, country_a, port, distance, port_fee, id_port_b, country_b, port_b)

