import os
import pandas as pd

class Node:
    def __init__(self, id, country, port_name, type, area_local, area_global):
        self.id = id
        self.country = country
        self.port_name = port_name
        self.type = type
        self.area_local = area_local
        self.area_global = area_global

class Connection:
    def __init__(self, id_connection, port_a, country_a, port_fee, port_b, country_b, port_b_name):
        self.id_connection = id_connection
        self.port_a = port_a
        self.country_a = country_a
        self.port_fee = port_fee
        self.port_b = port_b
        self.country_b = country_b
        self.port_b_name = port_b_name


# Obtén la ruta del directorio actual del script
dir_actual = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta relativa del archivo Excel
ruta_excel = os.path.join(dir_actual, 'Port_Data_v3.xlsx')

# Lee el archivo Excel
df = pd.read_excel(ruta_excel, sheet_name='Port_Data')
df_connections = pd.read_excel(ruta_excel, sheet_name='Connections')

# Accede a las columnas de los nodos
id_columna = df['Id']
country_columna = df['Country']
port_name_columna = df['Port Name']
type_columna = df['Type']
area_local_columna = df['Area Local']
area_global_columna = df['Area Global']

# Itera sobre los nodos
nodes = []
for i in range(len(df)):
    id_nodo = id_columna[i]
    country = country_columna[i]
    port_name = port_name_columna[i]
    tipo = type_columna[i]
    area_local = area_local_columna[i]
    area_global = area_global_columna[i]
    
    node = Node(id_nodo, country, port_name, tipo, area_local, area_global)
    nodes.append(node)


# Itera sobre los nodos
for node in nodes:
    id_nodo = node.id
    country = node.country
    port_name = node.port_name
    tipo = node.type
    area_local = node.area_local
    area_global = node.area_global
    
    # Haz algo con cada nodo
    #print(f"Id: {id_nodo}, Country: {country}, Port Name: {port_name}, Type: {tipo}, Area Local: {area_local}, Area Global: {area_global}")

# Accede a las columnas de las conexiones
id_connection_columna = df_connections['ID_Connection']
port_a_columna = df_connections['Id_Port_A']
country_a_columna = df_connections['Country']
port_fee_columna = df_connections['Port Fee($)/h']
port_b_columna = df_connections['Id_Port_B']
country_b_columna = df_connections['Country_B']
port_b_name_columna = df_connections['Port_B']

# Crear una instancia de la clase Connection para cada conexión en el DataFrame
connections = []
for i in range(len(df_connections)):
    id_connection = id_connection_columna[i]
    port_a = port_a_columna[i]
    country_a = country_a_columna[i]
    port_fee = port_fee_columna[i]
    port_b = port_b_columna[i]
    country_b = country_b_columna[i]
    port_b_name = port_b_name_columna[i]
    
    connection = Connection(id_connection, port_a, country_a, port_fee, port_b, country_b, port_b_name)
    connections.append(connection)

# Itera sobre las conexiones
for connection in connections:
    id_connection = connection.id_connection
    port_a = connection.port_a
    country_a = connection.country_a
    port_fee = connection.port_fee
    port_b = connection.port_b
    country_b = connection.country_b
    port_b_name = connection.port_b_name
    
    # Haz algo con cada conexión
    #print(f"ID Connection: {id_connection}, Port A: {port_a}, Country A: {country_a}, Port Fee: {port_fee}, Port B: {port_b}, Country B: {country_b}, Port B Name: {port_b_name}")