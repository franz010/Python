# """crea un algoritmo en python que ingrese 3 notas de cada modulo al final necesito
# necesiTA tener el promedio final  y si el promedio es mayor o igual a 61 APROBADO y si es
# menor a 61 REPROBADO"""

nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 61:
    print("El alumno está APROBADO con el promedio de: ", round(promedio, 2))
else:
    print("El alumno está REPROBADO con el promedio de: ", round(promedio, 2))
