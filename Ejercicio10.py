#"""tienes una lista con las notas finales de un grupo de estudiantes
#donde se aprueba con 51 o mas
#Escribe un programa que recorra la lista y determine cuantos estudiantes 
#aprobaron y reprobaron. Suma todos los estdiantes apr
#"""

notas = [45,50,50,50,50,50]

aprobados = 0
reprobados =0
sumaAprobados = 0
sumaReprobados = 0
promedioAprobados = 0
promedioReprobados = 0

for nota in notas:
    if nota >= 51:
        aprobados += 1
        sumaAprobados += nota
        promedioAprobados = sumaAprobados/aprobados
        
    else:
        reprobados += 1
        promedioReprobados = sumaReprobados/reprobados


print("Estudiantes aprobados: ", aprobados)
print("estudiantes reprobados: ", reprobados)  
print("El promedio de los aprobados es : ",promedioAprobados)
print("El promedio de los aprobados es : ",promedioReprobados)


