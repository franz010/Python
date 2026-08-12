
frutas = []

num_frutas = int(input("Ingrese la cantidad de frutas: "))

for fruta in range(num_frutas):
    nombre_fruta = input("Ingrese el nombre de la fruta: ")
    frutas.append(nombre_fruta)

#se muestra por pantalla las frutas que se encuentran en la lista
print("La lista de frutas ingresadas es: ", frutas)

eliminar = frutas.remove(input("Ingresa la fruta que quieres eliminar: "))


print("La actual lista de frutas es: ", frutas)