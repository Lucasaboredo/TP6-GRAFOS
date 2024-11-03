from grafo import Graph
# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.

## RESOLUCION (14) ##

# Se crea el grafo no dirigido
grafo = Graph(dirigido=False) 

# Vertices con los ambientes de la casa
ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
             "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]

# Se añaden los vertices al grafo
for ambiente in ambientes:
    grafo.insert_vertice(ambiente)

# Se agregan las aristas (inicio,final) y el peso(metros)
grafo.insert_arista("cocina", "comedor", 5)
grafo.insert_arista("cocina", "terraza", 7)
grafo.insert_arista("cocina", "baño 1", 6)
grafo.insert_arista("comedor", "sala de estar", 4)
grafo.insert_arista("comedor", "patio", 8)
grafo.insert_arista("comedor", "cocina", 5)
grafo.insert_arista("cochera", "patio", 6)
grafo.insert_arista("cochera", "baño 1", 9)
grafo.insert_arista("cochera", "habitación 1", 10)
grafo.insert_arista("quincho", "terraza", 3)
grafo.insert_arista("quincho", "patio", 5)
grafo.insert_arista("quincho", "sala de estar", 6)
grafo.insert_arista("baño 1", "baño 2", 2)
grafo.insert_arista("baño 2", "habitación 1", 3)
grafo.insert_arista("baño 2", "sala de estar", 7)
grafo.insert_arista("habitación 1", "habitación 2", 4)
grafo.insert_arista("habitación 2", "terraza", 6)
grafo.insert_arista("sala de estar", "terraza", 5)
grafo.insert_arista("terraza", "patio", 4)

# Calculamos el arbol de expansion minima con Kruskal y lo imprimimos
arbol_expansion_minima = grafo.kruskal("cocina")
print("")
print("Árbol de expansión mínima:", arbol_expansion_minima)

# Sacamos los pesos del arbol anterior y hacemos la suma
distancia_total_mst = 0
for arista in arbol_expansion_minima[0].split(';'):
    if '-' in arista:
        # La distancia (peso en metros) esta al final de la sentencia
        peso = int(arista.split('-')[-1])
        distancia_total_mst += peso

print("")
print("Total de metros de cables necesarios para conectar todos los ambientes:", distancia_total_mst, "metros")


# Usamos el algoritmo de Dijkstra para determinar el camino mas corto de la "habitacion 1" hasta la "sala de estar"
camino_mas_corto_stack = grafo.dijkstra("habitación 1")

distancia_total_camino = 0

# Buscamos la distancia acumulada hasta "sala de estar" en el pila
while True:
    nodo = camino_mas_corto_stack.pop()
    if nodo is None:
        break
    if nodo[1][0] == "sala de estar":
        distancia_total_camino = nodo[0]  # Distancia acumulada en la pila
        break
print("")
print("Distancia total desde habitación 1 hasta sala de estar:", distancia_total_camino, "metros")
