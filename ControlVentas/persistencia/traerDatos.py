
rutica = "modelo/prueba.txt"

productos =[]
def recibirProductos(ruta):
    
    with open(ruta, 'r') as file:
        
          producto = file.readline()
          
          while producto:  
            
            linea = producto.split(";") 
            
            pro = {   
                "codProd"  : linea[0],
                "desProd"  : linea[1],
                "valorUni" : linea[2]
              }
             
            productos.append(pro)
            producto = file.readline()     
             
    return(productos)



def recibirCliente(ruta):
    
    clientes =[]
    
    with open(ruta, 'r') as file:
        
          producto = file.readline()
          
          while producto:  
            
            linea = producto.split(";") 
            
            pro = {   
                "codCli"  : linea[0],
                "nombre"  : linea[1],
                "telefono" : linea[2]
              }

            clientes.append(pro)
            producto = file.readline()     
             
    return(clientes)

ventas =[]

def recibirVentas(ruta):
    
    with open(ruta, 'r') as file:
        
          producto = file.readline()
          
          while producto:  
            
            linea = producto.split(";") 
            
            pro = {   
                "codFac"        : linea[0],
                "anio"          : linea[1],
                "mes"           : linea[2],
                "dia"           : linea[3],
                "codCli"        : linea[4],
                "codPro"        : linea[5],
                "unidadesProd"  : linea[6],
                "valor"         : linea[7],
                "valorFact"     : linea[8]
              }

            ventas.append(pro)
            producto = file.readline()     
             
    return(ventas)


def obtenerDatosVentas():
  ventas = recibirVentas(rutica)
  return ventas
        
        