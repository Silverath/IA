# coding=utf-8
import sys
import Puerta as puerta
from AG import *

entrada = [1, 1, 1]
puertas_defectuosas = []
circuito_usado = circuito
salida = puerta.calcular_salida(entrada, circuito_usado, puertas_defectuosas)
print (entrada)
print (salida)
print circuito_usado


