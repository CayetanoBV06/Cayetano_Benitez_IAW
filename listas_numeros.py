#Introducir valores numericos en una lista, maximo 5 valores, de forma ascendente,
#es decir que si el valor es menor que el anterior no se mete en la lista, hacerlo con funciones

def introducir_numero():
    numeros=[]
    while len(numeros) < 5:
        valor= int(input("Introduce un valor numerico:"))
        if len(numeros)==0 or valor>=numeros[-1]:
            numeros.append(valor)
        else:
            print("El valor debe de ser mayor al anterior")
    return numeros


valores= introducir_numero()
print("Los numeros introducidos son:", valores) 
