alumnos = [
{"nombre": "Ana", "curso": "1ºASIR", "notas": [8, 7, 9, 6, 10]},
{"nombre": "Luis", "curso": "1ºASIR", "notas": [10, 10, 10, 10, 10]},
{"nombre": "Pepe", "curso": "1ºASIR", "notas": [8, 5, 3, 4, 10]}
]
def promedio(alum):
    return sum(alum["notas"]) / len(alum["notas"])

def alumno_con_media_mas_alta(lista_alumnos):
    mejor = max(lista_alumnos, key=promedio)
    return mejor, promedio(mejor)

def Visualizar(alum, media):
    print(f"nombre: {alum['nombre']}")
    print(f"curso: {alum['curso']}")
    print(f"nota media: {media}")

top, media_top = alumno_con_media_mas_alta(alumnos)
Visualizar(top, media_top)
