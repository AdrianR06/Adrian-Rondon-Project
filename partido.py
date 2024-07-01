from equipo import Equipo
class Partido:
    def __init__(self, id:str, number:int, home:Equipo, away:Equipo, date:str, group:str, stadium_id:str, attendances=0):
        self.id = id
        self.número = number
        self.local = home
        self.visitante = away
        self.fecha = date
        self.grupo = group
        self.id_estadio = stadium_id
        self.asistencias = attendances
    
    def mostrar_detalles(self, estadio_nombre):
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("{:>30}".format("Home   "),end="")
        print("{:<30}".format("   Away"))
        print("{:>28}".format(f"{self.local.nombre}"),end="")
        print(" V.S.", end="")
        print("{:<30}".format(f"{self.visitante.nombre}"))
        print(f"""------------------------------------------------------------
    Match Number {self.número}
    {self.grupo}
    Date: {self.fecha}
    Stadium: {estadio_nombre}
    Match ID: {self.id}
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
""")
        
    def mostrar_asistencias(self, estadio_nombre):
        print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("{:>30}".format("Home   "),end="")
        print("{:<30}".format("   Away"))
        print("{:>28}".format(f"{self.local.nombre}"),end="")
        print(" V.S.", end="")
        print("{:<30}".format(f"{self.visitante.nombre}"))
        print(f"""------------------------------------------------------------
    Match Number {self.número}
    {self.grupo}
    Date: {self.fecha}
    Stadium: {estadio_nombre}                Assists: {self.asistencias}
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
""")
    
    def sumar_asistencia(self):
        self.asistencias += 1