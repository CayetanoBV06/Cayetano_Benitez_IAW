#lista formada por un nombre y las notas de ese alumno, crear un diccionario, donde la clave sea el nombre y el valor las notas
def crear_diccionario(lista):
    nombre= lista[0]
    notas= lista[1:]
    return{nombre: notas}


alumno=["Pepe", 5, 3, 8]
resul=crear_diccionario(alumno)
print(resul)