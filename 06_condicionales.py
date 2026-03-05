#condicionales

my_condicion = False

if my_condicion==True:
    print("Se ejecuta la condicion del if")

my_condicion = 5 * 1
if my_condicion == 10:
    print("Se ejecuta la condicion del segundo if")


if my_condicion>10:
    print("mayor que 10")

else:
    print("menor o igual que 10")

if my_condicion == 10:
    print("igual a 10")

elif my_condicion < 10:
    print("menor que 10")

else:
    print("mayor que 10")


if my_condicion >10 and my_condicion <20:
    print("mayor que 10 y menor de 20")

else:
    print("menor de 10 o mayor de 20")
print("La ejecucion continua:")
