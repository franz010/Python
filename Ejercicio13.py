edades = [20,80,10,14,11,21,50]
mayor_de_edad = []
contar_mayores = 0
contar_menores = 0

for edad in edades:
    if edad >= 18:
        contar_mayores += 1
        mayor_de_edad.append(edad)
    else:
        contar_menores += 1
print("La lista de edades es: ", edades)
print("La lista de mayores de edad es: ", mayor_de_edad)
print("La cantidad de mayores de edad es: ", contar_mayores)
print("La cantidad de menores de edad es: ", contar_menores)

cantidad_personas = len(edades)
print("La cantidad de personas son: ", cantidad_personas)