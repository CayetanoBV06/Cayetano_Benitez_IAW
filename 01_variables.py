#Variables

#forma correcta de nombrar variable
my_variable = "My string variable"
print(my_variable)

my_int_variable = 10
print(my_int_variable)

my_bool_var = True
print(my_bool_var)

#Concatenacion de variables en un print
print(my_variable, my_bool_var, my_int_variable)

#Algunas Funciones del sistema
print(len(my_variable))

print("Este es el valor de: ", my_bool_var)

#variables en una sola linea
name, surname, alias, edad= "Cayetano", "Benitez", "Caye", 19
print("me llamo",name, surname,"Mi edad es", edad, "Y mi alias es:", alias)


#Inputs
first_name = input("Escribe tu nombre")
age = input("Cual es tu edad")

print(first_name)
print(age)

#Forzamos el tipo, es unicamente para llevarlo de ayuda/guia de que tipo queremos que sea
address:str = "Mi direccion"
address = 32
print(address)