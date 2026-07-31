#  crea una variable con una contraseña (python123), pide al usuario
#  que ingrese la clave y siga pidiendo con un bucle ehile hasta que el ususario coloque la contraseña correcta

clave = input("Ingrese la contraseña: ")
while clave != "python123":
    clave = input("Ingrese la contraseña: ")
    if clave == "python123":
        print("Contraseña correcta")
    else:
        print("contraseña incorrecta")
