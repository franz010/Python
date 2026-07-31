# pedimos el nombre del usuario y lo guardamos en la varialble nombre
nombre = input("Ingrese su nombre: ")
# pedimos el apellido del usuario y lo guardamos en la varialble apellido
apellido = input("Ingrese su apellido: ")
# pedimos la edad del usuario y la guardamos en la variable edad
edad = int(input("Ingrese su edad: "))
# pedimos el peso del usuario y lo guardamos en la variable peso
peso = float(input("Ingrese su peso: "))

nombreCompleto = f"mi nombre es {nombre}, y mi apellido es {apellido} y mi edad es {str(edad)}, estoy aprendiendo python, mi peso es {str(peso)} kg"
print(nombreCompleto)
