#almacenar en un diccionario un vehículo que contenga numero de matricula y su precio Pregunta al usuario por su precio, devolver 
#un array con aquellas matrículas de aquellos coches con precio superior al introducido

coches={"1234ABC": 15000, 
        "5678DEF": 20000, 
        "9012GHI": 12000, 
        "3456JKL": 18000} 

def filtrar_por_precio(diccionario_coches, precio_limite):
    resultado = []
    
    for matricula, precio in diccionario_coches.items():
        if precio > precio_limite:
            resultado.append(matricula)
            
    return resultado

precio_usuario = float(input("Introduce el precio límite: "))
coches_filtrados = filtrar_por_precio(coches, precio_usuario)
print("Matrículas de coches con precio superior a", precio_usuario, ":", coches_filtrados)

