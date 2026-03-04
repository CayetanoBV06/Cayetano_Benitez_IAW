#Strings

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))

print(my_string + " " + my_other_string)
my_new_line_string="Este string\ntiene salto de linea"

print(my_new_line_string)

my_tab_string = "este es un string\tcon tabulacion"
print(my_tab_string)

my_scape_string = "\\teste es un string \n escapado"
print(my_scape_string)

#formateo

name, surname, age = "Caye", "Benitez", 35

print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))
print("Mi nombre es {} {} y mi edad es {}" .format(name,surname,age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaqueado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Division

language_slice = language[1:3]
print(language_slice)

#Reverse

reversed_language = language[::-1]

print(reversed_language)

#Funciones
print(language.capitalize())