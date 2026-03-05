#bucles

#while
"""""
my_condicion = 0

while my_condicion < 10:
    print(my_condicion)
    my_condicion +=3
if my_condicion ==10:
    print("Mi condicion es igual a 10")
else:
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condicion < 20:
    my_condicion+=1
    if my_condicion == 15:
        print("Se detiene la ejecucion")
        break
    print("Mi condicion es menor que 20")
    print(my_condicion)
"""

#for

my_lista = [19, 25, 58, 64, 22, 14]

for element in my_lista:
    print(element)

my_diccionario = {"Nombre":"Caye",
                  "Apellido":"Benitez",
                  "Edad":19,
                  "Lenguajes":{"Python","Swift","Kotlin"}}

for element in my_diccionario:
    print(element)
    if element=="Edad":
        
        continue
else:
    print("El bucle for para el diccionario a finalizado")
