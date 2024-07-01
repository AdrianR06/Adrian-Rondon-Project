# Crear, modificar, actualizar, borrar
from estadio import Estadio
from equipo import Equipo
from partido import Partido
from producto import Comida, Bebida
from cliente import Cliente
from boleto import BoletoGeneral, BoletoVIP
from requests import get
from pickle import dump, load
from re import fullmatch
from uuid import uuid4
from matplotlib import pyplot as chart
import numpy as np


def abrir_programa():
    """Verifica la existencia de un archivo. \n
    En caso de que el archivo no exista, crea los siguientes arcihvos: \n
        - 'archivo_equipos.txt'\n
        - 'archivo_estadios.txt'\n
        - 'archivo_partidos.txt'\n
        - 'archivo_clientes.txt'\n
    Y guarda, en cada uno, una lista de objetos con los datos de su respectiva API.
    """
    print("Initiating program...\n")
    try:
        with open("archivo_equipos.txt") as archivo_equipos:
            print("Opening saved files...")

    except FileNotFoundError:
        print("Downloading data...\n")
        descargar_equipos()
        descargar_estadios()
        descargar_partidos()
        descargar_clientes()


def descargar_equipos():
    """Descarga el contenido de la api de equipos, los transforma a objetos y los guarda en un archivo .txt.
    """
    api_aux = get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json")
    response = api_aux.json()
    equipos = []
    for data in response:
        equipo = Equipo(data['id'], data['code'], data['name'], data['group'])
        equipos.append(equipo)
        
    with open("archivo_equipos.txt", "wb") as archivo_equipos:
        dump(equipos, archivo_equipos)
def descargar_estadios():
    """Descarga el contenido de la api de estadios, los transforma a objetos y los guarda en un archivo .txt.
    """
    api_aux = get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")
    response = api_aux.json()
    estadios = []
    for data in response:
        lista_restaurants = data['restaurants']
        lista_restaurantes = []
        for restaurant in lista_restaurants:
            lista_productos = []
            lista_products = restaurant['products']
            for producto in lista_products:
                if producto['adicional'] == 'package' or producto['adicional'] == 'plate':
                    producto = Comida(producto['name'], producto['quantity'], float(producto['price']), producto['stock'], restaurant['name'], producto['adicional'])
                    lista_productos.append(producto)
                elif producto['adicional'] == 'non-alcoholic' or producto['adicional'] == 'alcoholic':
                    producto = Bebida(producto['name'], producto['quantity'], float(producto['price']), producto['stock'], restaurant['name'], producto['adicional'])
                    lista_productos.append(producto)
            lista_restaurantes.append((restaurant['name'], lista_productos))
        estadio = Estadio(data['id'], data['name'], data['city'], data['capacity'], lista_restaurantes)
        estadios.append(estadio)
        
    with open("archivo_estadios.txt", "wb") as archivo_estadios:
        dump(estadios, archivo_estadios)
def descargar_partidos():
    """Descarga el contenido de la api de partidos, los transforma a objetos y los guarda en un archivo .txt.
    """
    api_aux = get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json")
    response = api_aux.json()
    partidos = []
    for data in response:
        home = data['home']
        home = Equipo(home['id'], home['code'], home['name'], home['group'])
        away = data['away']
        away = Equipo(away['id'], away['code'], away['name'], away['group'])
        partido = Partido(data['id'], data['number'], home, away, data['date'], data['group'], data['stadium_id'])
        partidos.append(partido)

    with open("archivo_partidos.txt", "wb") as archivo_partidos:
        dump(partidos, archivo_partidos)
def descargar_clientes():
    """Genera una pequeña base de datos inicial de objetos Cliente, y los guarda en un archivo .txt.
    """
    npc1 = Cliente("Jorge Rosales", 64738291, 18)
    npc2 = Cliente("Aristides Rey", 87654321, 20)
    npc3 = Cliente("Akira Toriyama", 23456789, 22)
    npc4 = Cliente("Holly Molly", 98765432, 24)
    npc5 = Cliente("Gwen Stacy", 19283746, 26)
    equipo = Equipo("0015bd66-71ce-4869-9d9b-be8b12914dcd","ESP","Spain","B")
    equipo2 = Equipo("eee64995-57ba-4261-be76-4faf9c808fd8","ITA","Italy","B")
    partido = Partido("6cc7f8b0-cf4f-49ce-a0d2-c242b68674b4", 10, equipo, equipo2, "2024-06-20", "Group B", "50542213-b8e8-400e-8353-4e3b3cfa8144", 4)
    ticket1 = BoletoVIP(npc1, partido, 205, None, "V.I.P.", 87.0)
    ticket2 = BoletoVIP(npc1, partido, 206, None, "V.I.P.", 87.0)
    ticket3 = BoletoVIP(npc1, partido, 207, None, "V.I.P.", 87.0)
    ticket4 = BoletoGeneral(npc1, partido, 204, None, "General", 40.6)
    ticket5 = BoletoGeneral(npc1, partido, 205, "ej184b19", "General", 40.6)
    npc1 = Cliente("Jorge Rosales", 64738291, 18, ticket1, 87)
    npc2 = Cliente("Aristides Rey", 87654321, 20, ticket2, 100.3)
    npc3 = Cliente("Akira Toriyama", 23456789, 22, ticket3, 530.7)
    npc4 = Cliente("Holly Molly", 98765432, 24, ticket4, 40.6)
    npc5 = Cliente("Gwen Stacy", 19283746, 26, ticket5, 40.6)
    npcs = [ npc1, npc2, npc3, npc4, npc5]
    with open("archivo_clientes.txt", "wb") as archivo_clientes:
        dump(npcs, archivo_clientes)

def leer_equipos():
    """Lee el archivo .txt correspondiente a los equipos guardados, y los carga al programa.

    Returns:
        lista: lista de objetos Equipo
    """
    with open("archivo_equipos.txt", "rb") as archivo_equipos:
        lista_equipos = load(archivo_equipos)
    return lista_equipos
def leer_estadios():
    """Lee el archivo .txt correspondiente a los estadio guardados, y los carga al programa.

    Returns:
        lista: lista de objetos Estadio
    """
    with open("archivo_estadios.txt", "rb") as archivo_estadios:
        lista_estadios = load(archivo_estadios)
    return lista_estadios
def leer_partidos():
    """Leee el archivo .txt correspondiente a los partidos guardados, y los carga al programa.

    Returns:
        lista: lista de objetos Partido
    """
    with open("archivo_partidos.txt", "rb") as archivo_partidos:
        lista_partidos = load(archivo_partidos)
    return lista_partidos
def leer_clientes():
    """Lee el archivo .txt correspondiente a los clientes guaradaos, y los carga al programa.

    Returns:
        lista: lista de objetos Cliente
    """
    with open("archivo_clientes.txt", "rb") as archivo_clientes:
        lista_clientes = load(archivo_clientes)
    return lista_clientes

def leer_archivos():
    """Lee los siguientes archivos: \n
        - 'archivo_equipos.txt'\n
        - 'archivo_estadios.txt'\n
        - 'archivo_partidos.txt'\n
        - 'archivo_clientes.txt'\n
    Transforma su contenido a una lista de objetos, y lo guarda en cuatro variables.

    Returns:
        tuple: (lista_equipos, lista_estadios, lista_partidos, lista_clientes)
    """
    print("Reading files...\n")
    return leer_equipos(), leer_estadios(), leer_partidos(), leer_clientes()


def actualizar_equipos(lista_equipos:list):
    """Sobreescribe los datos guardados en el archivo .txt correspondiente

    Args:
        lista_equipos (list): nueva lista de equipos
    """
    with open("archivo_equipos.txt", "wb") as archivo_equipos:
        dump(lista_equipos, archivo_equipos)        
def actualizar_estadios(lista_estadios:list):
    """Sobreescribe los datos guardados en el archivo .txt correspondiente

    Args:
        lista_estadios (list): nueva lista de estadios
    """
    with open("archivo_estadios.txt", "wb") as archivo_estadios:
        dump(lista_estadios, archivo_estadios)        
def actualizar_partidos(lista_partidos:list):
    """Sobreescribe los datos guardados en el archivo .txt correspondiente

    Args:
        lista_partidos (list): Nueva lista de partidos 
    """
    with open("archivo_partidos.txt", "wb") as archivo_partidos:
        dump(lista_partidos, archivo_partidos)
def actualizar_clientes(lista_clientes:list):
    """Sobreescribe los datos guardados en el archivo .txt correspondiente

    Args:
        lista_clientes (list): Nueva lista de clientes
    """
    with open("archivo_clientes.txt", "wb") as archivo_clientes:
        dump(lista_clientes, archivo_clientes)

def actualizar_archivos(lista_equipos:list, lista_estadios:list, lista_partidos:list, lista_clientes:list):
    """Actualiza todos los archivos .txt con los nuevos datos del sistema.

    Args:
        lista_equipos (list): Nueva lista equipos
        lista_estadios (list): Nueva lista estadios
        lista_partidos (list): Nueva lista partidos
        lista_clientes (list): Nueva lista clientes
    """
    actualizar_equipos(lista_equipos)
    actualizar_estadios(lista_estadios)
    actualizar_partidos(lista_partidos)
    actualizar_clientes(lista_clientes)


def bienvenida():
    """Muestra en pantalla la bienvenida al programa
    """    
    print("""
 ██     ██ ███████ ██       ██████  ██████  ███    ███ ███████    ████████  ██████  
 ██     ██ ██      ██      ██      ██    ██ ████  ████ ██            ██    ██    ██ 
 ██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████         ██    ██    ██ 
 ██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██            ██    ██    ██ 
  ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████       ██     ██████  
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░███████╗░██╗░░░██╗░██████╗░░░██████╗░░░██████╗░░░██████╗░░██████╗░░██╗░░██╗░░░░
▬▬ ░██╔════╝░██║░░░██║░██╔══██╗░██╔═══██╗░░╚════██╗░██╔═████╗░╚════██╗░██║░░██║░ ▬▬
▓▓ ░█████╗░░░██║░░░██║░██████╔╝░██║░░░██║░░░█████╔╝░██║██╔██║░░█████╔╝░███████║░ ▓▓
▓▓ ░██╔══╝░░░██║░░░██║░██╔══██╗░██║░░░██║░░██╔═══╝░░████╔╝██║░██╔═══╝░░╚════██║░ ▓▓
▬▬ ░███████╗░╚██████╔╝░██║░░██║░╚██████╔╝░░███████╗░╚██████╔╝░███████╗░░░░░░██║░ ▬▬
░░░░╚══════╝░░╚═════╝░░╚═╝░░╚═╝░░╚═════╝░░░╚══════╝░░╚═════╝░░╚══════╝░░░░░░╚═╝░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
⚽︎ ⚽︎ ⚽︎ ⚽︎ ⚽︎ ⚽︎ ⚽︎ ⚽︎ ⚽︎ ⚽︎ ⚽︎ EURO CUP GERMANY 2024 ⚽︎ ⚽︎ ⚽︎ ⚽︎ ⚽︎ ⚽︎ ⚽︎ ⚽︎ ⚽︎ ⚽︎""")

def menu_principal(lista_equipos:list, lista_estadios:list, lista_partidos:list, lista_clientes:list):
    """Ejecuta el código de los 6 módulos desde un menú.\n
    Al cerrar el programa, guarda todos los datos en los archivos .txt correspondientes.

    Args:
        lista_equipos: lista de objetos {Equipo}
        lista_estadios: lista de objetos {Estadio}
        lista_partidos: lista de objetos {Partido}
    """    
    elección = None
    while elección != "0":
        print("\n░░▒▒▓▓█████████████████████████████████ MENU █████████████████████████████████▓▓▒▒░░")
        print("""
Select what you want to manage:
[1] Match and stadium
[2] Ticket sales
[3] Match attendance
[4] Restaurants
[5] Restaurants sales
[6] Statistics

[0] Close program
              """)
        elección = input("Type here -> ")
        if elección == "1":
            elección, lista_equipos, lista_estadios, lista_partidos = gestion_partidos_y_estadios(lista_equipos, lista_estadios, lista_partidos)
        elif elección == "2":
            elección, lista_equipos, lista_estadios, lista_partidos, lista_clientes = gestion_venta_de_entradas(lista_equipos, lista_estadios, lista_partidos, lista_clientes)
        elif elección == "3":
            elección, lista_partidos, lista_clientes = gestion_asistencias_al_partido(lista_partidos, lista_clientes)
        elif elección == "4":
            elección = gestion_restaurantes(lista_estadios)
        elif elección == "5":
            elección, lista_estadios, lista_clientes = gestion_ventas_restaurantes(lista_estadios, lista_clientes)
        elif elección == "6":
            elección, lista_equipos, lista_estadios, lista_partidos, lista_clientes = estadísticas(lista_equipos, lista_estadios, lista_partidos, lista_clientes)
        elif elección == "0":
            break
        else: 
            print("\nError. Please type a valid argument\n")
    
    print("\nSaving data...\n")
    actualizar_archivos(lista_equipos, lista_estadios, lista_partidos, lista_clientes)
    print("Closing program...")    



def gestion_partidos_y_estadios(lista_equipos:list, lista_estadios:list, lista_partidos:list):
    """Ejecuta el programa correspondiente a la gestion de partidos y estdios.\n
    Permite retroceder al menú en cualquier momento. Modifica las variables: 
    - elección\n
    - lista_equipos\n
    - lista_partidos\n
    """
    
    elección = None
    while elección != "0":
        print("""-------------------- Match and Stadium Mangement --------------------
[1] Register teams
[2] Register stadiums
[3] Register matches
[4] Search matches

[9] Go back
[0] Close program
          """)
        elección = input("Type here -> ")
        
        if elección == "1":
            print("\nDownloading teams...\n")
            descargar_equipos()
            lista_equipos = leer_equipos()
            print("Teams successfully registered.\n")
            
        elif elección == "2":
            print("\nDownloading stadiums...\n")
            descargar_estadios()
            lista_estadios = leer_estadios()
            print("Stadiums successfully registered.\n")
            
        elif elección == "3":
            print("\nDownloading matches...\n")
            descargar_partidos()
            lista_partidos = leer_partidos()
            print("Matches successfully registered.\n")
            
        elif elección == "4":
            elección = mostrar_filtrado(lista_estadios, lista_partidos)
                

        elif elección == "9": break
        elif elección == "0": break
        else: print("\nError. Please type a valid argument\n")
    return elección, lista_equipos, lista_estadios, lista_partidos

def buscar_partido(lista_estadios:list, lista_partidos:list):

    filtro = input("Type here -> ")
    lista_filtrada = []
    
    if filtro != "0" and filtro != "9":
        
        for estadio in lista_estadios:
            if filtro.lower() == estadio.nombre.lower():
                id_estadio = estadio.id
                for partido in lista_partidos:
                    if partido.id_estadio == id_estadio:
                        lista_filtrada.append((partido, estadio.nombre))

        for partido in lista_partidos:
            local = partido.local
            nombre_local, código_local = local.nombre, local.codigo_fifa
            
            visitante = partido.visitante
            nombre_visitante, código_visitante = visitante.nombre, visitante.codigo_fifa
            
            if filtro == partido.id:
                id_estadio = partido.id_estadio
                for estadio in lista_estadios:
                    if id_estadio == estadio.id:
                        estadio_nombre = estadio.nombre
                        lista_filtrada.append((partido, estadio_nombre))                
            
            elif filtro.lower() == nombre_local.lower():
                id_estadio = partido.id_estadio
                for estadio in lista_estadios:
                    if id_estadio == estadio.id:
                        estadio_nombre = estadio.nombre
                        lista_filtrada.append((partido, estadio_nombre))
                
            elif filtro.lower() == nombre_visitante.lower():
                id_estadio = partido.id_estadio
                for estadio in lista_estadios:
                    if id_estadio == estadio.id:
                        estadio_nombre = estadio.nombre
                        lista_filtrada.append((partido, estadio_nombre))
                
            elif filtro.lower() == código_local.lower():
                id_estadio = partido.id_estadio
                for estadio in lista_estadios:
                    if id_estadio == estadio.id:
                        estadio_nombre = estadio.nombre
                        lista_filtrada.append((partido, estadio_nombre))
                
            elif filtro.lower() == código_visitante.lower():
                id_estadio = partido.id_estadio
                for estadio in lista_estadios:
                    if id_estadio == estadio.id:
                        estadio_nombre = estadio.nombre
                        lista_filtrada.append((partido, estadio_nombre))
                
            elif filtro == partido.fecha:
                id_estadio = partido.id_estadio
                for estadio in lista_estadios:
                    if id_estadio == estadio.id:
                        estadio_nombre = estadio.nombre
                        lista_filtrada.append((partido, estadio_nombre))
        if len(lista_filtrada) == 0:
            print("\nMatch not found. Please try with another filter.")
        else: pass
    else: pass
    return filtro, lista_filtrada

def mostrar_filtrado(lista_estadios:list, lista_partidos:list):
    elección = None
    while elección != '0' and elección != '9':
        print("""―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
Search a match by:
- Country's name/code
- Stadium's name
- Date (Year-Month-Day)
- Match ID

[9] Go back
[0] Close program
""")    
        elección, lista_filtrada = buscar_partido(lista_estadios, lista_partidos)
        if len(lista_filtrada) != 0:
            for filtro in lista_filtrada:
                partido, nombre_estadio = filtro
                partido.mostrar_detalles(nombre_estadio)
        elif elección == '9': print("\nComing back...\n")
        else: break
    return elección



def gestion_venta_de_entradas(lista_equipos:list, lista_estadios:list, lista_partidos:list, lista_clientes:list):
    """Ejecuta el programa correspondiente a la gestion de venta de entradas.\n
    Permite retroceder al menú en cualquier momento. Modifica las variables: 
    - elección\n
    - lista_equipos\n
    - lista_partidos\n
    - lista_clientes"""
    
    cliente = pedir_datos_cliente(lista_clientes)
    elección = None
    while elección != '0':
        print("""
-------------------- Ticket Sales Mangement --------------------
[1] Show all the matches
[2] Search matches by a filter
[3] Buy a ticket

[9] Go back
[0] Close program
""")
        elección = input("Type here -> ")

        if elección == '1':
            mostrar_partidos(lista_partidos, lista_estadios)
            
        elif elección == '2':
            elección = mostrar_filtrado(lista_estadios, lista_partidos)
        elif elección == '3':
            elección = comprar_entrada(lista_estadios, lista_partidos, cliente)
            
        elif elección == '9': break
        elif elección == '0': break
        else: print("\nError. Please enter a valid argument.\n")
    return elección, lista_equipos, lista_estadios, lista_partidos, lista_clientes

def solo_letras_espacios(cadena:str):
  """
  Función que verifica si una cadena contiene solo letras o espacios en blanco usando expresiones regulares.
  """
  patron = r"[A-Za-z\s]+$"  # Patrón que incluye letras mayúsculas, minúsculas y espacios en blanco
  return fullmatch(patron, cadena) is not None

def buscar_cliente(idc:str, lista_clientes:list):
    validacion = False
    for cliente in lista_clientes:
        if cliente.cedula == idc:
            return cliente
        else: pass
    if validacion == False:
        return False

def pedir_datos_cliente(lista_clientes:list):
    print("\n--------------------- Customer Registration --------------------")
    while True:
        idc = input("\nType your ID:\n-> ")
        if idc.isnumeric() == False:
            print("\nThis ID is not valid. Please enter the ID numbers without points or commas.")
        elif int(idc) > 40000000 or int(idc) < 100000:
            print("This ID is not valid. Pleas enter a valid ID.")
        else: break
    cliente = buscar_cliente(idc, lista_clientes)
    if cliente == False:
        while True:
            name = input("\nType your full name:\n-> ")
            if solo_letras_espacios(name) == False:
                print("\nThis name is not valid. Please use only alphabetic characters.")
            elif len(name) > 35:
                print("\nThis name is too long. Please enter a shorter name.")
            else: 
                name = name.title()
                break
        while True:
            age = input("\nType your age:\n-> ")
            if age.isnumeric() == False:
                print("\nThis age is not valid. Please enter a valid number.")
            elif int(age) > 120:
                print("\nThis age is not valid. There is no way you are that old! Please enter a valid number.")
            else:
                age = int(age)
                break
        cliente = Cliente(name, idc, age)
        lista_clientes.append(cliente)
    else: 
        print(f"\nWelcome again, {cliente.nombre}\n")
        pass
        
    return cliente

def mostrar_partidos(lista_partidos:list, lista_estadios:list):
    for partido in lista_partidos:
        for estadio in lista_estadios:
            if partido.id_estadio == estadio.id:
                nombre_estadio = estadio.nombre
        partido.mostrar_detalles(nombre_estadio)

def comprar_entrada(lista_estadios:list, lista_partidos:list, cliente:Cliente):

    elección, partido, estadio = seleccionar_partido(lista_estadios, lista_partidos)
        
    while elección != '0' and elección != '9':
        print("""
What type of ticket do you want?
[1] General ticket ..................... $35
[2] VIP ticket ......................... $75

[9] Go back
[0] Close program
""")
        elección = input("-> ")
        if elección == '1':
            estadio.mapa_asientos_general()
            asiento = estadio.escoger_asiento_general()
            if asiento != '0' and asiento != '9':
                codigo = generar_codigo_unico()
                ticket = BoletoGeneral(cliente, partido, asiento, codigo)
                elección, gasto = ticket.mostrar_precio()
                if elección != '0' and elección != '9':
                    estadio.sitios_generales_ocupados.append(asiento)
                    cliente.cambiar_ticket(ticket)
                    cliente.sumar_gastos(gasto)
                    ticket.mostrar_ticket(estadio.nombre)
            else: 
                elección = asiento
                break
            break
        
        elif elección == '2':
            estadio.mapa_asientos_vip()
            asiento = estadio.escoger_asiento_vip()
            if asiento != '0' and asiento != '9':
                codigo = generar_codigo_unico()
                ticket = BoletoVIP(cliente, partido, asiento, codigo)
                elección, gasto = ticket.mostrar_precio()
                if elección != '0' and elección != '9':
                    estadio.sitios_vip_ocupados.append(asiento)
                    cliente.cambiar_ticket(ticket)
                    cliente.sumar_historial()
                    cliente.sumar_gastos(gasto)
                    ticket.mostrar_ticket(estadio.nombre)
                
            else: 
                elección = asiento
                break
            break

        elif elección == '9':
            break
        elif elección == '0':
            break
        else: print("\nError. Please enter a valid argument.\n")
    return elección

def seleccionar_partido(lista_estadios, lista_partidos):
    validacion = False
    elección = None
    partido = None
    estadio = None
    while validacion == False and elección != '0':
        print("""
Please, enter the Match ID down here:
    """)
        elección, tuplas = buscar_partido(lista_estadios, lista_partidos)
        if elección == '9': return elección, partido, estadio
        elif elección == '0': return elección, partido, estadio
        if len(tuplas) > 0 and len(tuplas) < 2:
            validacion = True
            print("\nYou have selected this match: \n")
            for tupla in tuplas:
                partido, nombre_estadio = tupla
                partido.mostrar_detalles(nombre_estadio)
            for stadium in lista_estadios:
                if stadium.nombre == nombre_estadio:
                    estadio = stadium
            else: pass
        else:
            pass
        if validacion == False:
            print("\nError. Please enter a valid ID.")
    return elección, partido, estadio

def generar_codigo_unico():
    identificador_unico = uuid4().hex[:8]
    codigo = f"{identificador_unico}" 
    return codigo
    


def gestion_asistencias_al_partido(lista_partidos:list, lista_clientes:list):
    """Ejecuta el programa correspondiente a la gestion de asistencias al partido.\n
    Permite retroceder al menú en cualquier momento. Modifica las variables: 
    - elección
    - lista_partidos\n
    -lista_clientes"""
    elección = None
    while elección != '0':
        print("""-------------------- Match Attendance Mangement --------------------

Enter your ticket unique code down here:
    """)
        elección = input("Type here -> ")
        if elección == '9': break
        elif elección == '0': break
        else:
            validacion = False
            for cliente in lista_clientes:
                ticket = cliente.ticket
                
                if ticket != None:
                    
                    if elección == ticket.codigo:
                        validacion = True
                        ticket.usar_codigo()
                        print("Your ticket was successfully validated")
                        cliente.ticket.partido.sumar_asistencia()
                    else: pass
                    
                else: pass
            if validacion == False:
                print("Error. Your code is incorrect, or was already used.")
    return elección, lista_partidos, lista_clientes




def gestion_restaurantes(lista_estadios:list):
    """Ejecuta el programa correspondiente a la visualizacion de productos de restaurantes.\n
    Permite retroceder al menú en cualquier momento. Modifica las variables: 
    - elección
    - lista_estadio"""
    elección = None
    while elección != '0' and elección != '9':
    
        print("""-------------------- Restaurants Mangement --------------------

Search a product by:
- Product's name ..................... Example: 'Hecho a mano Algodón Teclado'
- Product's clasification ............ food or drink
- Price Range ........................ Example: 300.00
- Restaurant ......................... Example: 'Urrutia y Pelayo'

[9] Go back
[0] Close program
""")
        filtro = input("Type here -> ")
        lista_filtrada = buscar_producto(filtro, lista_estadios)
        mostrar_productos_filtrados(lista_filtrada)
        elección = filtro
        if elección == '9': break
        elif elección == '0': break
    return elección

def buscar_producto(filtro, lista_estadios):
    
    lista_filtrada = []
    
    if filtro != '0' and filtro != '9':
        for estadio in lista_estadios:
            lista_restaurantes = estadio.restaurantes
            for restaurante in lista_restaurantes:
                nombre_restaurante = restaurante[0]
                lista_productos = restaurante[1]

                if filtro.isnumeric() == False:
                    if filtro.lower() == 'food':
                        for producto in lista_productos:
                            if type(producto) == Comida:
                                lista_filtrada.append(producto)
                    
                    elif filtro.lower() == 'drink':
                        for producto in lista_productos:
                            if type(producto) == Bebida:
                                lista_filtrada.append(producto)
                    
                    else:
                        for producto in lista_productos:
                            if filtro.lower() == nombre_restaurante.lower():
                                lista_filtrada.append(producto)
                            elif filtro.lower() == producto.nombre.lower():
                                lista_filtrada.append(producto)
                            else: pass
                                
                            
                else:
                    if int(filtro) in range(50,1000):
                        filtrofloat = float(filtro)
                        filtroint = int(filtro)
                        if filtroint > 0 and filtroint < 1000:
                            for producto in lista_productos:
                                if producto.precio == filtrofloat:
                                    lista_filtrada.append(producto)
                                elif producto.precio in range(filtroint-50, filtroint):
                                    lista_filtrada.append(producto)
                                elif producto.precio in range(filtroint, filtroint+50):
                                    lista_filtrada.append(producto)
        if len(lista_filtrada) == 0:
            print("Product not found. Please try another filter.\n")
        else:pass
    else:pass
    return lista_filtrada
    
def mostrar_productos_filtrados(lista_filtrada:list):
    for producto in lista_filtrada:
        producto.mostrar_detalles()



def gestion_ventas_restaurantes(lista_estadios:list, lista_clientes:list):
    """Ejecuta el programa correspondiente a la gestion de ventas de los restaurantes.\n
    Permite retroceder al menú en cualquier momento. Modifica las variables: 
    - elección \n
    - lista_estadios\n
    - lista_clientes\n
    """
    cliente = pedir_datos_cliente(lista_clientes)
    if cliente.ticket == None:
        print("You do not have any ticket yet. Buy a ticket if you want to buy anything here.")
        elección = '9'
    elif type(cliente.ticket) == BoletoGeneral:
        print("Sorry, only customers whit V.I.P. tickets can buy here.")
        elección = '9'
    else: elección = None
    
    while elección!='0' and elección!='9':
        ticket = cliente.ticket
        partido = ticket.partido
        idestadio = partido.id_estadio
        for estadio in lista_estadios:
            if idestadio == estadio.id:
                estadio_cliente = estadio
        lista_restaurantes = estadio_cliente.restaurantes
        while elección != '0':
            print("""-------------------- Restaurants Sales Mangement --------------------

You can search products of the following restaurants in this stadium:\n""")
            nombres_restaurantes = []
            for i in range(1, len(lista_restaurantes)):
                restaurante = lista_restaurantes[i]
                nombre_restaurante = restaurante[0]
                print(f"[{i}] {nombre_restaurante}")
                nombres_restaurantes.append(nombre_restaurante)
            print("")
            
            filtro = input("Type here -> ")
            
            for j in range(1, len(lista_restaurantes)):
                if filtro == str(j):
                    restaurante = lista_restaurantes[j]
                    filtro = restaurante[0]
                    break
                else:pass
            if filtro == '9': 
                elección = filtro
                break
            elif filtro == '0': 
                elección = filtro
                break
            
            if elección != '0' and elección != '9': 
                lista_filtrada = buscar_producto(filtro, lista_estadios)
                
                
                productos_filtrados = []
                validacion = False
                for producto in lista_filtrada:
                    if producto.restaurante in nombres_restaurantes:
                        validacion = True
                        producto.mostrar_detalles()
                        productos_filtrados.append(producto)
                    else: pass
                if validacion == False:
                    print("\nError. No products were found in the stadium restaurants.\n")
                else: pass
            
            if len(productos_filtrados) != 1:
                while True: 
                    print("\nEnter the name of the product you want to buy.\n")
                    nombre_producto = input("-> ")
                    validacion = False
                    if nombre_producto == '9': break
                    elif nombre_producto == '0': break
                    for product in productos_filtrados:
                
                        if product.nombre.lower() == nombre_producto.lower():
                            validacion = True
                            producto = product
                            break
                        else:
                            pass
                    
                    if validacion == False:
                        print("\nError. Product not found. Try with another name.")
                    else: break
            else: producto = productos_filtrados[0]
            
            if cliente.edad < 18 and producto.tipo == 'alchoholic':
                print("You can not buy alcoholic drinks. Please choose another product.")
                elección == '9'
            else:
                while True:
                    print("\nYou have seleceted this product:\n")
                    producto.mostrar_detalles()
                    
                    print("\nHow many products do you want?\n")
                    cantidad = input("-> ")
                    if cantidad.isnumeric() == False:
                        print("Error. Please enter only numbers.")
                    elif int(cantidad) > producto.cantidad:
                        print("Error. You have selected more products than available. Please enter a smaller amount")
                    elif int(cantidad) < 0:
                        print("Error. Negative numbers are not a valid option. Please enter a valid amount")
                    else: 
                        cantidad = int(cantidad)
                        break
                    
                elección, gasto = producto.mostrar_precio(cliente, cantidad)
                    
                if elección == '1':
                    cliente.sumar_gastos(gasto)
                    print("\nYour purchase has been completed successfully.\n")
                elif elección == '9':
                    print("\nCanceling the purchase...\n")
                    break
                elif elección == '0':
                    break

    return elección, lista_estadios, lista_clientes



def estadísticas(lista_equipos:list, lista_estadios:list, lista_partidos:list, lista_clientes:list):
    """Ejecuta el programa correspondiente a la gestion de asistencias al partido.\n
    Permite retroceder al menú en cualquier momento. Modifica las variables: 
    - elección\n
    - lista_equipos\n
    - lista_partidos\n
    - lista_estadios\n
    - lista_clientes\n"""
    elección = None
    while elección != '0':
        print("""-------------------- Statistics --------------------
[1] Average spending of a VIP client in a match
[2] Match attendance table
[3] Match with more assists
[4] Match with more tickets
[5] Top 3 best-selling products in the restaurant
[6] Top 3 clients who bought tickets the most

[9] Go back
[0] Close program
            """)
        elección = input("Type here -> ")
        
        if elección == '1':
            average(lista_clientes)
            
        elif elección == '2':
            lista_partidos = ordenar_por_asistencias(lista_partidos)
            mostrar_asistencias(lista_partidos, lista_estadios, lista_clientes)
        
        elif elección == '3':
            lista_partidos = ordenar_por_asistencias(lista_partidos)
            partido = lista_partidos[0]
            for estadio in lista_estadios:
                if partido.id_estadio == estadio.id:
                    nombre_estadio = estadio.nombre
            partido.mostrar_asistencias(nombre_estadio)
            
        elif elección == '4':
            lista_partidos = ordenar_por_tickets(lista_partidos,lista_clientes)
            partido = lista_partidos[0]
            for estadio in lista_estadios:
                if partido.id_estadio == estadio.id:
                    nombre_estadio = estadio.nombre
            partido.mostrar_asistencias(nombre_estadio)
            pass
        elif elección == '5':
            pass
        elif elección == '6':
            lista_clientes = ordenar_boletos_comprados(lista_clientes)
        elif elección == '9':
            break
        elif elección == '0':
            break
    return elección, lista_equipos, lista_estadios, lista_partidos, lista_clientes

def average(lista_clientes):
    lista_vips = []
    gastos = 0
    for cliente in lista_clientes:
        if type(cliente.ticket) == BoletoVIP:
            lista_vips.append(cliente)
            gastos += cliente.gastos
    
    promedio = round(gastos / len(lista_vips), 2)
    print(f"An average VIP client spends {promedio}$ in total each match.")

def ordenar_por_asistencias(lista_partidos):
    """Ordena y muestra de mayor a menor, con el Método Selection Sort, la lista de argumento."""
    
    
    largo = len(lista_partidos)
        
    for i in range(largo): 
      
        # Encontrar el minimo elemento de los restantes sin ordenar
        maximo = i 
        for j in range(i+1, largo):
            a = lista_partidos[maximo] 
            b = lista_partidos[j]
            if a.asistencias < b.asistencias: 
                maximo = j 
                
        # Cambiamos el elemento minimo encontrado con el primer elemento de la matriz
        lista_partidos[i], lista_partidos[maximo] = lista_partidos[maximo], lista_partidos[i]
        # Repetimos el proceso hasta terminar
    return lista_partidos

def ordenar_por_tickets(lista_partidos, lista_clientes):
    """Ordena y muestra de mayor a menor, con el Método Selection Sort, la lista de argumento."""
                
    largo = len(lista_partidos)
        
    for i in range(largo): 
      
        # Encontrar el minimo elemento de los restantes sin ordenar
        maximo = i 
        for j in range(i+1, largo):
            a = lista_partidos[maximo] 
            b = lista_partidos[j]
            
            if a.asistencias < b.asistencias: 
                maximo = j 
                
        # Cambiamos el elemento minimo encontrado con el primer elemento de la matriz
        lista_partidos[i], lista_partidos[maximo] = lista_partidos[maximo], lista_partidos[i]
        # Repetimos el proceso hasta terminar
    return lista_partidos

def mostrar_asistencias(lista_partidos, lista_estadios, lista_clientes):
    print("\nTOP 3 MATCHES MORE ASSISTED\n")
    lista_boletos_vendidos = []
    lista_asistencias = []
    for m,partido in enumerate(lista_partidos):
        for cliente in lista_clientes:
            ticket = cliente.ticket
            if ticket.partido == partido:
                lista_boletos_vendidos.append(cliente)
                if ticket.codigo != None:
                    lista_asistencias.append(cliente)
        if m < 3:
            for estadio in lista_estadios:
                if partido.id_estadio == estadio.id:
                    nombre_estadio = estadio.nombre
                    partido.mostrar_asistencias(nombre_estadio)

        else:
            for estadio in lista_estadios:
                if partido.id_estadio == estadio.id:
                    nombre_estadio = estadio.nombre
            print("{:.<65}".format(f"#{partido.número}: {partido.local.nombre} V.S. {partido.visitante.nombre} in {nombre_estadio}"),end="")
            print("{:.>30}".format(f"....{partido.asistencias} assists   {len(lista_boletos_vendidos)} tickets selled"))
    
def ordenar_boletos_comprados(lista_clientes):
    """Ordena y muestra de mayor a menor, con el Método Selection Sort, la lista de argumento."""
    
    
    largo = len(leer_clientes)
        
    for i in range(largo): 
      
        # Encontrar el minimo elemento de los restantes sin ordenar
        maximo = i 
        for j in range(i+1, largo):
            a = lista_clientes[maximo] 
            b = lista_clientes[j]
            if a.historial < b.historial: 
                maximo = j 
                
        # Cambiamos el elemento minimo encontrado con el primer elemento de la matriz
        lista_clientes[i], lista_clientes[maximo] = lista_clientes[maximo], lista_clientes[i]
        # Repetimos el proceso hasta terminar
    return lista_clientes

def mostrar_grafico(datox,datoy):
    x = np.linspace(1, len(datox))
    y = np.linspace(30, datoy)
    chart.plot(x, y)
    chart.xlabel("VIP clients")
    chart.ylabel("Expenses")
    chart.title("Average spending of a VIP client in a match")
    chart.grid(True)
    chart.show()
    
    