# coding=utf-8
from Puerta import *
import random
import matplotlib.pyplot as dibuj
import networkx as nx
import sys
import itertools

#IMPORTANTE: AQUÍ SE MODIFICAN LOS NÚMEROS DE FILAS Y COLUMNAS DEL CIRCUITO.
filas = 3
columnas = 3

def get_filas():
    return filas

def get_columnas():
    return columnas  

#Crea una tupla con el tamaño del circuito que queremos
def inicializar_circuito():
    circuito = ()
    filas = get_filas()
    columnas = get_columnas()
    for i in range(0, filas):
        nuevo = []
        for j in range(0, columnas): 
            nuevo.append(Puerta())
        tupla = nuevo
        circuito = circuito + (tupla,)
    return circuito

'''
Entrada
    -   entrada: lista de bits de entrada.
    -   circuito: circuito del cual calcularemos la salida.
    -   puertas_defectuosas: lista de puertas que están defectuosas.
    
Salida
    -   Salida resultante.



Para cada puerta en circuito[fila][columna] hacer:

    -   Si la fila es la primera (fila = 0):
        -   La puerta solo tiene una entrada (en entrada1) que será el valor de entrada[columna]. El valor del segundo input (entrada) es 0.
        -   Si la puerta se encuentra dentro de la lista de las puertas defectuosas la salida directamente es 0.
        -   En caso contrario se calcula la salida en función del tipo de puerta que sea y las dos entradas.
    -   Si la fila es la última:
        -   Asigna los valores de salida de las puertas conectadas (si es que tienen. Si no, el valor de la entrada que corresponde a esa puerta es 0) esta a las entradas respectivas.
        -   Si la puerta está defectuosa el valor de salida[columna] es 0. En caso contrario, se calcula.
    -   En cualquier otro caso:
        -   Se calcula el valor de salida de la misma puerta en función de las entradas (si no esta defectuosa).

Se devuelve la salida.
'''
def calcular_salida(entrada, circuito, puertas_defectuosas):
    filas = get_filas()
    columnas = get_columnas()
    salida = [0]*columnas
    for i in range(0, filas):
        for j in range(0, columnas): 
            puerta = circuito[i][j]
            if i == 0:
                puerta.entrada1 = entrada[j]
                puerta.entrada2 = 0
                if puerta in puertas_defectuosas:
                    puerta.salida = 0
                else:
                    puerta.salida = puerta.salida_resultante()
            if i == filas-1:
                                   
                if puerta.puerta_entrada1 != None:
                    puerta.entrada1 = puerta.puerta_entrada1.salida
                else:
                    puerta.entrada1 = 0
                if puerta.puerta_entrada2 != None:
                    puerta.entrada2 = puerta.puerta_entrada2.salida
                else:
                    puerta.entrada2 = 0
                
                if puerta in puertas_defectuosas:
                    salida[j] = 0
                else:
                    salida[j] = puerta.salida_resultante()
            if i != 0 and i != filas-1:
                if puerta.puerta_entrada1 != None:
                    puerta.entrada1 = puerta.puerta_entrada1.salida
                else:
                    puerta.entrada1 = 0
                if puerta.puerta_entrada2 != None:
                    puerta.entrada2 = puerta.puerta_entrada2.salida
                else:
                    puerta.entrada2 = 0
                
                if  puerta in puertas_defectuosas:
                    puerta.salida = 0
                else:
                    puerta.salida = puerta.salida_resultante()
        
    return salida

'''
Entrada
    -   individuo: circuito al que se le calcula la salida omitiendo las puertas señaladas como defectuosas.
    -   entrada: lista de bits que se le pasa como entrada al circuito.
    
Salida
    -   Salida resultante.

Se calcula la salida que resultaría de no haber ni una puerta defectuosa mediante el método calcular_salida().
'''
def salida_esperada(individuo, entrada):
    puertas_nodefectuosas = []
    result = calcular_salida(entrada, individuo, puertas_nodefectuosas)
    return result

'''
Entrada
    Ninguna
    
Salida
    -   Circuito resultante.

Se inicializa el circuito con el tamaño dado por los valores filas y columnas.
Para cada posición en circuito[fila][columna] hacer:

    -   Si es en la primera fila:
        -   Se crea un objeto Puerta, donde el tipo de lógica será aleatoria y se sitúa en la posición [fila][columna] del circuito nuevo.
    -   Si es la segunda fila:
        -   Se hace lo mismo y además en caso de que se vaya a crear, se añade como puerta de entrada una de las de la primera fila (lo mismo para las dos puertas de entrada).
        -   Se sitúa en la posición [fila][columna] del circuito nuevo.
    -   En cualquier otro caso:
        -   Se hace exactamente lo mismo que en la segunda fila con la modificación de que las puertas de entrada pueden ser cualquiera de las de las dos filas directamente inferiores.

Se devuelve el circuito ya creado
'''
def generar_circuito():

    individuo = inicializar_circuito()
    filas = get_filas()
    columnas = get_columnas()
    for i in range(0, filas):
        for j in range(0, columnas):
            if(i == 0):
                tipo = random.randint(0, 6)
                nueva_puerta = Puerta()
                nueva_puerta.tipo = tipo
                individuo[i][j] = nueva_puerta
            
            elif(i == 1):
                tipo = random.randint(0, 6)
                nueva_puerta = Puerta()
                nueva_puerta.tipo = tipo
                if 50 <random.randint(0, 100):
                    puerta_entrada1 = individuo[0][random.randint(0, columnas-1)]   
                    nueva_puerta.puerta_entrada1 = puerta_entrada1
                if 50 <random.randint(0, 100):
                    puerta_entrada2 = individuo[0][random.randint(0, columnas-1)]
                    nueva_puerta.puerta_entrada2 = puerta_entrada2
                individuo[i][j] = nueva_puerta
            
            else:
                tipo = random.randint(0, 6)
                nueva_puerta = Puerta()
                nueva_puerta.tipo = tipo
                if 50 <random.randint(0, 100):
                    puerta_entrada1 = individuo[random.randint(i-2, i-1)][random.randint(0, columnas-1)]
                    nueva_puerta.puerta_entrada1 = puerta_entrada1
                if 50 <random.randint(0, 100):
                    puerta_entrada2 = individuo[random.randint(i-2, i-1)][random.randint(0, columnas-1)]
                    nueva_puerta.puerta_entrada2 = puerta_entrada2
                    
                individuo[i][j] = nueva_puerta

    return individuo

'''
Entrada
    -   circuito: circuito del cual queremos crear el grafo
    
Salida
    Ninguna

Se crea un grafo que sera direccional

Para cada puerta dentro del circuito se crea un nodo que será esa misma puerta y se crea una arista con las puertas de entrada (si tienen).
Posteriormente, se dibuja el grafo y se muestran los nodos y aristas del mismo.
'''
def crear_grafo(circuito):
    g = nx.OrderedDiGraph()
    for i in range(0, len(circuito)):
        for j in range(0, len(circuito[0])): 
            puerta = circuito[i][j]
            g.add_node(puerta)
            if(puerta.puerta_entrada1 != None):
                g.add_edge(puerta.puerta_entrada1, puerta)
            if(puerta.puerta_entrada2 != None):
                g.add_edge(puerta.puerta_entrada2, puerta)
    nx.draw(g)

#Generación del circuito al que se hará el diagnóstico
circuito = generar_circuito()

#IMPORTANTE: AQUÍ SE MODIFICA LA LISTA DE PUERTAS DEFECTUOSAS. DEBEN SER AÑADIDAS EN FUNCIÓN DEL NÚMERO DE FILAS Y COLUMNAS QUE SE HAN DEFINIDO ARRIBA, YA QUE SI NO DARÁ ERROR.
puertas_defectuosas = [circuito[1][0], circuito[1][1], circuito[1][2]] 

def main(reparacion):
    
    print('-----------------------------------------------GENERANDO CIRCUITO-----------------------------------------------')
    print circuito
    
    print('-----------------------------------------------CREANDO GRAFO-----------------------------------------------')
    crear_grafo(circuito)
    print('-----------------------------------------------PUERTAS PUESTAS COMO DEFECTUOSAS-----------------------------------------------')
    
    
    print puertas_defectuosas

    print('-----------------------------------------------ANALIZANDO CIRCUITO-----------------------------------------------')
    
    dibuj.show()

    
    permutaciones = list(itertools.product([0, 1], repeat=columnas))                #Lista de todas las posibles combinaciones de entrada
    for permutacion in permutaciones:
        salida_buena = salida_esperada(circuito, permutacion)                       #Salida que deberia de dar en caso de que este correcto el circuito
        salida_real = calcular_salida(permutacion, circuito, puertas_defectuosas)   #Salida que da dadas las puertas defectuosas
        
        if salida_buena != salida_real:
            print ("la salida para la entrada "), permutacion, (" no es correcta: resulta en "), salida_real, (" cuando deberia de ser "), salida_buena
            reparacion = True
        
        if reparacion == False:
            print('-----------------------------------------------CIRCUITO CORRECTO, NO NECESITA DE REPARACION-----------------------------------------------')
            return 0
        else:
            print('-----------------------------------------------CIRCUITO CON FALLOS, REPARANDO-----------------------------------------------')
            return -1
