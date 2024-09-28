from persistencia.traerDatos import obtenerDatosVentas

datosVentas = obtenerDatosVentas()

def consultardatosFactura(codFactura):
    
    try:
        # Buscar la factura  por código
        factura = next((fac for fac in datosVentas if fac['codFac'] == codFactura), None)
        if not factura:
            print(f"factura con código {codFactura} no encontrado.")
            return []
        
        # Obtener los datos de la factura 
                         
        print(f"El codigo es : {factura['codFac' ]}" )      
        print(f"El año es : {factura['anio']}" )        
        print(f"El mes de : {factura['mes']}")           
        print(f"El dia de : {factura['dia']}")              
        print("el codigo del cliente es: ", factura["codCli"])         
        print("codigo del producto: ",factura["codPro" ] )       
        print("unidades de producto: ", factura["unidadesProd"] )  
        print("valor de la factura: ", factura["valor" ] )       
        print("valor facturado: ", factura["valorFact"] )     
            
        # Retornar la lista de datosFactura
    
    except FileNotFoundError as e:
        print(e)
        return []  # Retornar lista vacía en caso de error
    
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        return []  # Retornar lista vacía en caso de error