#Universidad del Valle de Guatemala
#Inteligencia Artificial
#Integrantes:
# Bryann Alfaro
# Raul Jimenez
# Donaldo Garcia
# Oscar Saravia

import sys

if __name__ == "__main__":
    definicion_grafo = sys.argv[1]
    estado_inicial = sys.argv[2]
    estado_final = sys.argv[3]

#Abrir archivo de definicion del grafo
grafo = open(definicion_grafo, "r")
vertices = grafo.readline()
cantidad_aristas = grafo.readline()

print(grafo.read())

print('vertices: ',vertices)
print('aristas: ',cantidad_aristas)
print('estado inicial: ',estado_inicial)
print('estado final: ',estado_final)
