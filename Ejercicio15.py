lista_contactos = []

for contacto in range(3):
    nombre_contacto = input("Ingrese el nombre del contacto: ")
    lista_contactos.append(nombre_contacto)

print("La lista de los 3 contactos ordenados es: ", lista_contactos)

lista_ordenada = sorted(lista_contactos)
print("La lista de los 3 contactos ordenados es: ", lista_ordenada)

contacto_eliminar = input("Ingrese el nombre de contacto a eliminar: ")

if contacto_eliminar in lista_contactos:
    lista_contactos.remove(contacto_eliminar)

else:
    print("No se ha encontrado el nombre¡¡¡")

print("La lista de los 3 contactos ordenados es: ", lista_contactos)
    
