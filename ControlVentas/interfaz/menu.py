def menu():
    while True:
        print("")
        print(">>>>             MENU            <<<<")
        print("")
        print("1. Imprimir copia de una factura." )
        print("2. Imprimir facturas de un cliente en cierto mes.")
        print("3. Diagrama de barras  de facturas por mes de un año especifico. " )
        print("4. Productos comunes entre dos clientes" )
        print("5. Salir" )
        print("")
        print(">>> Seleccione la opcion ?", end="")

        try:
            opcion = int(input())
            if opcion < 1 or opcion > 5:
                print("Error. opcion no valida")
                input("presione cualquier tecla para volver al menu")
                continue
            return opcion
        except ValueError:
            print("Error opcion no valida.")
            input("Presione cualquier tecla para volver al menu")
            
            
def inicio():
    print(">>>>            MODULO CONTROL DE VENTAS           <<<<")
    Acme_ascii = r"""
                
           █████╗  ██████╗ ███╗   ███╗███████╗
          ██╔══██╗██╔═══██╗████╗ ████║██╔════╝
          ███████║██║      ██╔████╔██║█████╗  
          ██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  
          ██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗
          ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
    """
    print(Acme_ascii)
    print("="*55)
    input( "Pulse  enter para ir a iniciar sesion")
    