#Universidad del Valle de Guatemala
#Inteligencia Artificial
#Integrantes:
# Bryann Alfaro
# Raul Jimenez
# Donaldo Garcia
# Oscar Saravia

import sys
from grafo import *
from dijkstra import *

definicion_grafo = sys.argv[1]
estado_inicial = sys.argv[2]
estado_final = sys.argv[3]

#Abrir archivo de definicion del grafo
grafo = open(definicion_grafo, "r")
vertices = grafo.readline()
cantidad_aristas = grafo.readline()
aristas = []
for arista in grafo.readlines():
    arista = arista.split()
    arista[0] = arista[0]
    arista[1] = arista[1]
    arista[2] = arista[2]
    aristas.append(arista)

nodes = []
aristas_weighted = {}

for i in range(int(vertices)):
    nodes.append(str(i+1))

for node in nodes:
    aristas_weighted[node] = {}

for arista in aristas:
    aristas_weighted[(arista[0])][arista[1]] = int(arista[2])

graph = Graph(nodes, aristas_weighted)
print('nodos: ',graph.get_nodes())
print('cantidad de vertices: ',vertices)
print('cantidad de aristas: ',cantidad_aristas)
print('estado inicial: ',estado_inicial)
print('estado final: ',estado_final)

previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=estado_inicial)
print_result(previous_nodes, shortest_path, start_node=estado_inicial, target_node=estado_final)