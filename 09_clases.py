#clases

class Person:
    pass

print(Person())

class MyPerson:
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname

my_person=MyPerson("Caye", "Benitez")
print(f"{my_person.name} {my_person.surname}")

class MyPerson2:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name=f"{name} {surname} {alias}"

    def walk(self):
        print(f"{self.full_name} Esta caminando")

person=MyPerson2("Caye", "Benitez")
print(person.full_name)
person.walk()