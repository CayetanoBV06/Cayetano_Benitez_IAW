#declarar dos listas con valores numericos ambas del mismo tamaño, se pide si no son del mismo tamaño visualiza error, 
#en caso de mismo tamaño obtener otra lista con aquellos valores que esten en ambas listas, 
#que sean iguales y que esten en la misma posicion

lista_A=[1,6,8,3]
lista_B=[3,6,2,3]



def Proceso(lista_A, lista_B):
    lista_ambas=[]
    if len(lista_A)!=len(lista_B):
        print("error: tienen distinto tamaño")
        return lista_ambas
    else:
        for i in range(len(lista_A)):
            if lista_A[i]==lista_B[i]:
                lista_ambas.append(lista_A[i])
    return lista_ambas

def Visualizar(lista_ambas):
    for x in lista_ambas:
        print(x)

tab_resul = Proceso(lista_A, lista_B)
Visualizar(tab_resul)