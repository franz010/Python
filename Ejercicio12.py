#solicitar el peso en kg y su estatura en metros
#caldular4 el indice de masa coorporal = peso/altura 2
#mostrar los resultados de IMC
#clasificar el estado del peso de la persona segun la OMS
#rango de IMC clasificacion
#menor a 18.5  Bajo peso
#25.0 a 29.9 sobrepeso
#30.0 a 34.9 obesidad


peso = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en mts: "))

imc = peso/(altura**2)

if imc < 18.5:
    print("Bajo peso")
elif imc >= 30.0 and imc < 34.9:
    print("con obesidad")
elif imc >= 25.0 and imc <= 29.9:
    print("sobrepeso")


print("El resultado del IMC es: ", imc)
