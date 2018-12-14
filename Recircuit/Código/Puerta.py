# coding=utf-8
import itertools
import random as rand
'''
Esta clase Puerta es la que utilizaremos para referenciar a cada puerta de un circuito. Cada objeto Puerta contará con:

    -   puerta_entrada1: puerta conectada al input 1 de la misma
    -   puerta_entrada2: puerta conectada al input 2 de la misma
    -   entrada1: valor resultante del output de la puerta_entrada1 
    -   entrada2: valor resultante del output de la puerta_entrada1 
    -   salida: valor resultante del output de esta puerta
    -   tipo: lógica que realizará la puerta para calcular la salida (puede ser OR, AND, NOT...). 
        Este atributo es un entero y en función del valor del mismo actuará de una forma u otra 
        (por ejemplo, si el entero es 0 actuará como una puerta AND, si es 1 como una OR, etc).
    -   id: entero aleatorio en el rango (0,1000) que servirá para diferenciar a las puertas del circuito entre ellas.

Cada objeto Puerta se representará de la siguiente forma: un par (lógica, id) donde "lógica" se refiere al tipo de puerta lógica que simula e "id" el identificador de la misma.

Dentro de esta clase, también podemos encontrar una función que se llama "salida_resultante", 
la cual se encargará, en función del tipo de puerta, de calcular el output y asignar el valor al atributo "salida"
'''
class Puerta(object):
    
    
    def __init__(self):
        self.puerta_entrada1 = None
        self.puerta_entrada2 = None
        self.entrada1 = int
        self.entrada2 = int
        self.salida = int
        self.tipo = int
        self.id = rand.randint(0, 1000)

    def __str__(self):
        if self.tipo == 0:
            return 'AND, ' + str(self.id)
        if self.tipo == 1:
            return 'OR, ' + str(self.id)
        if self.tipo == 2:
            return 'NOT, ' + str(self.id)
        if self.tipo == 3:
            return 'NAND, ' + str(self.id)
        if self.tipo == 4:
            return 'XOR, ' + str(self.id)
        if self.tipo == 5:
            return 'NOR, ' + str(self.id)
        if self.tipo == 6:
            return 'XNOR, ' + str(self.id)

    def __repr__(self):
        if self.tipo == 0:
            return 'AND, ' + str(self.id)
        if self.tipo == 1:
            return 'OR, ' + str(self.id)
        if self.tipo == 2:
            return 'NOT, ' + str(self.id)
        if self.tipo == 3:
            return 'NAND, ' + str(self.id)
        if self.tipo == 4:
            return 'XOR, ' + str(self.id)       
        if self.tipo == 5:
            return 'NOR, ' + str(self.id)
        if self.tipo == 6:
            return 'XNOR, ' + str(self.id)

    def salida_resultante(self):
        #AND
        if self.tipo == 0:
            if self.entrada1 == 1 and self.entrada2 == 1:
                return 1
            else:
                return 0
        #OR
        if self.tipo == 1:
            if self.entrada1 == 1 or self.entrada2 == 1:
                return 1
            else:
                return 0
        #NOT
        if self.tipo == 2:
            if self.entrada1 == 0:
                return 1
            else:
                return 0
        #NAND
        if self.tipo == 3:
            if self.entrada1 == 1 and self.entrada2 == 1:
                return 0
            else:
                return 1
        #XOR
        if self.tipo == 4:
            if self.entrada1 == self.entrada2:
                return 0
            else:
                return 1  

        #NOR
        if self.tipo == 5:
            if self.entrada1 == 0 and self.entrada2 == 0:
                return 1
            else:
                return 0

        #XNOR         
        if self.tipo == 6:
            if self.entrada1 == self.entrada2:
                return 1
            else:
                return 0