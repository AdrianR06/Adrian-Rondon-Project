class Estadio:
    def __init__(self, id:str, name:str, city:str, capacity:list, restaurants:list, ocupatedg=["206", "207"], ocupatedvip=["205", "206", "204"]):
        self.id = id
        self.nombre = name
        self.ubicacion = city
        self.capacidad = capacity
        self.restaurantes = restaurants
        self.sitios_generales_ocupados = ocupatedg
        self.sitios_vip_ocupados = ocupatedvip

    def mapa_asientos_general(self):
        asientos = self.capacidad
        print("\nGeneral Sits:")
        for asiento in range(1, asientos[0], 10):
            columna = []
            for i in range(10):
                valor = asiento+i            
                if valor <= asientos[0]:
                    sitio = f"{valor:0{3}}"
                    if sitio not in self.sitios_generales_ocupados:
                        columna.append(sitio)
                    else: columna.append(f"XXX")
                else: break
            print(columna)

    def escoger_asiento_general(self):
        while True:
            print("\nEnter the sit number do you want")
            asiento_escogido = input("-> ")
            if len(asiento_escogido) == 3 and asiento_escogido.isnumeric():
                
                asientos = self.capacidad
                if int(asiento_escogido) in range(1, asientos[0]+1) and asiento_escogido not in self.sitios_generales_ocupados:
                    return asiento_escogido
                else: print("Error. This sit is not available. Please choice another seat.")
                
            elif asiento_escogido == '9':
                return asiento_escogido
            elif asiento_escogido == '0':
                return asiento_escogido
            else: print("\nError. Please enter a valid seat.")
        
    def mapa_asientos_vip(self):
        asientos = self.capacidad
        print("\nVIP Sits:")
        for asiento in range(1, asientos[1], 10):
            columna = []
            for i in range(10):
                valor = asiento + i
                if valor <= asientos[1]:
                    sitio = f"{valor:0{3}}"
                    if sitio not in self.sitios_vip_ocupados:
                        columna.append(sitio)
                    else: columna.append(f"XXX")
                else: break
            print(columna)

    def escoger_asiento_vip(self):
        while True:
            print("\nEnter the sit number do you want")
            asiento_escogido = input("-> ")
            if len(asiento_escogido) == 3 and asiento_escogido.isnumeric():
                
                asientos = self.capacidad
                if int(asiento_escogido) in range(1, asientos[1]+1) and asiento_escogido not in self.sitios_vip_ocupados:
                    return asiento_escogido
                else: print("Error. This sit is not available. Please choice another seat.")
                
            elif asiento_escogido == '9':
                return asiento_escogido
            elif asiento_escogido == '0':
                return asiento_escogido
            else: print("\nError. Please enter a valid seat.")