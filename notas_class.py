#Declarar una clase alumno, que contenga el nombre del 
#alumno y su nota, ademas una funcion que permita subir 
#esa nota y otra que le permita bajar la nota

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

def subir_nota(self):
    self.nota +=1
    print(f"nombre: {self.nombre}, nota: {self.nota}")

def bajar_nota(self):
    self.nota -=1
    print(f"nombre: {self.nombre}, nota: {self.nota}")

alumno1=Alumno("Pepe", 5)

bajar_nota(alumno1)
subir_nota(alumno1)
subir_nota(alumno1)
bajar_nota(alumno1)