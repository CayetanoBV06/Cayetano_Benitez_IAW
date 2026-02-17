#crear una super lista, en la que contenga 5 listas, cada una de esas sublistas, se crean igual que en el ejercicio anterior
def super_lista():
    super_lista=[]
    for i in range (5):
        numeros=[]
        while len(numeros) < 5:
            valor= int(input(f"Introduce un valor numerico para la sublista {i+1}:"))
            if len(numeros)==0 or valor>=numeros[-1]:
                numeros.append(valor)
            else:
                print("El valor debe de ser mayor al anterior")
        super_lista.append(numeros)
        return super_lista
super_lista_completa= super_lista()
print("La super lista es:", super_lista_completa)