from itertools import permutations

class Cliente:
    def __init__(self, name:str, idc:str, age:int, ticket=None, spendings=0.0, historial=0):
        self.nombre = name
        self.cedula = idc
        self.edad = age
        self.ticket = ticket
        self.gastos = spendings
        self.historial = historial
    
    
    def es_vampiro(self):
        cedula = self.cedula
        if len(cedula) % 2 == 0:
            mitad = len(cedula) // 2
            permutaciones = []
            permutaciones = set(permutations(cedula, len(cedula)))
            for perm in permutaciones:
                numero_1 = int("".join(perm[:mitad]))
                numero_2 = int("".join(perm[mitad:]))
                
                if str(numero_1).endswith("0") and str(numero_2).endswith("0"):
                    continue
                else:
                    
                    if numero_1*numero_2 == int(cedula):
                        return True

        else: return False
    
    def es_perfecto(self):
        divisores = []
        suma = 0
        
        for i in range (1, int(self.cedula)):
            if int(self.cedula) % i == 0:
                divisores.append(i)
            else: pass
            
        for numero in divisores:
            suma += numero
        return suma == int(self.cedula)
        
    def cambiar_ticket(self, boleto):
        self.ticket = boleto
    
    def sumar_gastos(self, gasto):
        self.gastos += gasto
    
    def sumar_historial(self):
        self.historial += 1