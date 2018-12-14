# coding=utf-8
import Puerta
from deap import base, creator, tools, algorithms
import numpy
from Circuito import *


'''
Entrada
    -   Individuo a evaluar.

Salida
    -   Fitness del individuo.

DADO QUE EL PROBLEMA CONSISTIRÁ EN MAXIMIZAR:

    -   Se definen dos variables: salida_buena (la salida que debería de dar el circuito original ignorando las puertas defectuosas) y salida_real (la salida del circuito a evaluar con las puertas defectuosas).
    -   Se define una variable double que se inciará a 0.0 llamada "errores".
    -   Se define una variable "fitness" que se inciará a 0.0 y sera el valor final que devolvamos.
    -   Para cada posición de las dos salidas, si difieren en el valor, la variable "errores" se suma en 10.
    -   Por último, se multiplica el valor final de "errores" por 1000 y guardamos el valor en la variable "fitness".

Se devuelve "fitness"
'''
def evaluar_individuo(individuo):
    #IMPORTANTE: AQUÍ SE MODIFICA LA LISTA DE PUERTAS DEFECTUOSAS PARA EL ALGORITMO GENÉTICO.
    #DEBEN SER AÑADIDAS EN FUNCIÓN DEL NÚMERO DE FILAS Y COLUMNAS QUE SE HAN DEFINIDO Y 
    #SER LAS MISMAS POSICIONES DENTRO DEL CIRCUITO "individuo" QUE LAS DECLARADAS EN EL ARCHIVO "Circuito.py"S 
    puertas_defectuosas = [individuo[1][0], individuo[1][1], individuo[1][2]] 
    
    errores = 0.0
    fitness = 0.0
    permutaciones = list(itertools.product([0, 1], repeat=columnas))
    for permutacion in permutaciones:
        salida_buena = salida_esperada(circuito, permutacion)
        salida_real = calcular_salida(permutacion, individuo, puertas_defectuosas)
        for i in range(0, len(salida_buena)):
            if salida_real[i] != salida_buena[i]:
                errores = errores + 10
    fitness = 1000.0*errores
    return [fitness]

'''
Entrada
    -   Individuos que se van a cruzar.
    
Salida
    -   Los dos individuos cruzados.

-   Se eligen una puertas dentro del rango [filas][columnas]
-   Se definen las puertas que se encuentran en la posición resultante de los dos individuos (circuitos) que pasamos como parámetros
-   Se intercambian los tipos de logica (atributo "tipo") y se devuelven el par de individuos nuevos con el tipo de logica intercambiada.
'''
def cross(ind1, ind2):
    filas = get_filas()
    columnas = get_columnas()
    for i in range(0, filas*columnas/4):
        fila = random.randint(0, filas-1)
        columna = random.randint(0, columnas-1)
        puerta1 = ind1[fila][columna]
        puerta2 = ind2[fila][columna]
        ind2[fila][columna].tipo = puerta1.tipo
        ind1[fila][columna].tipo = puerta2.tipo
    return ind1, ind2

'''
Entrada
    -   Individuo a mutar.
    -   índice de probabilidad de que una puerta mute (indpb).
    
Salida
    -   Fitness del individuo.

Para cada puerta del individuo que se le pasa como parámetro y si un número aleatorio resultante entre 0 y 1 es menor que indpb:

    -   En caso de que la posición sea de la primera fila, se muta solamente el tipo de puerta.
    -   Si consta de la segunda fila, se muta el tipo y las puertas de entrada solo pueden ser de la primera fila.
    -   En cualquier otro caso, se muta el tipo y las puertas de entrada, que si se les asignan, solo pueden ser de las dos filas anteriores.

Por último, se devuelve el individuo mutado
'''
def mutar(individuo, indpb):
    filas = get_filas()
    columnas = get_columnas()
    for i in range(0, filas):
        for j in range(0, columnas):
            if random.random() < indpb:
                if(i == 0):
                    tipo = random.randint(0, 6)
                    individuo[i][j].tipo = tipo
            
                elif(i == 1):
                    tipo = random.randint(0, 6)
                    individuo[i][j].tipo = tipo

                    if 1 == random.randint(0, 1):
                        puerta_entrada1 = individuo[0][random.randint(0, columnas-1)]
                        individuo[i][j].puerta_entrada1 = puerta_entrada1
                    if 1 == random.randint(0, 1):
                        puerta_entrada2 = individuo[0][random.randint(0, columnas-1)]
                        individuo[i][j].puerta_entrada2 = puerta_entrada2                              
                else:
                    tipo = random.randint(0, 6)
                    individuo[i][j].tipo = tipo
                    if 1 == random.randint(0, 1):
                        puerta_entrada1 = individuo[random.randint(i-2, i-1)][random.randint(0, columnas-1)]
                        individuo[i][j].puerta_entrada1 = puerta_entrada1
                    if 1 == random.randint(0, 1):
                        puerta_entrada2 = individuo[random.randint(i-2, i-1)][random.randint(0, columnas-1)]
                        individuo[i][j].puerta_entrada2 = puerta_entrada2  
                    

    return individuo,

'''
En este método main, si el circuito de prueba resulta estar erroneo, se crea el algoritmo genético de tipo torneo y se muestran al final el registro del mismo y los tres mejores resultados (fitness).
'''
#IMPORTANTE: AQUÍ SE CAMBIAN LOS PARÁMETROS DEL ALGORITMO GENÉTICO
def mainAG():
    reparacion = False
    if main(reparacion) == -1:
        
        CANTIDAD_POBLACION = 20 #Población
        TOURNSIZE = 5           #Número de individuos a seleccionar
        INDICE_MUTACION = 0.1   #Probabilidad de que se mute alguna puerta de un individuo
        PROB_CRUCE = 0.2        #Probabilidad de que dos individuos contiguos se crucen
        PROB_MUTAR = 0.3        #Probabilidad de que un individuo mute
        NUM_GENERACIONES = 30  #Numero de generaciones del algoritmo

        creator.create('Fitness', base.Fitness, weights=(-1.0,))
        creator.create('Individuo', tuple, fitness = creator.Fitness)
        caja_de_herramientas = base.Toolbox()
        caja_de_herramientas.register('individuo', tools.initIterate,
                                    container=creator.Individuo, 
                                    generator=generar_circuito)
        caja_de_herramientas.register('poblacion', tools.initRepeat,
                                    container=list, func=caja_de_herramientas.individuo, n=CANTIDAD_POBLACION)
        caja_de_herramientas.register('evaluate', evaluar_individuo)
        caja_de_herramientas.register('mate', cross)
        caja_de_herramientas.register('mutate', mutar, indpb=INDICE_MUTACION)
        caja_de_herramientas.register('select', tools.selTournament, tournsize=TOURNSIZE)
        estadisticas = tools.Statistics(lambda ind: ind.fitness.values)
        estadisticas.register("minimo", numpy.min)
        estadisticas.register("media", numpy.mean)
        estadisticas.register("maximo", numpy.max)
        salon_fama = tools.HallOfFame(3)
        poblacion_inicial = caja_de_herramientas.poblacion()
        poblacion, registro = algorithms.eaSimple(poblacion_inicial,
                                                caja_de_herramientas,
                                                cxpb=PROB_CRUCE, # Probabilidad de que dos individuos contiguos se crucen
                                                mutpb=PROB_MUTAR, # Probabilidad de que un individuo mute
                                                ngen=NUM_GENERACIONES, # Número de generaciones
                                                stats=estadisticas,    # Estadísticas
                                                halloffame=salon_fama)  # Salón de fama
        print "-----------------------------------------------MEJORES RESULTADOS-----------------------------------------------"
        for individuo in salon_fama:
            
            if evaluar_individuo(individuo) == [0.0]:
                print "SE ENCONTRO UN SUSTITUTO CORRECTO:"
                print('Individuo Fitness: {0}'.format(
                individuo.fitness.values[0], *evaluar_individuo(individuo)))
            else:
                print "NO ES UNA SOLUCION PERFECTA:"
                print('Individuo Fitness: {0}'.format(
                individuo.fitness.values[0], *evaluar_individuo(individuo)))
            print individuo
                
            crear_grafo(individuo)
            dibuj.show()