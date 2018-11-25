# coding=utf-8
import random
import Puerta
#from Main import *

'''

tam: Número de individuos por población.
largo: Longitud de la lista.
presion: Número de individuos que se seleccionan para la siguiente iteración en el algoritmo
c_clique: Contiene el mayor clique(k-completo) en el grafo

'''


puerta01 = Puerta.Puerta()
puerta01.tipo = 1
puerta02 = Puerta.Puerta()
puerta02.tipo = 0
puerta03 = Puerta.Puerta()
puerta03.tipo = 1
puerta04 = Puerta.Puerta()
puerta05 = Puerta.Puerta()
puerta11 = Puerta.Puerta()
puerta11.tipo = 2
puerta11.puerta_entrada1 = puerta01
puerta11.puerta_entrada2 = puerta02     
puerta12 = Puerta.Puerta()
puerta12.tipo = 4
puerta12.puerta_entrada1 = puerta01
puerta12.puerta_entrada2 = puerta02     
puerta13 = Puerta.Puerta()
puerta13.tipo = 3
puerta13.puerta_entrada1 = puerta02
puerta13.puerta_entrada2 = puerta03     
puerta14 = Puerta.Puerta()
puerta14.tipo = 3
puerta14.puerta_entrada1 = puerta01
puerta14.puerta_entrada2 = puerta03
puerta15 = Puerta.Puerta()
puerta21 = Puerta.Puerta()
puerta21.tipo = 2
puerta21.puerta_entrada1= puerta11
puerta22 = Puerta.Puerta()
puerta22.tipo = 0
puerta22.puerta_entrada1 = puerta12
puerta22.puerta_entrada2 = puerta13     
puerta23 = Puerta.Puerta()
puerta23.tipo = 2
puerta23.puerta_entrada1 = puerta12
puerta23.puerta_entrada2 = puerta13     
puerta24 = Puerta.Puerta()
puerta25 = Puerta.Puerta()
puerta31 = Puerta.Puerta()
puerta31.tipo = 0
puerta31.puerta_entrada1= puerta12
puerta31.puerta_entrada2= puerta21
puerta32 = Puerta.Puerta()
puerta32.tipo = 1
puerta32.puerta_entrada1= puerta21
puerta32.puerta_entrada2= puerta23
puerta33 = Puerta.Puerta()
puerta33.tipo = 4
puerta33.puerta_entrada1= puerta21
puerta33.puerta_entrada2= puerta13
puerta34 = Puerta.Puerta()
puerta35 = Puerta.Puerta()
puerta41 = Puerta.Puerta()
puerta42 = Puerta.Puerta()
puerta43 = Puerta.Puerta()
puerta44 = Puerta.Puerta()
puerta45 = Puerta.Puerta()
puerta51 = Puerta.Puerta()
puerta52 = Puerta.Puerta()
puerta53 = Puerta.Puerta()
puerta54 = Puerta.Puerta()
puerta55 = Puerta.Puerta()
puerta61 = Puerta.Puerta()
puerta62 = Puerta.Puerta()
puerta63 = Puerta.Puerta()
puerta64 = Puerta.Puerta()
puerta65 = Puerta.Puerta()
puerta71 = Puerta.Puerta()
puerta72 = Puerta.Puerta()
puerta73 = Puerta.Puerta()
puerta74 = Puerta.Puerta()
puerta75 = Puerta.Puerta()
puerta81 = Puerta.Puerta()
puerta82 = Puerta.Puerta()
puerta83 = Puerta.Puerta()
puerta84 = Puerta.Puerta()
puerta85 = Puerta.Puerta()
puerta91 = Puerta.Puerta()
puerta92 = Puerta.Puerta()
puerta93 = Puerta.Puerta()
puerta94 = Puerta.Puerta()
puerta95 = Puerta.Puerta()

circuito = ([puerta01, puerta02, puerta03],
            [puerta11, puerta12, puerta13],
            [puerta21, puerta22, puerta23])
'''

Crea un individuo de manera aleatoria.

'''

puertas_defectuosas = [puerta11, puerta13]
entrada = [1, 1, 1]

def salida_esperada():
    puertas_nodefectuosas = []
    return Puerta.calcular_salida(entrada, circuito, puertas_nodefectuosas)
'''

Crea una población aleatoria utilizando 'crea_individuo'.

'''



'''

Se crea una población inicial

'''


poblacion_inicial = circuito


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

'''
def seleccion(poblacion):
    puntuados = [(otro_fitness(i), i) for i in poblacion]
    puntuados = [i[1] for i in sorted(puntuados)]

    seleccionados = puntuados[(len(puntuados) - 1)]

    return seleccionados

'''
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
'''
