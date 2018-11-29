# coding=utf-8
import random
import Puerta

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

puertas_defectuosas = [puerta11, puerta13]
entrada = [1, 1, 1]

def salida_esperada():
    puertas_nodefectuosas = []
    return Puerta.calcular_salida(entrada, circuito, puertas_nodefectuosas)
