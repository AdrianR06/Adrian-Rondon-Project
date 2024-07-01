from cliente import Cliente

class Producto:
    def __init__(self, name:str, quiantity:int, price:float, stock:int, restaurant:str, adicional=None):
        self.nombre = name
        self.vendidos = quiantity
        self.precio = price
        self.cantidad = stock
        self.restaurante = restaurant
        self.tipo = adicional
    
    def mostrar_detalles(self):
        mitad = len(self.nombre) // 2
        parte1 = self.nombre[:mitad]
        parte2 = self.nombre[mitad:]
        available_in = f"Available in: {self.restaurante}"
        mitad2 = len(available_in) // 2
        parte3 = available_in[:mitad2]
        parte4 = available_in[mitad2:]

        print("――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("{:>25}".format(f"{parte1}"), end="")
        print("{:<25}".format(f"{parte2}"))
        print(f"""--------------------------------------------------""")
        print("{:<25}".format(f"    Stock: {self.cantidad}"), end='')
        print("{:>25}".format(f"Selled: {self.vendidos}    "))
        print("{:<25}".format(f"    Price: {self.precio} $"), end='')
        print("{:>25}".format(f"Type: {self.tipo}    "))
        print("{:>25}".format(f"{parte3}"), end="")
        print("{:<25}".format(f"{parte4}"))
        print("――――――――――――――――――――――――――――――――――――――――――――――――――")
        
    def mostrar_precio(self,cliente:Cliente, cantidad:int):
        pre_product = self.precio
        initial = self.precio * cantidad
        if cliente.es_perfecto() == True:
            descuento_perfecto = initial*0.5
            print(f"""
Your ID is a Perfect Number! Now you have a 15% of discount
{initial} ----perfect discount----> {initial-descuento_perfecto}
""")
            discount = initial - descuento_perfecto
        else: 
            discount = initial
            descuento_perfecto = 0
        iva = round(discount*0.16, 2)
        self.precio = discount + (iva)
        print(f"""
―――――――――――――――― RECEIPT ――――――――――――――――
Price of the product: {pre_product}
Amount: {cantidad}

Subtotal: {initial}
- Discount: {descuento_perfecto}
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
                self.cantidad = self.cantidad - cantidad
                self.vendidos = self.vendidos + cantidad
                return eleccion, self.precio
            elif eleccion == '9':
                return eleccion
            elif eleccion == '0':
                return eleccion
            else: 
                print("Error. Please enter a valid option.")



class Bebida(Producto):
    def __init__(self, name: str, quiantity: int, price: float, stock: int, restaurant:str, adicional: str):
        super().__init__(name, quiantity, price, stock, restaurant, adicional)

class Comida(Producto):
    def __init__(self, name: str, quiantity: int, price: float, stock: int, restaurant:str, adicional: str):
        super().__init__(name, quiantity, price, stock, restaurant, adicional)