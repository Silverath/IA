class Puerta(object):
    
    def __init__(self, tipo_puerta, entrada1, entrada2, salida):
        self.tipo = tipo_puerta
        self.entrada1 = entrada1
        self.entrada2 = entrada2
        self.salida = salida
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
        self.puerta_salida = puerta_salida
