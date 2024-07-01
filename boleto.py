from cliente import Cliente
from partido import Partido
class Boleto:
    def __init__(self, customer:Cliente, match:Partido, seat:str, code:str):
        self.partido = match
        self.cliente = customer
        self.asiento = seat
        self.codigo = code

    def mostrar_ticket(self, estadio_nombre:str):
        nombre_cliente = self.cliente.nombre.upper()
        
        print("――――――――――――――――――――――――――――― 1 TICKET ―――――――――――――――――――――――――――――")
        print("{:>34}".format("Home   "),end="")
        print("{:<34}".format("   Away"))
        print("{:>31}".format(f"{self.partido.local.nombre}"),end="")
        print(" V.S. ", end="")
        print(" {:<31}".format(f"{self.partido.visitante.nombre}"))
        print(f"--------------------------------------------------------------------")
        print("{:<34}".format(f"    Match Number #{self.partido.número}"), end="")
        print("{:>34}".format("TICKET HOLDER:    "))
        print("{:<34}".format(f"    {self.partido.grupo}"), end="")
        print("{:>34}".format(f"{nombre_cliente}    "))
        print("{:<34}".format(f"    Stadium: {estadio_nombre}"), end="")
        print("{:>34}".format(f"Seat:    "))
        print("{:<34}".format(f"    Date: {self.partido.fecha}"), end="")
        print("{:>34}".format(f"Seat:{self.asiento}    "))
        print(f"    Unique Code: {self.codigo} (Do not lose or give this to anyone.)")
        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
    
    def usar_codigo(self):
        self.codigo = None

class BoletoGeneral(Boleto):
    def __init__(self, customer:Cliente, match:Partido, seat:str, code:str, ticket_type="General", price=35.0):
        super().__init__(customer, match, seat, code)
        self.tipo_entrada = ticket_type
        self.precio = price
        
    def mostrar_precio(self):
        subtotal = self.precio
        if self.cliente.es_vampiro() == True:
            descuento_vampiro = self.precio*0.5
            print(f"""
Your ID is a Vampire Number! Now you have a 50% of discount
{subtotal} ----vampire discount----> {subtotal-descuento_vampiro}
""")
            subtotal = self.precio - descuento_vampiro
        else: pass
        iva = round(self.precio*0.16, 2)
        self.precio = subtotal + (iva)
        print(f"""
―――――――――――――――― RECEIPT ――――――――――――――――
1 General Ticket

Subtotal: {subtotal}
+ IVA: {iva}
TOTAL: {self.precio} $
―――――――――――――――――――――――――――――――――――――――――""")
        eleccion = None
        while eleccion != '9' and eleccion != '0':    
            print("""
Do yo want to continue?
[1] Yes
[9] No
""")
            eleccion = input("-> ")
            if eleccion == '1':
                return eleccion, self.precio
            elif eleccion == '9':
                return eleccion, None
            elif eleccion == '0':
                return eleccion, None
            else: 
                print("Error. Please enter a valid option.")
    
    
class BoletoVIP(Boleto):
    def __init__(self, customer:Cliente, match:Partido, seat:str, code:str, ticket_type="V.I.P.", price=75.0):
        super().__init__(customer, match, seat, code)
        self.tipo_entrada = ticket_type
        self.precio = price

    def mostrar_precio(self):
        subtotal = self.precio
        if self.cliente.es_vampiro() == True:
            descuento_vampiro = self.precio*0.5
            print(f"""
Your ID is a Vampire Number! Now you have a 50% of discount
{subtotal} ----vampire discount----> {subtotal-descuento_vampiro}
""")
            subtotal = self.precio - descuento_vampiro
        else: pass
        iva = round(self.precio*0.16, 2)
        self.precio = subtotal + (iva)
        print(f"""
―――――――――――――――― RECEIPT ――――――――――――――――
1 VIP Ticket

Subtotal: {subtotal}
+ IVA: {iva}
TOTAL: {self.precio} $
―――――――――――――――――――――――――――――――――――――――――""")
        eleccion = None
        while eleccion != '9' and eleccion != '0':    
            print("""
Do yo want to continue?
[1] Yes
[9] No
""")
            eleccion = input("-> ")
            if eleccion == '1':
                return eleccion, self.precio
            elif eleccion == '9':
                return eleccion, None
            elif eleccion == '0':
                return eleccion, None
            else: 
                print("Error. Please enter a valid option.")