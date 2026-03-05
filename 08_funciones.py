#funciones

def my_funcion ():
    print("Esto es una funcion")

my_funcion()

def sum_dos_valores (first_number, second_number):
    print(first_number + second_number)

sum_dos_valores(5,7 )

def sum_dos_valores_con_return (first_number, second_number):
    return first_number + second_number

resul = sum_dos_valores_con_return(10, 5)
print(resul)

def sum_dos_valores_con_return_dos (first_number, second_number):
    suma = first_number + second_number
    return suma

resul2 = sum_dos_valores_con_return_dos(10, 5)
print(resul2)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Benitez", name="Caye")

def print_name_con_default(name, surname, alias ="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_con_default("Caye", "Benitez")

def print_texts(*text):
    for texts in text:
        print(texts)

print_texts("Hola", "Python", "Caye", "Si")
print_texts("Hola")

def print_upper_texts(*text):
    for texts in text:
        print(texts.upper())
print_upper_texts("Hola", "Python", "Caye", "Si")
print_upper_texts("Hola")