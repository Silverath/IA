import random
import networkx as nx
from MetodosAuxiliares import *
#from Main import *

g = nx.fast_gnp_random_graph(15, 0.3)

'''

tam: Número de individuos por población.
largo: Longitud de la lista.
presion: Número de individuos que se seleccionan para la siguiente iteración en el algoritmo
c_clique: Contiene el mayor clique(k-completo) en el grafo

'''


tam = 1000000
largo = nx.number_of_nodes(g)
c_max = clique_maximo(g)


'''

Crea un individuo de manera aleatoria.

'''


def crea_individuo(min, max):
    return[random.randint(min, max) for i in range(largo)]


'''

Crea una población aleatoria utilizando 'crea_individuo'.

'''

def crea_poblacion():
    return [crea_individuo(1, colores(g)) for i in range(tam)]


'''

Se crea una población inicial

'''


poblacion_inicial = crea_poblacion();


'''

Calcula el fitness para un individuo:

Parámetros de entrada:
    individuo: Individuo a valorar.

Funcionamiento:
1. Se declara la variable 'fitness', en la que se va a almacenar el valor acumulado de un individuo
2. Para cada color en el individuo HACER:
    2.1. Si el numero de colores usados en el individuo en cuestión es mayor que el clique(k-completo) 
    máximo en el grafo g, suma al fitness 10000.
    2.2. Se crea una lista VECINOS en la que se almacenen los nodos vecinos del nodo i.
    2.3. Para cada elemento en VECINOS, HACER:
        2.3.1. Si  el color del nodo i es igual al color del nodo vecino j, suma 100000 al fitness
3. Devolver fitness

'''


def otro_fitness(individuo):
    fitness = 0
    for i in range(0, len(individuo)):
        if numero_colores_usados(individuo) > c_max:
           fitness += 10000
        vecinos = list(nx.neighbors(g, i))
        for j in range(len(vecinos)):
            if individuo[i] == individuo[vecinos[j]]:
                fitness += 100000
    return fitness


'''

Se puntúan todos los elementos de la población y nos quedamos con los mejores:

Parámetros de entrada:
    población: Población sobre la que se desea realizar la selección.
    
Funcionamiento:
1. Se puntúan los individuos de la población.
2. Se ordenan los individuos de puntuados.
3. Se selecionan los mejores individuos.
4. Se devuelven los individuos seleccionados.

'''


def seleccion(poblacion):
    puntuados = [(otro_fitness(i), i) for i in poblacion]
    puntuados = [i[1] for i in sorted(puntuados)]

    seleccionados = puntuados[(len(puntuados) - 1)]

    return seleccionados


'''

Genera un sucesor de un individuo aleatorio de la población inicial:

Parámetros de entrada:
    Este método no recibe ningún parámetro de entrada.

Funcionamiento:
1. Se escoge aleatoriamente un individuo de la población inicial.
2. Se elige aleatoriamente el elemento(color) del individuo a cambiar y se sustituye por otro aleatorio
3. Se devuelve el individuo cambiado

'''


def genera_sucesor():
    individuo = random.choice(poblacion_inicial)
    individuo_cambiado = individuo
    individuo_cambiado[random.randint(0, len(individuo) - 1)] = random.randint(0, len(individuo) - 1)
    return individuo_cambiado


'''

Algoritmo de enfriamiento simulado(Simulated Annealing):

Parámetros de entrada:
    t_inicial: 'Temperatura' inicial del algoritmo.
    factor_descenso: Cuanto desciende la temperatura después de cada iteración.
    n_enfriamientos: Número de enfriamientos que se realizan en el algoritmo(número de veces que
        se disminuye la t_inicial).
    n_iteraciones: Número de veces que se realiza el algoritmo.
    
Funcionamiento:
1. Se declaran las variables:
    - temperatura: Donde se almacena la temperatura actual en el algoritmo.
    - actual: Donde se almacena la selección de los mejores individuos de la población inicial.
    - valor_actual: Donde se almacena el fitness del mejor individuo de la población.
    - mejor: Donde se almacena el mejor individuo encontrado.
    - valor_mejor: Donde se almacena el fitness del mejor individuo encontrado.
2. Para todos los valores de i hasta n_enfriamientos HACER
    2.1. Para todos lo valores de j hasta n_iteraciones HACER
        2.1.1. Se genera un individuo candidato y se calcula su fitness.
        2.1.2. Si la diferencia entre el valor del individuo candidato y el mejor actual es menor que cero,
            se almacena en actual el individuo candidato y en valor_actual su fitness.
        2.1.3. Si valor_actual es menor que valor_mejor, en mejor se almacena el individuo actual y en mejor_valor,
            valor_actual.
    2.2. Se reduce la temperatura en función del factor descenso.
3. Se devuelve el mejor candidato encontrado.
    
'''


def enfriamiento_simulado(t_inicial, factor_descenso, n_enfriamientos, n_iteraciones):
    temperatura = t_inicial
    actual = seleccion(poblacion_inicial)
    valor_actual = otro_fitness(actual)
    mejor = actual
    valor_mejor = valor_actual

    for i in range(0, n_enfriamientos):
        for j in range(0, n_iteraciones):
            candidata = genera_sucesor()
            valor_candidata = otro_fitness(candidata)
            incremento = valor_candidata - valor_actual
            if incremento < 0:
                actual = candidata
                valor_actual = valor_candidata
            if valor_actual < valor_mejor:
                mejor = actual
                valor_mejor = valor_actual
        temperatura -= factor_descenso

    return mejor

