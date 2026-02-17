tab_nombres=[]
tab_edades=[]
def CargaNombres(tab_nom):
    for x in range(5):
        valor=int(input("Ingrese un nombre:"))
        tab_nom.append(valor)
        return tab_edades

def CargarEdades (tad_edad):
    valor=int(input("Ingrese edad:"))
    tab_edad.append(valor)
    return tab_edad

def Visualizar(tab_nom,tab_edad):
    for x in range(5):
        if tab_edad[x]>=18:
            print(tab_nom[x])


CargaNombres(tab_nombres)
CargarEdades(tab_edades)
Visualizar(tab_nombres,tab_edades)