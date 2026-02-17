#se declara los datos de un alumno, nombre curso notas y las notas en un array, se pide la nota media de ese alumno
alumno = {"nombre": "Ana", "curso": "1ºASIR", "notas": [8, 7, 9, 6, 10]}

def Nota_media(alum):
    suma = 0
    for nota in alum["notas"]:
        suma += nota
    media = suma / len(alum["notas"])
    return media

def Visualizar(alum):
    print(f"nombre: {alum['nombre']}")
    print(f"curso: {alum['curso']}")
    print(f"nota media: {Nota_media(alum)}")

Visualizar(alumno)
