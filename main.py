# coding=utf-8
import sys
import Puerta as Puerta
import networkx as nx
from AG import *
import matplotlib.pyplot as dibuj

def crear_grafo(circuito):
    g = nx.OrderedDiGraph()
    for i in range(0, len(circuito)):
        for j in range(0, len(circuito[i])): 
            puerta = circuito[i][j]
            g.add_node(puerta)
            if(puerta.puerta_entrada1 != None):
                g.add_edge(puerta.puerta_entrada1, puerta)
            if(puerta.puerta_entrada2 != None):
                g.add_edge(puerta.puerta_entrada2, puerta)
    nx.draw(g)
    print "puertas: ", sorted(g.nodes())
    print "conexiones: ", sorted(g.edges())
entrada = [1, 1, 1]
puertas_defectuosas = []
circuito_usado = circuito
salida = Puerta.calcular_salida(entrada, circuito_usado, puertas_defectuosas)
print (entrada)
print (salida)
print circuito_usado
crear_grafo(circuito_usado)
dibuj.show()
