import funciones as f

def main():
    
    f.abrir_programa()
    lista_equipos, lista_estadios, lista_partidos, lista_clientes = f.leer_archivos()
    f.bienvenida()
    f.menu_principal(lista_equipos, lista_estadios, lista_partidos, lista_clientes)

main()
