def Visualizar(asignaturas):
    for clave, valor in asignaturas.items():
        print(f"{clave}: {valor} créditos")

def Cred_tot(asig):
    # Usamos .values() para obtener solo los números y sumarlos
    total = sum(asig.values())
    return total

# Bloque principal
asignaturas = {"matemáticas": 6, "física": 4, "química": 5}

Visualizar(asignaturas)

# Guardamos el resultado de la función en una variable para imprimirlo
total_creditos = Cred_tot(asignaturas)
print(f"Total de créditos: {total_creditos}")
