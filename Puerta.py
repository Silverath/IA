class Puerta(object):
    entrada1 = int
    entrada2 = int
    salida = int
    salida_real = salida_esperada
    def __init__(self, tipo_puerta):
        self.tipo = tipo_puerta
        self.salida_real = self.salida_esperada

    def salida_esperada(self):
        if self.tipo == 'AND':
            if self.entrada1 == 1 and self.entrada2 == 1:
                return 1
            else:
                return 0
        if self.tipo == 'OR':
            if self.entrada1 == 1 or self.entrada2 == 1:
                return 1
            else:
                return 0
        if self.tipo == 'NOT':
            if self.entrada1 == 0:
                return 1
            else:
                return 0
        if self.tipo == 'NAND':
            if self.entrada1 == 1 and self.entrada2 == 1:
                return 0
            else:
                return 1
        if self.tipo == 'XOR':
            if self.entrada1 == self.entrada2:
                return 0
            else:
                return 1 
    
    def esta_defectuosa(self):
        if(self.salida != self.salida_real):
            return True
        else:
            return False

class Conexion(object):
    def __init__(self, puerta_entrada1, puerta_entrada2, puerta_salida):
        self.puerta_entrada1 = puerta_entrada1
        self.puerta_entrada2 = puerta_entrada2
        if puerta_entrada2 == None:
            self.puerta_entrada2 = 0
        self.puerta_salida = puerta_salida

        self.puerta_salida.salida = self.salida_resultante()

    def salida_resultante(self):
        if self.puerta_salida.tipo == 'AND':
            if self.puerta_entrada1.salida == 1 and self.puerta_entrada2.salida == 1:
                return 1
            else:
                return 0
        if self.puerta_salida.tipo == 'OR':
            if self.puerta_entrada1.salida == 1 or self.puerta_entrada2.salida == 1:
                return 1
            else:
                return 0
        if self.puerta_salida.tipo == 'NOT':
            if self.puerta_entrada1.salida == 0:
                return 1
            else:
                return 0
        if self.puerta_salida.tipo == 'NAND':
            if self.puerta_entrada1.salida == 1 and self.puerta_entrada2.salida == 1:
                return 0
            else:
                return 1
        if self.puerta_salida.tipo == 'XOR':
            if self.puerta_entrada1.salida == self.puerta_entrada2.salida:
                return 0
            else:
                return 1 