#diccionarios

my_diccionario = dict()

my_other_diccionario = {}

print(type(my_diccionario))

print(type(my_other_diccionario))

my_other_diccionario = {"Nombre":"Caye",
                        "Apellido":"Benitez",
                        "Edad":19}

my_diccionario = {"Nombre":"Caye",
                  "Apellido":"Benitez",
                  "Edad":19,
                  "Lenguajes":{"Python","Swift","Kotlin"}}

print(my_diccionario)
print(my_other_diccionario)

print(len(my_diccionario))
print(len(my_other_diccionario))

print(my_diccionario["Nombre"])
print(my_diccionario["Lenguajes"])

my_diccionario["Nombre"] = "Pedro"
print(my_diccionario["Nombre"])


my_diccionario["Calle"]="Calle si"
print(my_diccionario)

del my_diccionario["Calle"]
print(my_diccionario)

print(my_diccionario.items())
print(my_diccionario.keys())
print(my_diccionario.values())
my_new_diccionario = dict.fromkeys(my_diccionario)
print((my_new_diccionario))

print(list(my_new_diccionario))
print(tuple(my_new_diccionario))
print(set(my_new_diccionario))