# coding=utf-8
import itertools
import random as rand

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
                
def calcular_salida(entrada, circuito, puertas_defectuosas):
    salida = [0]*len(circuito[0])
    for i in range(0, len(circuito)):
        for j in range(0, len(circuito[i])): 
            puerta = circuito[i][j]
            if i == 0:
                puerta.entrada1 = entrada[j]
                puerta.entrada2 = 0
                if puerta in puertas_defectuosas:
                    puerta.salida = 0
                else:
                    puerta.salida = puerta.salida_resultante()
            if i == len(circuito[i]) - 1:
                                   
                if puerta.puerta_entrada1 != None:
                    puerta.entrada1 = puerta.puerta_entrada1.salida
                else:
                    puerta.entrada1 = 0
                if puerta.puerta_entrada2 != None:
                    puerta.entrada2 = puerta.puerta_entrada2.salida
                else:
                    puerta.entrada2 = 0
                
                if puerta.puerta_entrada1 == None and puerta.puerta_entrada2 == None or puerta in puertas_defectuosas:
                    salida[j] = 0
                else:
                    salida[j] = puerta.salida_resultante()
            if i != 0 and i != len(circuito[i])-1:
                if puerta.puerta_entrada1 != None:
                    puerta.entrada1 = puerta.puerta_entrada1.salida
                else:
                    puerta.entrada1 = 0
                if puerta.puerta_entrada2 != None:
                    puerta.entrada2 = puerta.puerta_entrada2.salida
                else:
                    puerta.entrada2 = 0
                
                if puerta.puerta_entrada1 == None and puerta.puerta_entrada2 == None or puerta in puertas_defectuosas:
                    puerta.salida = 0
                else:
                    puerta.salida = puerta.salida_resultante()
        
    return salida