from interfaz.menu import inicio, menu
from modelo.consultas import  consultardatosFactura

inicio()

while True:
    op = menu()

    match op:
        case 1:
            codFact = input ("ingrese el codigo de la factura: ")
            print(consultardatosFactura(codFact)) 
            input("Enter para continuar")
        case 2:
            input("Enter para continuar")
        case 3:
            input("Enter para continuar")
        case 4:
            input("Enter para continuar")
        case 5:
            break
